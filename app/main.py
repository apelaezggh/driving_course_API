from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import func
from typing import List
import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta

from . import models, schemas, auth
from .database import engine, get_db

load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Driving Course API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database configuration
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "driving_course")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Welcome to Driving Course API"}

# Authentication endpoints
@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Topic endpoints
@app.post("/topics/", response_model=schemas.Topic)
def create_topic(
    topic: schemas.TopicCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    if not auth.is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    db_topic = models.Topic(**topic.dict())
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic

@app.get("/topics/", response_model=List[schemas.Topic])
def get_topics(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    topics = db.query(models.Topic).all()
    return topics

# Question endpoints
@app.post("/questions/", response_model=schemas.Question)
def create_question(
    question: schemas.QuestionCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    if not auth.is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    db_question = models.Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

@app.get("/questions/{topic_id}", response_model=List[schemas.Question])
def get_questions(
    topic_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    questions = db.query(models.Question).filter(models.Question.topic_id == topic_id).all()
    return questions

# Progress endpoints
@app.post("/progress/", response_model=schemas.UserProgress)
def update_progress(
    progress: schemas.UserProgressCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    db_progress = db.query(models.UserProgress).filter(
        models.UserProgress.user_id == current_user.id,
        models.UserProgress.question_id == progress.question_id
    ).first()

    if not db_progress:
        db_progress = models.UserProgress(
            user_id=current_user.id,
            question_id=progress.question_id
        )
        db.add(db_progress)

    db_progress.attempts += 1
    db_progress.correct_attempts += 1 if progress.correct_attempts > db_progress.correct_attempts else 0
    db_progress.last_attempt = datetime.utcnow()

    # Calculate learning score (0 to 1)
    if db_progress.attempts > 0:
        db_progress.learning_score = db_progress.correct_attempts / db_progress.attempts
        # Mark as learned if score is above 0.8 and at least 3 attempts
        db_progress.is_learned = db_progress.learning_score >= 0.8 and db_progress.attempts >= 3

    db.commit()
    db.refresh(db_progress)
    return db_progress

# Quiz generation
@app.get("/quiz/{topic_id}", response_model=schemas.Quiz)
def generate_quiz(
    topic_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    # Get questions that are not learned
    learned_questions = db.query(models.UserProgress.question_id).filter(
        models.UserProgress.user_id == current_user.id,
        models.UserProgress.is_learned == True
    ).subquery()

    available_questions = db.query(models.Question).filter(
        models.Question.topic_id == topic_id,
        ~models.Question.id.in_(learned_questions)
    ).all()

    if not available_questions:
        # If all questions are learned, get some random questions
        available_questions = db.query(models.Question).filter(
            models.Question.topic_id == topic_id
        ).order_by(func.random()).limit(5).all()

    quiz_questions = []
    for question in available_questions:
        # Get the correct language version
        lang = current_user.language
        question_text = getattr(question, f"question_{lang}")
        options = [
            getattr(question, f"option1_{lang}"),
            getattr(question, f"option2_{lang}"),
            getattr(question, f"option3_{lang}")
        ]
        quiz_questions.append(schemas.QuizQuestion(
            id=question.id,
            question=question_text,
            options=options
        ))

    return schemas.Quiz(questions=quiz_questions)

# Language preference
@app.put("/users/language", response_model=schemas.User)
def update_language(
    language: schemas.LanguagePreference,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    if language.language not in ["en", "es"]:
        raise HTTPException(status_code=400, detail="Invalid language")
    current_user.language = language.language
    db.commit()
    db.refresh(current_user)
    return current_user 