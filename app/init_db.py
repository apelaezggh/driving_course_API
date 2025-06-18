from sqlalchemy.orm import Session
from . import models, auth
from .database import SessionLocal

def init_db():
    db = SessionLocal()
    try:
        # Create admin role if it doesn't exist
        admin_role = db.query(models.Role).filter(models.Role.name == "admin").first()
        if not admin_role:
            admin_role = models.Role(name="admin")
            db.add(admin_role)
            db.commit()

        # Create admin user if it doesn't exist
        admin_user = db.query(models.User).filter(models.User.username == "admin").first()
        if not admin_user:
            admin_user = models.User(
                email="admin@example.com",
                username="admin",
                hashed_password=auth.get_password_hash("admin123"),
                is_active=True
            )
            admin_user.roles.append(admin_role)
            db.add(admin_user)
            db.commit()
            print("Admin user created successfully!")
        else:
            print("Admin user already exists.")

    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db() 