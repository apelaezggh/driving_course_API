from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, DateTime, ForeignKey, text
from sqlalchemy.sql import func
from datetime import datetime
import os

# Database URL - use environment variables
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "driving_course")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

def migrate_add_user_sessions():
    engine = create_engine(DATABASE_URL)
    metadata = MetaData()
    
    # Create user_sessions table
    user_sessions = Table(
        'user_sessions',
        metadata,
        Column('id', Integer, primary_key=True, index=True),
        Column('user_id', Integer, ForeignKey('users.id')),
        Column('session_token', String, unique=True, index=True, nullable=False),
        Column('device_info', String, nullable=True),
        Column('ip_address', String, nullable=True),
        Column('user_agent', String, nullable=True),
        Column('is_active', Boolean, default=True),
        Column('created_at', DateTime, default=datetime.utcnow),
        Column('last_activity', DateTime, default=datetime.utcnow)
    )
    
    try:
        # Create the table
        user_sessions.create(engine, checkfirst=True)
        print("✅ User sessions table created successfully!")
        
        # Verify the table was created
        with engine.connect() as conn:
            result = conn.execute(text("SELECT COUNT(*) FROM user_sessions"))
            count = result.scalar()
            print(f"✅ User sessions table verified. Current records: {count}")
            
    except Exception as e:
        print(f"❌ Error creating user sessions table: {e}")
        raise

if __name__ == "__main__":
    migrate_add_user_sessions() 