from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

# Temas y cantidad de preguntas
TOPICS = [
    {
        "name_es": "Operación de Vehículos Comerciales de Texas",
        "name_en": "Texas Commercial Vehicle Operation",
        "description_es": "Examen obligatorio sobre operación de vehículos comerciales en Texas.",
        "description_en": "Mandatory exam about commercial vehicle operation in Texas.",
        "num_questions": 20,
    },
    {
        "name_es": "Conocimientos Generales",
        "name_en": "General Knowledge",
        "description_es": "Examen de conocimientos generales.",
        "description_en": "General knowledge exam.",
        "num_questions": 50,
    },
    {
        "name_es": "Frenos de Aire",
        "name_en": "Air Brakes",
        "description_es": "Examen sobre frenos de aire.",
        "description_en": "Air brakes exam.",
        "num_questions": 25,
    },
    {
        "name_es": "Vehículos Combinados",
        "name_en": "Combined Vehicles",
        "description_es": "Examen sobre vehículos combinados.",
        "description_en": "Combined vehicles exam.",
        "num_questions": 20,
    },
    {
        "name_es": "Materiales Peligrosos",
        "name_en": "Hazardous Materials",
        "description_es": "Examen sobre materiales peligrosos.",
        "description_en": "Hazardous materials exam.",
        "num_questions": 30,
    },
    {
        "name_es": "Cisterna",
        "name_en": "Tanker",
        "description_es": "Examen sobre cisternas.",
        "description_en": "Tanker exam.",
        "num_questions": 20,
    },
    {
        "name_es": "Dobles o Triples",
        "name_en": "Doubles or Triples",
        "description_es": "Examen sobre dobles o triples.",
        "description_en": "Doubles or triples exam.",
        "num_questions": 20,
    },
    {
        "name_es": "Pasajeros",
        "name_en": "Passengers",
        "description_es": "Examen sobre transporte de pasajeros.",
        "description_en": "Passengers exam.",
        "num_questions": 20,
    },
    {
        "name_es": "Autobús Escolar",
        "name_en": "School Bus",
        "description_es": "Examen sobre autobús escolar.",
        "description_en": "School bus exam.",
        "num_questions": 20,
    },
]

def seed():
    db: Session = SessionLocal()
    try:
        for topic_data in TOPICS:
            # Crear tema si no existe
            topic = db.query(models.Topic).filter_by(name_es=topic_data["name_es"]).first()
            if not topic:
                topic = models.Topic(
                    name_es=topic_data["name_es"],
                    name_en=topic_data["name_en"],
                    description_es=topic_data["description_es"],
                    description_en=topic_data["description_en"]
                )
                db.add(topic)
                db.commit()
                db.refresh(topic)
            # Crear preguntas de ejemplo
            existing_questions = db.query(models.Question).filter_by(topic_id=topic.id).count()
            for i in range(existing_questions + 1, topic_data["num_questions"] + 1):
                q = models.Question(
                    topic_id=topic.id,
                    question_es=f"Pregunta de ejemplo {i} para {topic.name_es}",
                    question_en=f"Sample question {i} for {topic.name_en}",
                    option1_es=f"Opción 1 de ejemplo {i}",
                    option1_en=f"Sample option 1 for question {i}",
                    option2_es=f"Opción 2 de ejemplo {i}",
                    option2_en=f"Sample option 2 for question {i}",
                    option3_es=f"Opción 3 de ejemplo {i}",
                    option3_en=f"Sample option 3 for question {i}",
                    correct_option=1
                )
                db.add(q)
            db.commit()
        print("Temas y preguntas de ejemplo creados correctamente.")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed() 