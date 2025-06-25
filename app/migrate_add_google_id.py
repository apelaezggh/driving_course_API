from sqlalchemy import text
from .database import engine

def migrate_add_google_id():
    with engine.connect() as connection:
        try:
            # Add google_id column if it doesn't exist
            connection.execute(text("""
                ALTER TABLE users 
                ADD COLUMN IF NOT EXISTS google_id VARCHAR UNIQUE
            """))
            
            # Make phone and hashed_password nullable for Google users
            connection.execute(text("""
                ALTER TABLE users 
                ALTER COLUMN phone DROP NOT NULL
            """))
            
            connection.execute(text("""
                ALTER TABLE users 
                ALTER COLUMN hashed_password DROP NOT NULL
            """))
            
            connection.commit()
            print("Migration completed: Added google_id column and made phone/password nullable")
            
        except Exception as e:
            print(f"Migration error: {e}")
            connection.rollback()

if __name__ == "__main__":
    migrate_add_google_id() 