from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
from datetime import datetime

# Association table for user roles
user_roles = Table(
    'user_roles',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('role_id', Integer, ForeignKey('roles.id'))
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)  # Removed unique constraint to allow multiple users with empty phone
    hashed_password = Column(String, nullable=False)
    google_id = Column(String, unique=True, nullable=True)  # Google OAuth ID
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    language = Column(String, default='en')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    roles = relationship("Role", secondary=user_roles, back_populates="users")
    progress = relationship("UserProgress", back_populates="user")
    topic_permissions = relationship(
        "UserTopicPermission",
        back_populates="user",
        foreign_keys="UserTopicPermission.user_id"
    )
    sessions = relationship("UserSession", back_populates="user")
    refresh_tokens = relationship("RefreshToken", back_populates="user")

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    users = relationship("User", secondary=user_roles, back_populates="roles")

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name_en = Column(String, index=True)
    name_es = Column(String, index=True)
    description_en = Column(String, default="")
    description_es = Column(String, default="")
    category = Column(String, default="basic")
    quiz_size = Column(Integer, default=10)  # Number of questions per quiz (actual)
    target_quiz_size = Column(Integer, default=10)  # Number of questions the quiz should have (target)
    questions = relationship("Question", back_populates="topic")
    user_permissions = relationship("UserTopicPermission", back_populates="topic")

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("topics.id"))
    question_en = Column(String)
    question_es = Column(String)
    option1_en = Column(String)
    option1_es = Column(String)
    option2_en = Column(String)
    option2_es = Column(String)
    option3_en = Column(String)
    option3_es = Column(String)
    correct_option = Column(Integer)  # 1, 2, or 3
    topic = relationship("Topic", back_populates="questions")
    progress = relationship("UserProgress", back_populates="question")

class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    attempts = Column(Integer, default=0)
    correct_attempts = Column(Integer, default=0)
    last_attempt = Column(DateTime(timezone=True), server_default=func.now())
    is_learned = Column(Boolean, default=False)
    learning_score = Column(Float, default=0.0)  # Score from 0 to 1
    user = relationship("User", back_populates="progress")
    question = relationship("Question", back_populates="progress")

class UserTopicPermission(Base):
    __tablename__ = "user_topic_permissions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    topic_id = Column(Integer, ForeignKey("topics.id"))
    granted_by = Column(Integer, ForeignKey("users.id"))  # Admin who granted the permission
    granted_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)
    
    user = relationship("User", foreign_keys=[user_id], back_populates="topic_permissions")
    topic = relationship("Topic", back_populates="user_permissions")
    granted_by_user = relationship("User", foreign_keys=[granted_by])

class UserSession(Base):
    __tablename__ = "user_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    session_token = Column(String, unique=True, index=True, nullable=False)
    device_info = Column(String, nullable=True)  # Información del dispositivo
    ip_address = Column(String, nullable=True)   # Dirección IP
    user_agent = Column(String, nullable=True)   # User agent del navegador
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_activity = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="sessions")

class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    token = Column(String, unique=True, index=True, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    is_revoked = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    device_info = Column(String, nullable=True)
    ip_address = Column(String, nullable=True)
    user_agent = Column(String, nullable=True)
    
    user = relationship("User", back_populates="refresh_tokens") 