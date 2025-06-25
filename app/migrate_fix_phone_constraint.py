from sqlalchemy import create_engine, MetaData, Table, Column, String, text
import os

# Database URL - use environment variables
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "driving_course")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

def migrate_fix_phone_constraint():
    engine = create_engine(DATABASE_URL)
    
    try:
        with engine.connect() as connection:
            # Drop the unique constraint on phone column
            connection.execute(text("ALTER TABLE users DROP CONSTRAINT IF EXISTS users_phone_key"))
            
            # Make phone column nullable
            connection.execute(text("ALTER TABLE users ALTER COLUMN phone DROP NOT NULL"))
            
            connection.commit()
            print("Successfully removed unique constraint from phone column and made it nullable")
            
    except Exception as e:
        print(f"Error during migration: {e}")
        raise

if __name__ == "__main__":
    migrate_fix_phone_constraint() 