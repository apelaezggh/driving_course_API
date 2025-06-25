from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_doubles_triples_block2():
    db = SessionLocal()
    try:
        topic = db.query(Topic).filter(Topic.id == 18).first()
        if not topic:
            print("Topic ID 18 (Dobles o Triples) not found!")
            return
        print(f"Found topic: {topic.name_es} (ID: {topic.id})")
        questions_data = [
            {"question_en": "How is the dolly alignment checked?", "question_es": "¿Cómo se revisa la alineación del dolly?", "option1_en": "Looking at the mirror angle", "option1_es": "Mirando el ángulo de los espejos", "option2_en": "Checking that it is centered and straight with the second trailer", "option2_es": "Verificando que esté centrado y derecho con el segundo remolque", "option3_en": "Measuring the space between axles", "option3_es": "Midiendo el espacio entre ejes", "correct_option": 2},
            {"question_en": "Which trailer should be hooked up to the tractor first?", "question_es": "¿Qué remolque se debe enganchar primero al tractor?", "option1_en": "The shortest", "option1_es": "El más corto", "option2_en": "The heaviest and closest to the tractor", "option2_es": "El más pesado y cercano al tractor", "option3_en": "Any", "option3_es": "Cualquiera", "correct_option": 2},
            {"question_en": "What should be done when checking air and electrical connections in doubles?", "question_es": "¿Qué se debe hacer al revisar conexiones de aire y electricidad en dobles?", "option1_en": "Kick them", "option1_es": "Patearlas", "option2_en": "Check for leaks, tightness and firm connections", "option2_es": "Revisar fugas, ajuste y conexiones firmes", "option3_en": "Ignore them if they work", "option3_es": "Ignorarlas si funcionan", "correct_option": 2},
            {"question_en": "What can happen if the rear trailer is not properly secured?", "question_es": "¿Qué puede pasar si el remolque trasero no está bien asegurado?", "option1_en": "Nothing", "option1_es": "Nada", "option2_en": "It can come loose while moving", "option2_es": "Puede soltarse en movimiento", "option3_en": "Only the emergency brake is activated", "option3_es": "Solo se activa el freno de emergencia", "correct_option": 2},
            {"question_en": "How should brakes be applied on long descents with doubles or triples?", "question_es": "¿Cómo se deben aplicar los frenos en bajadas largas con dobles o triples?", "option1_en": "Hard and continuous", "option1_es": "Fuerte y continuo", "option2_en": "In short pulses", "option2_es": "Por pulsos cortos", "option3_en": "With controlled and brief pressures", "option3_es": "Con presiones controladas y breves", "correct_option": 3},
            {"question_en": "What is most important when hooking a converter dolly to the tractor?", "question_es": "¿Qué es lo más importante al enganchar un convertidor dolly al tractor?", "option1_en": "Check the dolly color", "option1_es": "Revisar el color del dolly", "option2_en": "Align it correctly and secure the fifth wheel", "option2_es": "Alinearlo correctamente y asegurar la quinta rueda", "option3_en": "Make sure it has brakes", "option3_es": "Asegurarse de que tenga frenos", "correct_option": 2},
            {"question_en": "What should you do if the last trailer sways or moves too much?", "question_es": "¿Qué debes hacer si el último remolque se balancea o se mueve demasiado?", "option1_en": "Accelerate", "option1_es": "Acelerar", "option2_en": "Reduce speed smoothly", "option2_es": "Reducir la velocidad suavemente", "option3_en": "Brake hard", "option3_es": "Frenar bruscamente", "correct_option": 2},
            {"question_en": "What indicates that the fifth wheel coupling is properly closed?", "question_es": "¿Qué indica que el enganche de la quinta rueda está bien cerrado?", "option1_en": "The trailer rises", "option1_es": "El remolque se eleva", "option2_en": "The latch locks correctly and there is no visible gap", "option2_es": "El pestillo se traba correctamente y no hay espacio visible", "option3_en": "A click is heard", "option3_es": "Se escucha un clic", "correct_option": 2},
            {"question_en": "What does an air leak in a service line between trailers indicate?", "question_es": "¿Qué indica una fuga de aire en una línea de servicio entre remolques?", "option1_en": "Less air consumption", "option1_es": "Menos consumo de aire", "option2_en": "Service brake failure", "option2_es": "Fallo en los frenos de servicio", "option3_en": "Light activation", "option3_es": "Activación de luces", "correct_option": 2},
            {"question_en": "What can a poor electrical cable connection between trailers cause?", "question_es": "¿Qué puede causar una mala conexión del cable eléctrico entre remolques?", "option1_en": "ABS failure, lights or electric brake failure", "option1_es": "Fallo del ABS, luces o frenos eléctricos", "option2_en": "Higher speed", "option2_es": "Mayor velocidad", "option3_en": "More traction", "option3_es": "Más tracción", "correct_option": 1}
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
        print(f"\nSuccessfully added {added_count} new questions to 'Dobles o Triples' (Block 2)")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_doubles_triples_block2() 