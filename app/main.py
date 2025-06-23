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
import re

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
    print(f"Login attempt for username: {form_data.username}")
    print(f"Password provided: {'Yes' if form_data.password else 'No'}")
    
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    print(f"Authentication result: {'Success' if user else 'Failed'}")
    
    if not user:
        print("Login failed - user not found or password incorrect")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    print(f"Login successful for user: {user.email} (ID: {user.id})")
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    
    response_data = {"access_token": access_token, "token_type": "bearer", "email": user.email, "id": user.id, "name": user.name, "lastname": user.lastname, "is_admin": user.is_admin}
    print(f"Returning token response: {response_data}")
    return response_data

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Check if phone already exists
    db_user_phone = db.query(models.User).filter(models.User.phone == user.phone).first()
    if db_user_phone:
        raise HTTPException(status_code=400, detail="Phone number already registered")
    
    # Validate email format
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, user.email):
        raise HTTPException(status_code=400, detail="Invalid email format")
    
    # Validate phone format (more flexible validation)
    # Remove all non-digit characters and check if it's a valid length
    phone_digits = re.sub(r'\D', '', user.phone)
    if len(phone_digits) < 10 or len(phone_digits) > 15:
        raise HTTPException(status_code=400, detail="Phone must have between 10 and 15 digits")
    
    # Validate required fields
    if not user.name or not user.name.strip():
        raise HTTPException(status_code=400, detail="Name is required")
    if not user.lastname or not user.lastname.strip():
        raise HTTPException(status_code=400, detail="Last name is required")
    if not user.email or not user.email.strip():
        raise HTTPException(status_code=400, detail="Email is required")
    if not user.phone or not user.phone.strip():
        raise HTTPException(status_code=400, detail="Phone is required")
    if not user.password or len(user.password) < 6:
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters")
    
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(
        name=user.name.strip(),
        lastname=user.lastname.strip(),
        email=user.email.lower().strip(),
        phone=user.phone.strip(),
        hashed_password=hashed_password,
        language=user.language
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
    
    # Add permission and progress information for each topic
    for topic in topics:
        permission = db.query(models.UserTopicPermission).filter(
            models.UserTopicPermission.user_id == current_user.id,
            models.UserTopicPermission.topic_id == topic.id,
            models.UserTopicPermission.is_active == True
        ).first()
        topic.has_permission = permission is not None or auth.is_admin(current_user)
        
        # Get learning progress for this topic
        if topic.has_permission:
            # Get all questions for this topic
            total_questions = db.query(models.Question).filter(
                models.Question.topic_id == topic.id
            ).count()
            
            # Get learned questions for this topic
            learned_questions = db.query(models.Question).join(
                models.UserProgress
            ).filter(
                models.Question.topic_id == topic.id,
                models.UserProgress.user_id == current_user.id,
                models.UserProgress.is_learned == True
            ).count()
            
            topic.total_questions = total_questions
            topic.learned_questions = learned_questions
            topic.learning_progress = round((learned_questions / total_questions * 100) if total_questions > 0 else 0, 1)
            topic.is_mastered = learned_questions == total_questions and total_questions > 0
        else:
            topic.total_questions = 0
            topic.learned_questions = 0
            topic.learning_progress = 0
            topic.is_mastered = False
    
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
    print(f"Progress update - User: {current_user.id}, Question: {progress.question_id}")
    print(f"Progress data received: {progress.dict()}")
    
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
        print(f"Creating new progress record for user {current_user.id}, question {progress.question_id}")
        db_progress = models.UserProgress(
            user_id=current_user.id,
            question_id=progress.question_id,
            attempts=0,
            correct_attempts=0,
            is_learned=False,
            learning_score=0.0
        )
        db.add(db_progress)
    else:
        # Ensure all fields are properly initialized
        if db_progress.attempts is None:
            db_progress.attempts = 0
        if db_progress.correct_attempts is None:
            db_progress.correct_attempts = 0
        if db_progress.is_learned is None:
            db_progress.is_learned = False
        if db_progress.learning_score is None:
            db_progress.learning_score = 0.0

    print(f"Current progress - attempts: {db_progress.attempts}, correct: {db_progress.correct_attempts}, learned: {db_progress.is_learned}")
    
    # Ensure correct_attempts is a number
    current_correct_attempts = db_progress.correct_attempts or 0
    
    # The frontend sends 1 if correct, 0 if incorrect
    is_correct = progress.correct_attempts == 1
    print(f"Is correct: {is_correct}")
    
    db_progress.attempts += 1
    if is_correct:
        db_progress.correct_attempts = current_correct_attempts + 1
        # Check for 3 consecutive correct answers
        if db_progress.correct_attempts >= 3:
            db_progress.is_learned = True
            print(f"Question {progress.question_id} marked as learned!")
    else:
        # Reset consecutive correct count if answer was wrong
        db_progress.correct_attempts = 0
        db_progress.is_learned = False
        print(f"Question {progress.question_id} reset - wrong answer")
    
    db_progress.last_attempt = datetime.utcnow()

    # Calculate learning score (0 to 1)
    if db_progress.attempts > 0:
        db_progress.learning_score = db_progress.correct_attempts / db_progress.attempts

    print(f"Updated progress - attempts: {db_progress.attempts}, correct: {db_progress.correct_attempts}, learned: {db_progress.is_learned}, score: {db_progress.learning_score}")

    db.commit()
    db.refresh(db_progress)
    return db_progress

@app.get("/progress/{question_id}", response_model=schemas.UserProgress)
def get_progress(
    question_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    # Verify the question belongs to a topic the user has permission for
    question = db.query(models.Question).filter(models.Question.id == question_id).first()
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
        models.UserProgress.question_id == question_id
    ).first()

    if not db_progress:
        # Return default progress if none exists
        return schemas.UserProgress(
            id=0,
            user_id=current_user.id,
            question_id=question_id,
            attempts=0,
            correct_attempts=0,
            is_learned=False,
            learning_score=0.0,
            last_attempt=datetime.utcnow()
        )
    
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
    
    # Get topic and its target_quiz_size
    topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    target_quiz_size = topic.target_quiz_size or 10  # How many questions the quiz should have
    
    # Get total questions for this topic
    total_questions = db.query(models.Question).filter(
        models.Question.topic_id == topic_id
    ).count()
    
    # Always show the same message format for unavailable quizzes
    if total_questions == 0:
        raise HTTPException(
            status_code=404, 
            detail="Quiz no disponible."
        )
    
    # Check if we have enough questions for the target quiz size
    if total_questions < target_quiz_size:
        raise HTTPException(
            status_code=404, 
            detail="Quiz no disponible."
        )
    
    # Get user's progress for this topic
    user_progress = db.query(models.UserProgress).filter(
        models.UserProgress.user_id == current_user.id,
        models.UserProgress.question_id.in_(
            db.query(models.Question.id).filter(models.Question.topic_id == topic_id)
        )
    ).all()
    
    # Create a dictionary of question_id -> progress for quick lookup
    progress_dict = {p.question_id: p for p in user_progress}
    
    # Get all questions for this topic
    all_questions = db.query(models.Question).filter(
        models.Question.topic_id == topic_id
    ).all()
    
    # Separate questions into learned and not learned
    learned_questions = []
    not_learned_questions = []
    
    for question in all_questions:
        progress = progress_dict.get(question.id)
        if progress and progress.is_learned:
            learned_questions.append(question)
        else:
            not_learned_questions.append(question)
    
    # Check if user has mastered all questions
    if len(learned_questions) == len(all_questions) and len(all_questions) > 0:
        print(f"Topic {topic_id} is mastered. Resetting progress for user {current_user.id}")
        
        # Reset all progress for this topic
        for progress in user_progress:
            progress.attempts = 0
            progress.correct_attempts = 0
            progress.is_learned = False
            progress.learning_score = 0.0
        db.commit()
        
        # Re-fetch questions after reset (now all questions are not learned)
        all_questions = db.query(models.Question).filter(
            models.Question.topic_id == topic_id
        ).all()
        
        # Select questions for the quiz (now all questions are available)
        selected_questions = random.sample(all_questions, min(target_quiz_size, len(all_questions)))
        
        # Shuffle the selected questions
        random.shuffle(selected_questions)
        
        # Build quiz questions
        quiz_questions = []
        lang = current_user.language if current_user.language else 'en'
        
        for question in selected_questions:
            question_text = getattr(question, f"question_{lang}")
            options = [
                getattr(question, f"option1_{lang}"),
                getattr(question, f"option2_{lang}"),
                getattr(question, f"option3_{lang}")
            ]
            
            quiz_questions.append(schemas.QuizQuestion(
                id=question.id,
                question=question_text,
                options=options,
                correct_option=question.correct_option
            ))
        
        return schemas.Quiz(questions=quiz_questions)
    
    # Select questions for the quiz
    selected_questions = []
    
    # First, try to fill with not learned questions
    if len(not_learned_questions) >= target_quiz_size:
        # Randomly select target_quiz_size questions from not learned
        selected_questions = random.sample(not_learned_questions, target_quiz_size)
    else:
        # Add all not learned questions
        selected_questions.extend(not_learned_questions)
        
        # If we still need more questions, add from learned questions
        # Prioritize recently incorrectly answered questions
        if len(selected_questions) < target_quiz_size:
            remaining_needed = target_quiz_size - len(selected_questions)
            
            # Sort learned questions by last_attempt (most recent first)
            learned_questions.sort(key=lambda q: progress_dict.get(q.id, models.UserProgress()).last_attempt or datetime.min, reverse=True)
            
            # Add the most recently attempted learned questions
            selected_questions.extend(learned_questions[:remaining_needed])
    
    # Shuffle the selected questions
    random.shuffle(selected_questions)
    
    # Build quiz questions
    quiz_questions = []
    lang = current_user.language if current_user.language else 'en'
    
    for question in selected_questions:
        question_text = getattr(question, f"question_{lang}")
        options = [
            getattr(question, f"option1_{lang}"),
            getattr(question, f"option2_{lang}"),
            getattr(question, f"option3_{lang}")
        ]
        
        quiz_questions.append(schemas.QuizQuestion(
            id=question.id,
            question=question_text,
            options=options,
            correct_option=question.correct_option
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
    
    # Check if user exists
    user = db.query(models.User).filter(models.User.id == permission.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if topic exists
    topic = db.query(models.Topic).filter(models.Topic.id == permission.topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    # Check if permission already exists and is active
    existing_permission = db.query(models.UserTopicPermission).filter(
        models.UserTopicPermission.user_id == permission.user_id,
        models.UserTopicPermission.topic_id == permission.topic_id,
        models.UserTopicPermission.is_active == True
    ).first()
    
    if existing_permission:
        raise HTTPException(status_code=400, detail="Permission already granted")
    
    # Check if there's an inactive permission and reactivate it
    inactive_permission = db.query(models.UserTopicPermission).filter(
        models.UserTopicPermission.user_id == permission.user_id,
        models.UserTopicPermission.topic_id == permission.topic_id,
        models.UserTopicPermission.is_active == False
    ).first()
    
    if inactive_permission:
        inactive_permission.is_active = True
        inactive_permission.granted_by = current_user.id
        db.commit()
        db.refresh(inactive_permission)
        return inactive_permission
    
    # Create new permission
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

@app.get("/admin/users", response_model=List[schemas.UserWithPermissions])
def get_users(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    if not auth.is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    
    users = db.query(models.User).all()
    
    # Add permissions for each user
    for user in users:
        permissions = db.query(models.UserTopicPermission).filter(
            models.UserTopicPermission.user_id == user.id,
            models.UserTopicPermission.is_active == True
        ).all()
        user.permissions = permissions
    
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

# Get current user permissions endpoint
@app.get("/users/me/permissions", response_model=List[schemas.UserTopicPermission])
def get_my_permissions(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    """Get permissions for the currently logged in user"""
    permissions = db.query(models.UserTopicPermission).filter(
        models.UserTopicPermission.user_id == current_user.id,
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
    print(f"Language update request - User ID: {current_user.id}, Current language: {current_user.language}, New language: {language.language}")
    
    if language.language not in ["en", "es"]:
        raise HTTPException(status_code=400, detail="Invalid language")
    
    # Get the user from the database session
    user = db.query(models.User).filter(models.User.id == current_user.id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    print(f"Before update - User language: {user.language}")
    user.language = language.language
    db.commit()
    db.refresh(user)
    print(f"After update - User language: {user.language}")
    
    return user

# Admin endpoints for topic management
@app.post("/admin/topics", response_model=schemas.Topic)
def create_topic_admin(
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

@app.delete("/admin/topics/{topic_id}")
def delete_topic(
    topic_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    if not auth.is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    
    # Check if topic exists
    topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    # Check if topic has questions
    questions = db.query(models.Question).filter(models.Question.topic_id == topic_id).first()
    if questions:
        raise HTTPException(status_code=400, detail="Cannot delete topic with existing questions")
    
    # Check if topic has permissions
    permissions = db.query(models.UserTopicPermission).filter(models.UserTopicPermission.topic_id == topic_id).first()
    if permissions:
        # Delete all permissions for this topic
        db.query(models.UserTopicPermission).filter(models.UserTopicPermission.topic_id == topic_id).delete()
    
    db.delete(topic)
    db.commit()
    return {"message": "Topic deleted successfully"}

@app.delete("/admin/topics/{topic_id}/force")
def force_delete_topic(
    topic_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    """Force delete a topic and all its questions (admin only)"""
    if not auth.is_admin(current_user):
        raise HTTPException(status_code=403, detail="Admin access required")
    
    topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    # Delete all questions associated with this topic
    db.query(models.Question).filter(models.Question.topic_id == topic_id).delete()
    
    # Delete all user permissions for this topic
    db.query(models.UserTopicPermission).filter(models.UserTopicPermission.topic_id == topic_id).delete()
    
    # Delete the topic
    db.delete(topic)
    db.commit()
    
    return {"message": "Topic and all associated questions deleted successfully"} 