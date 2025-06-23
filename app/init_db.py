from sqlalchemy.orm import Session
from sqlalchemy import text
from . import models, schemas, auth
from .database import engine, SessionLocal

def init_db():
    # Create all tables
    models.Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Delete all existing users except admin
        db.query(models.User).delete()
        db.commit()
        
        # Create admin user
        admin_password = "cdladmin"  # Change this in production
        hashed_password = auth.get_password_hash(admin_password)
        
        admin_user = models.User(
            name="Admin",
            lastname="User",
            email="admin@gmail.com",
            phone="+1234567890",
            hashed_password=hashed_password,
            is_admin=True,
            is_active=True,
            language="en"
        )
        
        db.add(admin_user)
        db.commit()
        
        print("Database initialized successfully!")
        print(f"Admin user created with email: admin@gmail.com")
        print(f"Admin password: {admin_password}")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db() 