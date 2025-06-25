from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_combination_vehicles_block1():
    db = SessionLocal()
    try:
        topic = db.query(Topic).filter(Topic.name_es == "Vehículos Combinados").first()
        if not topic:
            print("Topic 'Vehículos Combinados' not found!")
            return
        print(f"Found topic: {topic.name_es} (ID: {topic.id})")
        questions_data = [
            {"question_en": "What causes most rollovers in combination vehicles?", "question_es": "¿Qué causa la mayoría de los vuelcos en vehículos combinados?", "option1_en": "Braking hard", "option1_es": "Frenar con fuerza", "option2_en": "Taking curves too fast", "option2_es": "Tomar curvas demasiado rápido", "option3_en": "Bad road conditions", "option3_es": "Malas condiciones del camino", "correct_option": 2},
            {"question_en": "What is 'jackknife' in a combination vehicle?", "question_es": "¿Qué es el 'jackknife' en un vehículo combinado?", "option1_en": "A type of coupler", "option1_es": "Un tipo de acoplador", "option2_en": "An emergency tool", "option2_es": "Una herramienta de emergencia", "option3_en": "When the trailer folds against the tractor", "option3_es": "Cuando el remolque se pliega contra el tractor", "correct_option": 3},
            {"question_en": "What is the best way to avoid jackknife?", "question_es": "¿Cuál es la mejor forma de evitar el jackknife?", "option1_en": "Accelerate in curves", "option1_es": "Acelerar en curvas", "option2_en": "Brake early and smoothly", "option2_es": "Frenar temprano y suavemente", "option3_en": "Use emergency brake", "option3_es": "Usar el freno de emergencia", "correct_option": 2},
            {"question_en": "Why is it more difficult to brake a combination vehicle?", "question_es": "¿Por qué es más difícil frenar un vehículo combinado?", "option1_en": "Due to additional weight", "option1_es": "Por el peso adicional", "option2_en": "Because it has more wheels", "option2_es": "Por tener más ruedas", "option3_en": "Because it has more lights", "option3_es": "Porque tiene más luces", "correct_option": 1},
            {"question_en": "What part brakes first when using only the trailer brake?", "question_es": "¿Qué parte se frena primero cuando se usa solo el freno de remolque?", "option1_en": "Traction", "option1_es": "Tracción", "option2_en": "Trailer", "option2_es": "Remolque", "option3_en": "Tractor", "option3_es": "Tractor", "correct_option": 2},
            {"question_en": "What happens if the trailer doesn't have enough weight and brakes sharply?", "question_es": "¿Qué pasa si el remolque no tiene suficiente peso y se frena bruscamente?", "option1_en": "The tractor can push it", "option1_es": "El tractor puede empujarlo", "option2_en": "The trailer can skid or overturn", "option2_es": "El remolque puede patinar o volcarse", "option3_en": "The brake regenerates", "option3_es": "El freno se regenera", "correct_option": 2},
            {"question_en": "What indicates that a trailer is not properly coupled?", "question_es": "¿Qué indica que un remolque no está bien acoplado?", "option1_en": "The parking brake activates", "option1_es": "El freno de estacionamiento se activa", "option2_en": "A whistle is heard", "option2_es": "Se oye un silbido", "option3_en": "The trailer falls off the tractor", "option3_es": "El remolque se cae del tractor", "correct_option": 3},
            {"question_en": "What is the correct use of the trailer emergency valve?", "question_es": "¿Cuál es el uso correcto de la válvula de emergencia del remolque?", "option1_en": "Disconnect ABS brake", "option1_es": "Desconectar el freno ABS", "option2_en": "Stop the trailer in case of pressure loss", "option2_es": "Detener el remolque en caso de pérdida de presión", "option3_en": "Turn off the engine", "option3_es": "Apagar el motor", "correct_option": 2},
            {"question_en": "What should be done before disconnecting a trailer?", "question_es": "¿Qué se debe hacer antes de desconectar un remolque?", "option1_en": "Turn off the lights", "option1_es": "Apagar las luces", "option2_en": "Lower the landing gear", "option2_es": "Bajar las patas de apoyo (landing gear)", "option3_en": "Increase air pressure", "option3_es": "Aumentar la presión de aire", "correct_option": 2},
            {"question_en": "Where is the tractor protection valve located?", "question_es": "¿Dónde se encuentra la válvula de protección del tractor?", "option1_en": "In the engine", "option1_es": "En el motor", "option2_en": "In the rear of the tractor", "option2_es": "En la parte trasera del tractor", "option3_en": "In the dashboard", "option3_es": "En el tablero", "correct_option": 2},
            {"question_en": "What does the tractor protection valve prevent?", "question_es": "¿Qué previene la válvula de protección del tractor?", "option1_en": "Loss of tractor air in case of trailer leak", "option1_es": "Pérdida de aire del tractor en caso de fuga en el remolque", "option2_en": "Engine damage", "option2_es": "Daños al motor", "option3_en": "Accidental uncoupling", "option3_es": "Desacoplamiento accidental", "correct_option": 1},
            {"question_en": "How is it verified that the trailer is properly coupled?", "question_es": "¿Cómo se verifica que el remolque está bien acoplado?", "option1_en": "By backing up", "option1_es": "Dando marcha atrás", "option2_en": "Checking that the locking pin is secured", "option2_es": "Revisando que el pasador de bloqueo esté asegurado", "option3_en": "Touching the lights", "option3_es": "Tocando las luces", "correct_option": 2},
            {"question_en": "What does 'unbalanced weight' mean in a trailer?", "question_es": "¿Qué significa 'peso desbalanceado' en un remolque?", "option1_en": "Poorly distributed load", "option1_es": "Carga mal distribuida", "option2_en": "Deflated tires", "option2_es": "Neumáticos desinflados", "option3_en": "Cold brakes", "option3_es": "Frenos fríos", "correct_option": 1},
            {"question_en": "When is the trailer service valve used?", "question_es": "¿Cuándo se usa la válvula de servicio del remolque?", "option1_en": "To turn on lights", "option1_es": "Para encender luces", "option2_en": "To brake with the main pedal", "option2_es": "Para frenar con el pedal principal", "option3_en": "To brake manually", "option3_es": "Para frenar manualmente", "correct_option": 2},
            {"question_en": "How should you drive when transporting an empty trailer?", "question_es": "¿Cómo debes conducir cuando transportas un remolque vacío?", "option1_en": "Same as loaded", "option1_es": "Igual que cargado", "option2_en": "Faster", "option2_es": "Más rápido", "option3_en": "More slowly and carefully", "option3_es": "Más despacio y con cuidado", "correct_option": 3}
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
        print(f"\nSuccessfully added {added_count} new questions to 'Vehículos Combinados' (Block 1)")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_combination_vehicles_block1() 