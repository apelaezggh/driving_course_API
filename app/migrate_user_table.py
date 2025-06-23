from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from .database import SQLALCHEMY_DATABASE_URL
from . import models
from . import auth

def migrate_user_table():
    # Create engine
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    
    # Create session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        print("Starting user table migration...")
        
        # Check if the new columns exist
        result = db.execute(text("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = 'users' 
            AND column_name IN ('name', 'lastname', 'phone', 'is_admin', 'updated_at')
        """))
        existing_columns = [row[0] for row in result.fetchall()]
        
        # Add new columns if they don't exist
        if 'name' not in existing_columns:
            print("Adding 'name' column...")
            db.execute(text("ALTER TABLE users ADD COLUMN name VARCHAR"))
        
        if 'lastname' not in existing_columns:
            print("Adding 'lastname' column...")
            db.execute(text("ALTER TABLE users ADD COLUMN lastname VARCHAR"))
        
        if 'phone' not in existing_columns:
            print("Adding 'phone' column...")
            db.execute(text("ALTER TABLE users ADD COLUMN phone VARCHAR"))
        
        if 'is_admin' not in existing_columns:
            print("Adding 'is_admin' column...")
            db.execute(text("ALTER TABLE users ADD COLUMN is_admin BOOLEAN DEFAULT FALSE"))
        
        if 'updated_at' not in existing_columns:
            print("Adding 'updated_at' column...")
            db.execute(text("ALTER TABLE users ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"))
        
        # Check if username column exists
        result = db.execute(text("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = 'users' 
            AND column_name = 'username'
        """))
        
        if result.fetchone():
            print("Removing 'username' column...")
            # First, drop any foreign key constraints that reference username
            db.execute(text("""
                DO $$ 
                BEGIN
                    IF EXISTS (
                        SELECT 1 FROM information_schema.table_constraints 
                        WHERE constraint_name LIKE '%username%' 
                        AND table_name = 'users'
                    ) THEN
                        ALTER TABLE users DROP CONSTRAINT IF EXISTS users_username_key;
                    END IF;
                END $$;
            """))
            db.execute(text("ALTER TABLE users DROP COLUMN IF EXISTS username"))
        
        # Update existing admin user
        print("Updating admin user...")
        admin_user = db.execute(text("SELECT id FROM users WHERE email = 'admin@drivingcourse.com'")).fetchone()
        
        if admin_user:
            db.execute(text("""
                UPDATE users 
                SET name = 'Admin', 
                    lastname = 'User', 
                    phone = '+1234567890', 
                    is_admin = TRUE, 
                    language = 'en',
                    updated_at = CURRENT_TIMESTAMP
                WHERE email = 'admin@drivingcourse.com'
            """))
        else:
            # Create admin user if it doesn't exist
            print("Creating admin user...")
            admin_password = "admin123"
            hashed_password = auth.get_password_hash(admin_password)
            
            db.execute(text("""
                INSERT INTO users (name, lastname, email, phone, hashed_password, is_admin, is_active, language, created_at, updated_at)
                VALUES ('Admin', 'User', 'admin@drivingcourse.com', '+1234567890', :hashed_password, TRUE, TRUE, 'en', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            """), {"hashed_password": hashed_password})
        
        # Delete user_roles for users that are not admin
        print("Deleting user_roles for non-admin users...")
        db.execute(text("DELETE FROM user_roles WHERE user_id IN (SELECT id FROM users WHERE email != 'admin@drivingcourse.com')"))
        
        # Delete all other users except admin
        print("Deleting all users except admin...")
        db.execute(text("DELETE FROM users WHERE email != 'admin@drivingcourse.com'"))
        
        # Commit changes
        db.commit()
        print("Migration completed successfully!")
        
        # Show final table structure
        result = db.execute(text("""
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns 
            WHERE table_name = 'users' 
            ORDER BY ordinal_position
        """))
        
        print("\nFinal table structure:")
        for row in result.fetchall():
            print(f"  {row[0]}: {row[1]} ({'NULL' if row[2] == 'YES' else 'NOT NULL'})")
        
    except Exception as e:
        print(f"Error during migration: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    migrate_user_table() 