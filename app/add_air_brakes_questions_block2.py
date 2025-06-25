from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_air_brakes_questions_block2():
    db = SessionLocal()
    try:
        topic = db.query(Topic).filter(Topic.name_es == "Frenos de Aire").first()
        if not topic:
            print("Topic 'Frenos de Aire' not found!")
            return
        print(f"Found topic: {topic.name_es} (ID: {topic.id})")
        questions_data = [
            {"question_en": "When is the tractor protection valve activated?", "question_es": "¿Cuándo se activa la válvula de protección del tractor?", "option1_en": "When the hand brake is applied", "option1_es": "Cuando se aplica el freno de mano", "option2_en": "When air pressure drops below a safe level", "option2_es": "Cuando la presión de aire cae por debajo de un nivel seguro", "option3_en": "When the steering wheel is turned", "option3_es": "Cuando se gira el volante", "correct_option": 2},
            {"question_en": "What can cause moisture in the air system?", "question_es": "¿Qué puede causar humedad en el sistema de aire?", "option1_en": "Unfiltered compressed air", "option1_es": "Aire comprimido sin filtrado", "option2_en": "Excess oil", "option2_es": "Exceso de aceite", "option3_en": "Dirty filters", "option3_es": "Filtros sucios", "correct_option": 1},
            {"question_en": "What does 'controlled braking' mean?", "question_es": "¿Qué significa 'frenado controlado'?", "option1_en": "Apply brakes suddenly", "option1_es": "Aplicar frenos de golpe", "option2_en": "Brake hard all the time", "option2_es": "Frenar fuerte todo el tiempo", "option3_en": "Apply brakes firmly without locking wheels", "option3_es": "Aplicar frenos firmemente sin bloquear ruedas", "correct_option": 3},
            {"question_en": "What should you do if your vehicle has ABS brake system?", "question_es": "¿Qué debe hacer si su vehículo tiene sistema de frenos ABS?", "option1_en": "Brake normally", "option1_es": "Frenar normalmente", "option2_en": "Use only engine brake", "option2_es": "Usar solo el freno de motor", "option3_en": "Brake more slowly", "option3_es": "Frenar más despacio", "correct_option": 1},
            {"question_en": "What does the ABS system do?", "question_es": "¿Qué hace el sistema ABS?", "option1_en": "Reduces tire wear", "option1_es": "Reduce el desgaste de llantas", "option2_en": "Prevents wheels from locking when braking", "option2_es": "Evita que las ruedas se bloqueen al frenar", "option3_en": "Decreases brake pressure", "option3_es": "Disminuye la presión de los frenos", "correct_option": 2},
            {"question_en": "How is the ABS system operation tested?", "question_es": "¿Cómo se prueba el funcionamiento del sistema ABS?", "option1_en": "By checking the air valve", "option1_es": "Revisando la válvula de aire", "option2_en": "By verifying that the ABS light turns on and off", "option2_es": "Verificando que se encienda y apague la luz de ABS", "option3_en": "By braking hard", "option3_es": "Frenando a fondo", "correct_option": 2},
            {"question_en": "What part of the brake system maintains pressure to apply service brakes?", "question_es": "¿Qué parte del sistema de frenos mantiene presión para aplicar los frenos de servicio?", "option1_en": "Reserve tank", "option1_es": "Tanque de reserva", "option2_en": "Supply tank", "option2_es": "Tanque de suministro", "option3_en": "Control valve", "option3_es": "Válvula de control", "correct_option": 2},
            {"question_en": "What happens if the brake is pressed repeatedly in an air system?", "question_es": "¿Qué ocurre si se pisa el freno repetidamente en un sistema de aire?", "option1_en": "It cools down", "option1_es": "Se enfría", "option2_en": "It recharges", "option2_es": "Se recarga", "option3_en": "It loses pressure rapidly", "option3_es": "Se pierde presión rápidamente", "correct_option": 3},
            {"question_en": "What function does the brake pedal have in vehicles with air brakes?", "question_es": "¿Qué función tiene el pedal de freno en vehículos con frenos de aire?", "option1_en": "Releases the parking brake", "option1_es": "Libera el freno de estacionamiento", "option2_en": "Controls the amount of pressure sent to the brakes", "option2_es": "Controla la cantidad de presión enviada a los frenos", "option3_en": "Activates the air compressor", "option3_es": "Activa el compresor de aire", "correct_option": 2},
            {"question_en": "What should be done if an air leak is heard in the brake system?", "question_es": "¿Qué se debe hacer si se escucha una fuga de aire en el sistema de frenos?", "option1_en": "Ignore it", "option1_es": "Ignorarla", "option2_en": "Report it and repair it before driving", "option2_es": "Reportarla y repararla antes de conducir", "option3_en": "Cover it with tape", "option3_es": "Taparla con cinta", "correct_option": 2},
            {"question_en": "What is the minimum air pressure required before driving?", "question_es": "¿Cuál es el mínimo de presión de aire requerida antes de conducir?", "option1_en": "50 psi", "option1_es": "50 psi", "option2_en": "100 psi", "option2_es": "100 psi", "option3_en": "30 psi", "option3_es": "30 psi", "correct_option": 2},
            {"question_en": "What should you do when stopping on a steep slope?", "question_es": "¿Qué debes hacer al detenerte en una pendiente pronunciada?", "option1_en": "Turn off the engine", "option1_es": "Apagar el motor", "option2_en": "Use spring brakes and chocks", "option2_es": "Usar los frenos de resorte y calzas", "option3_en": "Only hand brake", "option3_es": "Solo freno de mano", "correct_option": 2},
            {"question_en": "What does a front brake limiting valve do?", "question_es": "¿Qué hace una válvula limitadora de freno delantero?", "option1_en": "Reduces brake noise", "option1_es": "Reduce el ruido del freno", "option2_en": "Reduces air pressure in front brakes to prevent locking", "option2_es": "Reduce la presión de aire en los frenos delanteros para evitar bloqueo", "option3_en": "Increases pressure", "option3_es": "Aumenta la presión", "correct_option": 2},
            {"question_en": "What pressure is required for the low pressure warning signal to turn off?", "question_es": "¿Qué presión se requiere para que se desactive la señal de advertencia de presión baja?", "option1_en": "60 psi", "option1_es": "60 psi", "option2_en": "20 psi", "option2_es": "20 psi", "option3_en": "80 psi", "option3_es": "80 psi", "correct_option": 1},
            {"question_en": "What can happen if spring brakes fail?", "question_es": "¿Qué puede ocurrir si los frenos de resorte fallan?", "option1_en": "The vehicle won't start", "option1_es": "El vehículo no arranca", "option2_en": "The vehicle may be left without parking brake", "option2_es": "El vehículo puede quedarse sin freno de estacionamiento", "option3_en": "The engine turns off", "option3_es": "El motor se apaga", "correct_option": 2}
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
        print(f"\nSuccessfully added {added_count} new questions to 'Frenos de Aire' (Block 2)")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_air_brakes_questions_block2() 