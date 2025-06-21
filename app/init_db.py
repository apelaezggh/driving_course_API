from sqlalchemy.orm import Session
from sqlalchemy import text
from . import models, schemas, auth
from .database import engine, SessionLocal

def init_db():
    db = SessionLocal()
    
    # Create admin role if it doesn't exist
    admin_role = db.query(models.Role).filter(models.Role.name == "admin").first()
    if not admin_role:
        admin_role = models.Role(name="admin")
        db.add(admin_role)
        db.commit()
        db.refresh(admin_role)
    
    # Create user role if it doesn't exist
    user_role = db.query(models.Role).filter(models.Role.name == "user").first()
    if not user_role:
        user_role = models.Role(name="user")
        db.add(user_role)
        db.commit()
        db.refresh(user_role)
    
    # Create admin user if it doesn't exist
    admin_user = db.query(models.User).filter(models.User.username == "admin").first()
    if not admin_user:
        hashed_password = auth.get_password_hash("admin123")
        admin_user = models.User(
            email="admin@example.com",
            username="admin",
            hashed_password=hashed_password
        )
        admin_user.roles.append(admin_role)
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
    
    # Add category field to existing topics if it doesn't exist
    try:
        # This will add the category column if it doesn't exist
        db.execute(text("ALTER TABLE topics ADD COLUMN IF NOT EXISTS category VARCHAR DEFAULT 'basic'"))
        db.execute(text("ALTER TABLE topics ALTER COLUMN description_en SET DEFAULT ''"))
        db.execute(text("ALTER TABLE topics ALTER COLUMN description_es SET DEFAULT ''"))
        db.commit()
    except Exception as e:
        print(f"Error updating topics table: {e}")
        db.rollback()
    
    # Create sample topics if they don't exist
    topics_data = [
        {
            "name_en": "Basic Traffic Rules",
            "name_es": "Reglas Básicas de Tráfico",
            "description_en": "Fundamental traffic rules and regulations",
            "description_es": "Reglas y regulaciones fundamentales de tráfico",
            "category": "basic"
        },
        {
            "name_en": "Road Signs",
            "name_es": "Señales de Tráfico",
            "description_en": "Understanding road signs and their meanings",
            "description_es": "Comprensión de señales de tráfico y sus significados",
            "category": "basic"
        },
        {
            "name_en": "Motorcycle Endorsement",
            "name_es": "Endoso de Motocicleta",
            "description_en": "Special rules and requirements for motorcycle operation",
            "description_es": "Reglas especiales y requisitos para operación de motocicletas",
            "category": "endorsement"
        }
    ]
    
    for topic_data in topics_data:
        existing_topic = db.query(models.Topic).filter(
            models.Topic.name_en == topic_data["name_en"]
        ).first()
        
        if not existing_topic:
            topic = models.Topic(**topic_data)
            db.add(topic)
    
    db.commit()
    db.close()

if __name__ == "__main__":
    init_db() 