from sqlalchemy.orm import Session
from app import models, auth
from app.database import SessionLocal

def init_db():
    db = SessionLocal()
    try:
        # Crear rol admin si no existe
        admin_role = db.query(models.Role).filter(models.Role.name == "admin").first()
        if not admin_role:
            admin_role = models.Role(name="admin")
            db.add(admin_role)
            db.commit()

        # Crear usuario admin si no existe
        admin_user = db.query(models.User).filter(models.User.username == "admin").first()
        if not admin_user:
            admin_user = models.User(
                email="admin@example.com",
                username="admin",
                hashed_password=auth.get_password_hash("cdladmin"),
                is_active=True
            )
            admin_user.roles.append(admin_role)
            db.add(admin_user)
            db.commit()
            print("Usuario admin creado correctamente!")
        else:
            print("El usuario admin ya existe.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db() 