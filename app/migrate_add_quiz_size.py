from sqlalchemy import text
from .database import engine

def add_quiz_size_column():
    with engine.connect() as connection:
        try:
            # Add quiz_size column to topics table
            connection.execute(text("""
                ALTER TABLE topics 
                ADD COLUMN quiz_size INTEGER DEFAULT 10
            """))
            connection.commit()
            print("Successfully added quiz_size column to topics table")
            
            # Update existing topics with their quiz_size values
            topic_updates = {
                "Operación de Vehículos Comerciales de Texas": 20,
                "Conocimientos Generales": 50,
                "Frenos de Aire": 25,
                "Vehículos Combinados": 20,
                "Materiales Peligrosos": 30,
                "Cisterna": 20,
                "Dobles o Triples": 20,
                "Pasajeros": 20,
                "Autobús Escolar": 20
            }
            
            for topic_name, quiz_size in topic_updates.items():
                result = connection.execute(text("""
                    UPDATE topics 
                    SET quiz_size = :quiz_size 
                    WHERE name_es = :topic_name
                """), {"quiz_size": quiz_size, "topic_name": topic_name})
                
                if result.rowcount > 0:
                    print(f"Updated {topic_name} with quiz_size: {quiz_size}")
                else:
                    print(f"Topic not found: {topic_name}")
            
            connection.commit()
            print("Quiz sizes updated successfully!")
            
        except Exception as e:
            print(f"Error during migration: {e}")
            connection.rollback()

if __name__ == "__main__":
    add_quiz_size_column() 