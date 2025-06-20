from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    language: str
    created_at: datetime

    class Config:
        from_attributes = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Topic schemas
class TopicBase(BaseModel):
    name_en: str
    name_es: str
    description_en: str
    description_es: str

class TopicCreate(TopicBase):
    pass

class Topic(TopicBase):
    id: int
    has_permission: Optional[bool] = None

    class Config:
        from_attributes = True

# User Topic Permission schemas
class UserTopicPermissionBase(BaseModel):
    user_id: int
    topic_id: int
    is_active: bool

class UserTopicPermissionCreate(UserTopicPermissionBase):
    pass

class UserTopicPermission(UserTopicPermissionBase):
    id: int
    granted_by: int
    granted_at: datetime

    class Config:
        from_attributes = True

# Question schemas
class QuestionBase(BaseModel):
    question_en: str
    question_es: str
    option1_en: str
    option1_es: str
    option2_en: str
    option2_es: str
    option3_en: str
    option3_es: str
    correct_option: int

class QuestionCreate(QuestionBase):
    topic_id: int

class Question(QuestionBase):
    id: int
    topic_id: int

    class Config:
        from_attributes = True

# Progress schemas
class UserProgressBase(BaseModel):
    attempts: int
    correct_attempts: int
    is_learned: bool
    learning_score: float

class UserProgressCreate(UserProgressBase):
    user_id: int
    question_id: int

class UserProgress(UserProgressBase):
    id: int
    user_id: int
    question_id: int
    last_attempt: datetime

    class Config:
        from_attributes = True

# Quiz schemas
class QuizQuestion(BaseModel):
    id: int
    question: str
    options: List[str]

class Quiz(BaseModel):
    questions: List[QuizQuestion]

# Language preference
class LanguagePreference(BaseModel):
    language: str

# Admin schemas
class GrantPermission(BaseModel):
    user_id: int
    topic_id: int

class RevokePermission(BaseModel):
    user_id: int
    topic_id: int 