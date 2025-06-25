from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_air_brakes_questions_block1():
    db = SessionLocal()
    try:
        topic = db.query(Topic).filter(Topic.name_es == "Frenos de Aire").first()
        if not topic:
            print("Topic 'Frenos de Aire' not found!")
            return
        print(f"Found topic: {topic.name_es} (ID: {topic.id})")
        questions_data = [
            {"question_en": "What is the typical working pressure range in an air brake system?", "question_es": "¿Cuál es el rango típico de presión de trabajo en un sistema de frenos de aire?", "option1_en": "50-75 psi", "option1_es": "50-75 psi", "option2_en": "100-125 psi", "option2_es": "100-125 psi", "option3_en": "150-200 psi", "option3_es": "150-200 psi", "correct_option": 2},
            {"question_en": "What part of the air brake system is used to release spring brakes?", "question_es": "¿Qué parte del sistema de frenos de aire se utiliza para liberar los frenos de resorte?", "option1_en": "Compressor", "option1_es": "Compresor", "option2_en": "Control valve", "option2_es": "Válvula de control", "option3_en": "Air pressure", "option3_es": "Presión de aire", "correct_option": 3},
            {"question_en": "What happens if the air system pressure drops too low?", "question_es": "¿Qué sucede si la presión del sistema de aire baja demasiado?", "option1_en": "The vehicle accelerates", "option1_es": "El vehículo se acelera", "option2_en": "The emergency brake activates automatically", "option2_es": "El freno de emergencia se activa automáticamente", "option3_en": "The horn turns on", "option3_es": "El claxon se enciende", "correct_option": 2},
            {"question_en": "What is the purpose of the air compressor?", "question_es": "¿Cuál es el propósito del compresor de aire?", "option1_en": "Cool the engine", "option1_es": "Refrigerar el motor", "option2_en": "Charge the air brake system", "option2_es": "Cargar el sistema de frenos de aire", "option3_en": "Turn on the lights", "option3_es": "Encender las luces", "correct_option": 2},
            {"question_en": "What is the brake called that activates automatically if there is air pressure loss?", "question_es": "¿Cómo se llama el freno que se activa automáticamente si hay pérdida de presión de aire?", "option1_en": "Service brake", "option1_es": "Freno de servicio", "option2_en": "Emergency brake", "option2_es": "Freno de emergencia", "option3_en": "Parking brake", "option3_es": "Freno de estacionamiento", "correct_option": 2},
            {"question_en": "What is the purpose of the air dryer in an air brake system?", "question_es": "¿Cuál es el propósito del secador de aire en un sistema de frenos?", "option1_en": "Increase pressure", "option1_es": "Aumentar la presión", "option2_en": "Cool the air", "option2_es": "Enfriar el aire", "option3_en": "Remove moisture and contaminants", "option3_es": "Eliminar humedad y contaminantes", "correct_option": 3},
            {"question_en": "What should be done before checking spring brakes?", "question_es": "¿Qué se debe hacer antes de revisar los frenos de resorte?", "option1_en": "Remove air from the system", "option1_es": "Quitar el aire del sistema", "option2_en": "Start the engine", "option2_es": "Encender el motor", "option3_en": "Uncouple the trailer", "option3_es": "Desacoplar el remolque", "correct_option": 1},
            {"question_en": "When is the parking brake released in vehicles with air brakes?", "question_es": "¿Cuándo se libera el freno de estacionamiento en vehículos con frenos de aire?", "option1_en": "When the hand brake lever is activated", "option1_es": "Cuando se acciona la palanca de freno de mano", "option2_en": "When air pressure is applied to the brake", "option2_es": "Cuando se aplica presión de aire al freno", "option3_en": "When the vehicle is turned off", "option3_es": "Cuando el vehículo se apaga", "correct_option": 2},
            {"question_en": "What is a dual service control valve?", "question_es": "¿Qué es una válvula de control de doble servicio?", "option1_en": "A valve to adjust suspension", "option1_es": "Una válvula para ajustar la suspensión", "option2_en": "A valve that controls emergency and service brakes", "option2_es": "Una válvula que controla el freno de emergencia y servicio", "option3_en": "A valve for the fuel tank", "option3_es": "Una válvula para el tanque de combustible", "correct_option": 2},
            {"question_en": "What does a red low air pressure warning light indicate?", "question_es": "¿Qué indica una luz de advertencia roja de baja presión de aire?", "option1_en": "That the engine needs oil", "option1_es": "Que el motor necesita aceite", "option2_en": "That ABS brakes are active", "option2_es": "Que los frenos ABS están activos", "option3_en": "That air pressure is dangerously low", "option3_es": "Que la presión de aire es peligrosamente baja", "correct_option": 3},
            {"question_en": "How often should the air tank be manually drained?", "question_es": "¿Cada cuánto tiempo se debe drenar manualmente el tanque de aire?", "option1_en": "Once a week", "option1_es": "Una vez por semana", "option2_en": "After each trip", "option2_es": "Después de cada viaje", "option3_en": "Daily", "option3_es": "Diariamente", "correct_option": 3},
            {"question_en": "What causes air brakes to fade or fail?", "question_es": "¿Qué causa que los frenos de aire se desvanezcan o fallen?", "option1_en": "Low pressure", "option1_es": "Baja presión", "option2_en": "Excessive use and overheating", "option2_es": "Uso excesivo y calentamiento", "option3_en": "Too much brake fluid", "option3_es": "Demasiado líquido de frenos", "correct_option": 2},
            {"question_en": "Which tank fills first in an air brake system?", "question_es": "¿Qué tanque se llena primero en un sistema de frenos de aire?", "option1_en": "Primary tank", "option1_es": "Tanque primario", "option2_en": "Emergency tank", "option2_es": "Tanque de emergencia", "option3_en": "Service system tank", "option3_es": "Tanque del sistema de servicio", "correct_option": 3},
            {"question_en": "What is the 'spring brake'?", "question_es": "¿Qué es el 'freno de resorte'?", "option1_en": "Brake used to maintain speed", "option1_es": "Freno usado para mantener la velocidad", "option2_en": "Emergency or parking brake activated by springs", "option2_es": "Freno de emergencia o estacionamiento activado por resortes", "option3_en": "Brake that activates with electricity", "option3_es": "Freno que se activa con electricidad", "correct_option": 2},
            {"question_en": "How is an air brake system leak verified?", "question_es": "¿Cómo se verifica una fuga del sistema de frenos de aire?", "option1_en": "By listening to the engine", "option1_es": "Escuchando el motor", "option2_en": "By applying the service brake and observing pressure drop", "option2_es": "Aplicando el freno de servicio y observando la caída de presión", "option3_en": "By turning on the lights", "option3_es": "Encendiendo las luces", "correct_option": 2}
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
        print(f"\nSuccessfully added {added_count} new questions to 'Frenos de Aire' (Block 1)")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_air_brakes_questions_block1() 