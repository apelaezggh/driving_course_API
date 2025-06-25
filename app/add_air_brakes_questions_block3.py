from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_air_brakes_questions_block3():
    db = SessionLocal()
    try:
        topic = db.query(Topic).filter(Topic.name_es == "Frenos de Aire").first()
        if not topic:
            print("Topic 'Frenos de Aire' not found!")
            return
        print(f"Found topic: {topic.name_es} (ID: {topic.id})")
        questions_data = [
            {"question_en": "What does it indicate if the low air pressure warning light stays on after starting the engine?", "question_es": "¿Qué indica si la luz de advertencia de baja presión de aire permanece encendida después de arrancar el motor?", "option1_en": "That the ABS system is active", "option1_es": "Que el sistema ABS está activo", "option2_en": "That the brake system has not yet reached safe pressure", "option2_es": "Que el sistema de frenos aún no ha alcanzado presión segura", "option3_en": "That the brakes are in good condition", "option3_es": "Que los frenos están en buenas condiciones", "correct_option": 2},
            {"question_en": "At what pressure should the compressor cut off in most air brake systems?", "question_es": "¿A qué presión debe cortarse el compresor en la mayoría de los sistemas de frenos de aire?", "option1_en": "100 psi", "option1_es": "100 psi", "option2_en": "125 psi", "option2_es": "125 psi", "option3_en": "150 psi", "option3_es": "150 psi", "correct_option": 2},
            {"question_en": "What is the function of the air compressor governor?", "question_es": "¿Cuál es la función del gobernador del compresor de aire?", "option1_en": "Cool the compressor", "option1_es": "Enfriar el compresor", "option2_en": "Control when the compressor charges and discharges air", "option2_es": "Controlar cuándo el compresor carga y descarga aire", "option3_en": "Regulate fuel level", "option3_es": "Regular el nivel de combustible", "correct_option": 2},
            {"question_en": "What should you do if during inspection you hear a continuous air leak?", "question_es": "¿Qué debes hacer si durante la inspección escuchas una fuga continua de aire?", "option1_en": "Use emergency brakes", "option1_es": "Usar los frenos de emergencia", "option2_en": "Ignore it if the vehicle brakes well", "option2_es": "Ignorarla si el vehículo frena bien", "option3_en": "Repair it before operating the vehicle", "option3_es": "Repararla antes de operar el vehículo", "correct_option": 3},
            {"question_en": "What part of the system maintains the air pressure necessary for the emergency brake?", "question_es": "¿Qué parte del sistema mantiene la presión de aire necesaria para el freno de emergencia?", "option1_en": "Safety valve", "option1_es": "Válvula de seguridad", "option2_en": "Emergency tank", "option2_es": "Tanque de emergencia", "option3_en": "Compressor", "option3_es": "Compresor", "correct_option": 2},
            {"question_en": "What can cause brakes to 'freeze' in cold weather?", "question_es": "¿Qué puede causar que los frenos se 'congelen' en climas fríos?", "option1_en": "Lack of brake fluid", "option1_es": "Falta de líquido de frenos", "option2_en": "Excess pressure", "option2_es": "Exceso de presión", "option3_en": "Moisture in the air system", "option3_es": "Humedad en el sistema de aire", "correct_option": 3},
            {"question_en": "What should be done if air brakes become excessively hot?", "question_es": "¿Qué se debe hacer si los frenos de aire se calientan excesivamente?", "option1_en": "Brake harder", "option1_es": "Frenar con más fuerza", "option2_en": "Use engine brake or retarder instead of service brakes", "option2_es": "Usar el freno del motor o retardador en lugar de los frenos de servicio", "option3_en": "Stop and turn off the engine", "option3_es": "Detenerse y apagar el motor", "correct_option": 2},
            {"question_en": "What is the pressure range for emergency brake activation due to low air pressure?", "question_es": "¿Cuál es el rango de presión de activación del freno de emergencia debido a baja presión de aire?", "option1_en": "60-80 psi", "option1_es": "60-80 psi", "option2_en": "20-45 psi", "option2_es": "20-45 psi", "option3_en": "100-120 psi", "option3_es": "100-120 psi", "correct_option": 2},
            {"question_en": "Why do vehicles with air brakes have dual systems?", "question_es": "¿Por qué los vehículos con frenos de aire tienen doble sistema?", "option1_en": "To brake faster", "option1_es": "Para frenar más rápido", "option2_en": "To separate front and rear brakes for safety", "option2_es": "Para separar frenos delanteros y traseros por seguridad", "option3_en": "To reduce air consumption", "option3_es": "Para reducir consumo de aire", "correct_option": 2},
            {"question_en": "What does it indicate if the spring brake does not release after pressurizing the system?", "question_es": "¿Qué indica si el freno de resorte no se libera después de presurizar el sistema?", "option1_en": "The service brake is activated", "option1_es": "El freno de servicio está activado", "option2_en": "There is a leak or failure in the system", "option2_es": "Hay una fuga o falla en el sistema", "option3_en": "The brake is working correctly", "option3_es": "El freno está funcionando correctamente", "correct_option": 2}
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
        print(f"\nSuccessfully added {added_count} new questions to 'Frenos de Aire' (Block 3)")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_air_brakes_questions_block3() 