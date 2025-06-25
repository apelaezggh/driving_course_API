from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_combination_vehicles_block3():
    db = SessionLocal()
    try:
        topic = db.query(Topic).filter(Topic.name_es == "Vehículos Combinados").first()
        if not topic:
            print("Topic 'Vehículos Combinados' not found!")
            return
        print(f"Found topic: {topic.name_es} (ID: {topic.id})")
        questions_data = [
            {"question_en": "What happens if the tractor separates from the trailer while driving?", "question_es": "¿Qué ocurre si el tractor se separa del remolque mientras conduces?", "option1_en": "The parking brake activates", "option1_es": "Se activa el freno de estacionamiento", "option2_en": "The lights turn on", "option2_es": "Se encienden las luces", "option3_en": "The trailer emergency brakes activate", "option3_es": "Se activan los frenos de emergencia del remolque", "correct_option": 3},
            {"question_en": "What should you do immediately after coupling the trailer?", "question_es": "¿Qué debes hacer justo después de acoplar el remolque?", "option1_en": "Turn on lights", "option1_es": "Encender luces", "option2_en": "Perform a complete visual inspection", "option2_es": "Realizar una inspección visual completa", "option3_en": "Honk the horn", "option3_es": "Tocar la bocina", "correct_option": 2},
            {"question_en": "What do you check in the trailer's 'kingpin'?", "question_es": "¿Qué revisas en el 'kingpin' del remolque?", "option1_en": "That it's bent", "option1_es": "Que esté doblado", "option2_en": "That it's clean", "option2_es": "Que esté limpio", "option3_en": "That it's not damaged or worn", "option3_es": "Que no esté dañado o gastado", "correct_option": 3},
            {"question_en": "Why should you avoid making tight turns with a trailer?", "question_es": "¿Por qué debes evitar hacer giros cerrados con remolque?", "option1_en": "Because tires wear out", "option1_es": "Porque se desgastan los neumáticos", "option2_en": "Because you can overturn or damage the load", "option2_es": "Porque puedes volcar o dañar la carga", "option3_en": "Because the engine strains", "option3_es": "Porque el motor se esfuerza", "correct_option": 2},
            {"question_en": "What should be checked before using trailer brakes on slopes?", "question_es": "¿Qué se debe revisar antes de usar los frenos del remolque en pendientes?", "option1_en": "That the air is complete", "option1_es": "Que el aire esté completo", "option2_en": "That the tank is full", "option2_es": "Que el tanque esté lleno", "option3_en": "That the lights are off", "option3_es": "Que las luces estén apagadas", "correct_option": 1},
            {"question_en": "When should tractor and trailer alignment be checked?", "question_es": "¿Cuándo se debe comprobar la alineación del tractor y remolque?", "option1_en": "During rain", "option1_es": "Durante la lluvia", "option2_en": "Before coupling", "option2_es": "Antes de acoplar", "option3_en": "When filling the tank", "option3_es": "Cuando llene el tanque", "correct_option": 2},
            {"question_en": "What happens if the fifth wheel coupler doesn't lock?", "question_es": "¿Qué ocurre si el acoplador de quinta rueda no se bloquea?", "option1_en": "The vehicle won't start", "option1_es": "El vehículo no arranca", "option2_en": "The trailer can come loose", "option2_es": "El remolque se puede soltar", "option3_en": "Air pressure drops", "option3_es": "La presión de aire baja", "correct_option": 2},
            {"question_en": "What is the greatest danger when uncoupling a trailer?", "question_es": "¿Cuál es el mayor peligro al desacoplar un remolque?", "option1_en": "Brake light off", "option1_es": "Luz de freno apagada", "option2_en": "That the trailer falls", "option2_es": "Que el remolque se caiga", "option3_en": "That brakes activate", "option3_es": "Que se activen los frenos", "correct_option": 2},
            {"question_en": "What indicates that the trailer is properly secured to the tractor?", "question_es": "¿Qué indica que el remolque está correctamente asegurado al tractor?", "option1_en": "Air flows well", "option1_es": "El aire fluye bien", "option2_en": "The pin is in place and the parking brake works", "option2_es": "El pasador está en su lugar y el freno de estacionamiento funciona", "option3_en": "The lights are on", "option3_es": "Las luces están encendidas", "correct_option": 2},
            {"question_en": "What part of the trailer couples with the fifth wheel?", "question_es": "¿Qué parte del remolque se acopla con la quinta rueda?", "option1_en": "The connection bar", "option1_es": "La barra de conexión", "option2_en": "The kingpin", "option2_es": "El kingpin", "option3_en": "The chassis", "option3_es": "El chasis", "correct_option": 2}
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
        print(f"\nSuccessfully added {added_count} new questions to 'Vehículos Combinados' (Block 3)")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_combination_vehicles_block3() 