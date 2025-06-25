import os
from typing import Optional
from google.oauth2 import id_token
from google.auth.transport import requests
from sqlalchemy.orm import Session
from . import models, auth
from .database import get_db

# Google OAuth configuration
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "your-google-client-id")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "your-google-client-secret")

def verify_google_token(token: str) -> Optional[dict]:
    """
    Verify Google ID token and return user info
    """
    try:
        # Verify the token
        idinfo = id_token.verify_oauth2_token(
            token, 
            requests.Request(), 
            GOOGLE_CLIENT_ID
        )
        
        # ID token is valid. Get the user's Google Account ID and profile info
        userid = idinfo['sub']
        email = idinfo['email']
        name = idinfo.get('given_name', '')
        lastname = idinfo.get('family_name', '')
        picture = idinfo.get('picture', '')
        
        return {
            'google_id': userid,
            'email': email,
            'name': name,
            'lastname': lastname,
            'picture': picture
        }
    except Exception as e:
        print(f"Error verifying Google token: {e}")
        return None

def get_or_create_google_user(google_user_info: dict, db: Session) -> Optional[models.User]:
    """
    Get existing user or create new user from Google info
    """
    try:
        # Check if user exists by email
        user = db.query(models.User).filter(models.User.email == google_user_info['email']).first()
        
        if user:
            # User exists, update Google ID if not set
            if not user.google_id:
                user.google_id = google_user_info['google_id']
                db.commit()
            return user
        
        # Create new user
        new_user = models.User(
            name=google_user_info['name'],
            lastname=google_user_info['lastname'],
            email=google_user_info['email'],
            phone="",  # Google doesn't provide phone
            hashed_password="",  # No password for Google users
            is_admin=False,
            is_active=True,
            language="en",
            google_id=google_user_info['google_id']
        )
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return new_user
        
    except Exception as e:
        print(f"Error creating/getting Google user: {e}")
        db.rollback()
        return None 