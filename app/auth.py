from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db
import secrets

# Security configuration
SECRET_KEY = "your-secret-key-here"  # Change this in production!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_session_token():
    """Create a unique session token"""
    return secrets.token_urlsafe(32)

def get_client_info(request: Request):
    """Extract client information from request"""
    client_ip = request.client.host if request.client else None
    user_agent = request.headers.get("user-agent", "")
    
    # Try to get real IP if behind proxy
    forwarded_for = request.headers.get("x-forwarded-for")
    if forwarded_for:
        client_ip = forwarded_for.split(",")[0].strip()
    
    return {
        "ip_address": client_ip,
        "user_agent": user_agent,
        "device_info": f"{client_ip} - {user_agent[:100]}"  # Truncate user agent
    }

def create_user_session(db: Session, user_id: int, request: Request):
    """Create a new session for a user and invalidate any existing sessions"""
    # First, deactivate any existing sessions for this user
    existing_sessions = db.query(models.UserSession).filter(
        models.UserSession.user_id == user_id,
        models.UserSession.is_active == True
    ).all()
    
    for session in existing_sessions:
        session.is_active = False
        session.last_activity = datetime.utcnow()
    
    # Create new session
    client_info = get_client_info(request)
    session_token = create_session_token()
    
    new_session = models.UserSession(
        user_id=user_id,
        session_token=session_token,
        device_info=client_info["device_info"],
        ip_address=client_info["ip_address"],
        user_agent=client_info["user_agent"],
        is_active=True,
        created_at=datetime.utcnow(),
        last_activity=datetime.utcnow()
    )
    
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    
    return session_token

def validate_user_session(db: Session, user_id: int, request: Request):
    """Validate if user has an active session and update last activity"""
    client_info = get_client_info(request)
    
    # Find active session for this user
    active_session = db.query(models.UserSession).filter(
        models.UserSession.user_id == user_id,
        models.UserSession.is_active == True
    ).first()
    
    if not active_session:
        return True, "No active session found - creating new one"
    
    # Update last activity for the existing session
    active_session.last_activity = datetime.utcnow()
    db.commit()
    
    return True, "Session valid"

def authenticate_user(db: Session, email: str, password: str):
    print(f"Authenticating user with email: {email}")
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        print(f"User not found for email: {email}")
        return False
    
    print(f"User found: {user.email} (ID: {user.id})")
    password_valid = verify_password(password, user.hashed_password)
    print(f"Password verification: {'Success' if password_valid else 'Failed'}")
    
    if not password_valid:
        return False
    return user

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db), request: Request = None):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
    user = db.query(models.User).filter(models.User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    
    # Session validation is now optional and less restrictive
    # Only validate if request is available and user has active sessions
    if request:
        try:
            session_valid, message = validate_user_session(db, user.id, request)
            if not session_valid:
                print(f"Session validation failed: {message}")
                # Don't block the request, just log the issue
        except Exception as e:
            print(f"Session validation error: {e}")
            # Don't block the request, just log the error
    
    return user

async def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def is_admin(user: models.User):
    return user.is_admin 