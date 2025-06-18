from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

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
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    language = Column(String, default="es")  # Default language
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    roles = relationship("Role", secondary=user_roles, back_populates="users")
    progress = relationship("UserProgress", back_populates="user")

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
    description_en = Column(String)
    description_es = Column(String)
    questions = relationship("Question", back_populates="topic")

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