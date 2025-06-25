from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_tank_block2():
    db = SessionLocal()
    try:
        topic = db.query(Topic).filter(Topic.id == 17).first()
        if not topic:
            print("Topic ID 17 (Cisterna) not found!")
            return
        print(f"Found topic: {topic.name_es} (ID: {topic.id})")
        questions_data = [
            {"question_en": "What class of CDL permit is required to drive a tank vehicle?", "question_es": "¿Qué clase de permiso CDL se requiere para conducir una cisterna?", "option1_en": "Class D", "option1_es": "Clase D", "option2_en": "Class B with N endorsement", "option2_es": "Clase B con endoso N", "option3_en": "Only HazMat", "option3_es": "Solo HazMat", "correct_option": 2},
            {"question_en": "When is it mandatory to have the N (Tank Vehicle) endorsement?", "question_es": "¿Cuándo es obligatorio tener el endoso N (Tank Vehicle)?", "option1_en": "Only if the liquid is toxic", "option1_es": "Solo si el líquido es tóxico", "option2_en": "When transporting liquids or gases in containers of 1,000 gallons or more", "option2_es": "Cuando se transportan líquidos o gases en contenedores de 1,000 galones o más", "option3_en": "Only if there are multiple compartments", "option3_es": "Solo si hay múltiples compartimentos", "correct_option": 2},
            {"question_en": "What can cause a spill in a poorly sealed tank?", "question_es": "¿Qué puede causar un derrame en una cisterna mal sellada?", "option1_en": "Heat", "option1_es": "El calor", "option2_en": "Evaporation", "option2_es": "La evaporación", "option3_en": "Expansion of liquid with temperature changes", "option3_es": "La expansión del líquido con cambios de temperatura", "correct_option": 3},
            {"question_en": "How can the slope of the terrain affect liquid transport?", "question_es": "¿Cómo puede afectar la pendiente del terreno al transportar líquidos?", "option1_en": "Increases fuel level", "option1_es": "Aumenta el nivel de combustible", "option2_en": "Changes the vehicle's center of gravity", "option2_es": "Cambia el centro de gravedad del vehículo", "option3_en": "Reduces liquid pressure", "option3_es": "Reduce la presión del líquido", "correct_option": 2},
            {"question_en": "Why does it take longer to brake a tank than a dry truck?", "question_es": "¿Por qué se requiere más tiempo para frenar una cisterna que un camión seco?", "option1_en": "Due to additional weight", "option1_es": "Por el peso adicional", "option2_en": "Due to power steering", "option2_es": "Por la dirección asistida", "option3_en": "Due to the movement of the liquid pushing forward", "option3_es": "Por el movimiento del líquido que empuja hacia adelante", "correct_option": 3},
            {"question_en": "What special precaution should be taken when driving an empty tank?", "question_es": "¿Qué precaución especial se debe tener al conducir una cisterna vacía?", "option1_en": "None", "option1_es": "Ninguna", "option2_en": "It can slide more easily because it weighs less", "option2_es": "Puede deslizarse más fácilmente porque pesa menos", "option3_en": "It can tip over less", "option3_es": "Puede volcarse menos", "correct_option": 2},
            {"question_en": "What should the driver do when loading a tank with several compartments?", "question_es": "¿Qué debe hacer el conductor al cargar una cisterna con varios compartimentos?", "option1_en": "Fill only one", "option1_es": "Llenar solo uno", "option2_en": "Balance the weight in all compartments", "option2_es": "Equilibrar el peso en todos los compartimentos", "option3_en": "Fill from back to front", "option3_es": "Llenar de atrás hacia adelante", "correct_option": 2},
            {"question_en": "What does a 'tank without baffles' mean?", "question_es": "¿Qué significa un tanque 'sin baffles'?", "option1_en": "Faster to fill", "option1_es": "Más rápido de llenar", "option2_en": "It has no compartments to reduce surge, requires more careful driving", "option2_es": "No tiene compartimentos que reduzcan el oleaje, requiere manejo más cuidadoso", "option3_en": "It has no valves", "option3_es": "No tiene válvulas", "correct_option": 2},
            {"question_en": "What should you do if a tank valve drips slightly?", "question_es": "¿Qué debe hacer si una válvula del tanque gotea ligeramente?", "option1_en": "Ignore it", "option1_es": "Ignorarla", "option2_en": "Cover it with a rag", "option2_es": "Taparla con trapo", "option3_en": "Report and repair before driving", "option3_es": "Reportar y reparar antes de conducir", "correct_option": 3},
            {"question_en": "What is 'lateral surge' in a tank?", "question_es": "¿Qué es el 'oleaje lateral' en una cisterna?", "option1_en": "Forward movement of liquid", "option1_es": "Movimiento hacia adelante del líquido", "option2_en": "Side-to-side movement that can cause rollover", "option2_es": "Movimiento de lado a lado, que puede causar vuelco", "option3_en": "Engine vibration", "option3_es": "Vibración del motor", "correct_option": 2}
        ]
        added_count = 0
        for q_data in questions_data:
            existing_question = db.query(Question).filter(Question.question_en == q_data["question_en"], Question.topic_id == topic.id).first()
            if not existing_question:
                question = Question(topic_id=topic.id, **q_data)
                db.add(question)
                added_count += 1
                print(f"Added question: {q_data['question_en']}")
            else:
                print(f"Question already exists: {q_data['question_en']}")
        db.commit()
        print(f"\nSuccessfully added {added_count} new questions to 'Cisterna' (Block 2)")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_tank_block2() 