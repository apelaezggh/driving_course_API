from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic

def update_quiz_sizes():
    db = SessionLocal()
    try:
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
            topic = db.query(Topic).filter(Topic.name_es == topic_name).first()
            if topic:
                topic.quiz_size = quiz_size
                print(f"Updated {topic_name} with quiz_size: {quiz_size}")
            else:
                print(f"Topic not found: {topic_name}")
        
        db.commit()
        print("Quiz sizes updated successfully!")
        
    except Exception as e:
        print(f"Error updating quiz sizes: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    update_quiz_sizes() 