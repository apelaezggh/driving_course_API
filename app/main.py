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
import random

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
    
    # Create user with default role
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password
    )
    
    # Add default user role
    user_role = db.query(models.Role).filter(models.Role.name == "user").first()
    if not user_role:
        user_role = models.Role(name="user")
        db.add(user_role)
        db.commit()
        db.refresh(user_role)
    
    db_user.roles.append(user_role)
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
    
    # Add permission information for each topic
    for topic in topics:
        permission = db.query(models.UserTopicPermission).filter(
            models.UserTopicPermission.user_id == current_user.id,
            models.UserTopicPermission.topic_id == topic.id,
            models.UserTopicPermission.is_active == True
        ).first()
        topic.has_permission = permission is not None or auth.is_admin(current_user)
    
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
    # Check if user has permission for this topic
    if not auth.is_admin(current_user):
        permission = db.query(models.UserTopicPermission).filter(
            models.UserTopicPermission.user_id == current_user.id,
            models.UserTopicPermission.topic_id == topic_id,
            models.UserTopicPermission.is_active == True
        ).first()
        if not permission:
            raise HTTPException(status_code=403, detail="No permission for this topic")
    
    questions = db.query(models.Question).filter(models.Question.topic_id == topic_id).all()
    return questions

# Progress endpoints
@app.post("/progress/", response_model=schemas.UserProgress)
def update_progress(
    progress: schemas.UserProgressCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    # Verify the question belongs to a topic the user has permission for
    question = db.query(models.Question).filter(models.Question.id == progress.question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    if not auth.is_admin(current_user):
        permission = db.query(models.UserTopicPermission).filter(
            models.UserTopicPermission.user_id == current_user.id,
            models.UserTopicPermission.topic_id == question.topic_id,
            models.UserTopicPermission.is_active == True
        ).first()
        if not permission:
            raise HTTPException(status_code=403, detail="No permission for this topic")
    
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
    # Check if user has permission for this topic
    if not auth.is_admin(current_user):
        permission = db.query(models.UserTopicPermission).filter(
            models.UserTopicPermission.user_id == current_user.id,
            models.UserTopicPermission.topic_id == topic_id,
            models.UserTopicPermission.is_active == True
        ).first()
        if not permission:
            raise HTTPException(status_code=403, detail="No permission for this topic")
    
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

# Permission management endpoints (admin only)
@app.post("/admin/grant-permission", response_model=schemas.UserTopicPermission)
def grant_permission(
    permission: schemas.GrantPermission,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    if not auth.is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    
    # Check if permission already exists
    existing_permission = db.query(models.UserTopicPermission).filter(
        models.UserTopicPermission.user_id == permission.user_id,
        models.UserTopicPermission.topic_id == permission.topic_id,
        models.UserTopicPermission.is_active == True
    ).first()
    
    if existing_permission:
        raise HTTPException(status_code=400, detail="Permission already granted")
    
    db_permission = models.UserTopicPermission(
        user_id=permission.user_id,
        topic_id=permission.topic_id,
        granted_by=current_user.id
    )
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission

@app.post("/admin/revoke-permission")
def revoke_permission(
    permission: schemas.RevokePermission,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    if not auth.is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db_permission = db.query(models.UserTopicPermission).filter(
        models.UserTopicPermission.user_id == permission.user_id,
        models.UserTopicPermission.topic_id == permission.topic_id,
        models.UserTopicPermission.is_active == True
    ).first()
    
    if not db_permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    
    db_permission.is_active = False
    db.commit()
    return {"message": "Permission revoked successfully"}

@app.get("/admin/users", response_model=List[schemas.User])
def get_users(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    if not auth.is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    
    users = db.query(models.User).all()
    return users

# Question management endpoints (admin only)
@app.post("/admin/questions/", response_model=schemas.Question)
def create_question_admin(
    question: schemas.QuestionCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    if not auth.is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    
    # Verify topic exists
    topic = db.query(models.Topic).filter(models.Topic.id == question.topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    db_question = models.Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

@app.delete("/admin/questions/{question_id}")
def delete_question(
    question_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    if not auth.is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    
    question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    # Delete related progress records first
    db.query(models.UserProgress).filter(models.UserProgress.question_id == question_id).delete()
    
    # Delete the question
    db.delete(question)
    db.commit()
    return {"message": "Question deleted successfully"}

@app.get("/admin/questions/", response_model=List[schemas.Question])
def get_all_questions(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    if not auth.is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    
    questions = db.query(models.Question).all()
    return questions

# User management endpoints (admin only)
@app.delete("/admin/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    if not auth.is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    
    if user_id == current_user.id:
        raise HTTPException(status_code=400, detail="Cannot delete yourself")
    
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if user is admin
    if any(role.name == "admin" for role in user.roles):
        raise HTTPException(status_code=400, detail="Cannot delete admin users")
    
    # Delete related records first
    db.query(models.UserProgress).filter(models.UserProgress.user_id == user_id).delete()
    db.query(models.UserTopicPermission).filter(models.UserTopicPermission.user_id == user_id).delete()
    
    # Remove user from roles
    user.roles.clear()
    
    # Delete the user
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

# Get user permissions endpoint
@app.get("/admin/users/{user_id}/permissions", response_model=List[schemas.UserTopicPermission])
def get_user_permissions(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    if not auth.is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    permissions = db.query(models.UserTopicPermission).filter(
        models.UserTopicPermission.user_id == user_id,
        models.UserTopicPermission.is_active == True
    ).all()
    
    return permissions

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