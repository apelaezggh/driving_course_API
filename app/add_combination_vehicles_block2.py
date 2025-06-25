from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_combination_vehicles_block2():
    db = SessionLocal()
    try:
        topic = db.query(Topic).filter(Topic.name_es == "Vehículos Combinados").first()
        if not topic:
            print("Topic 'Vehículos Combinados' not found!")
            return
        print(f"Found topic: {topic.name_es} (ID: {topic.id})")
        questions_data = [
            {"question_en": "What can cause poor trailer coupling?", "question_es": "¿Qué puede causar un mal acoplamiento del remolque?", "option1_en": "Damage to the fifth wheel", "option1_es": "Daños en la quinta rueda", "option2_en": "Full tank", "option2_es": "Tanque lleno", "option3_en": "Seat height", "option3_es": "Altura del asiento", "correct_option": 1},
            {"question_en": "What do you check in the fifth wheel when coupling?", "question_es": "¿Qué revisas en la quinta rueda al acoplar?", "option1_en": "That it's painted", "option1_es": "Que esté pintada", "option2_en": "That it has grease and is locked", "option2_es": "Que tenga grasa y esté bloqueada", "option3_en": "That it's rusty", "option3_es": "Que esté oxidada", "correct_option": 2},
            {"question_en": "What indicates a trailer pulling to one side?", "question_es": "¿Qué indica un tirón del remolque hacia un lado?", "option1_en": "Deflated tires", "option1_es": "Neumáticos desinflados", "option2_en": "Misadjusted brakes", "option2_es": "Frenos desajustados", "option3_en": "Light problem", "option3_es": "Problema con luces", "correct_option": 2},
            {"question_en": "What should be done when backing up to couple a trailer?", "question_es": "¿Qué se debe hacer al retroceder para acoplar un remolque?", "option1_en": "Go fast", "option1_es": "Ir rápido", "option2_en": "Use the right mirror", "option2_es": "Usar el espejo derecho", "option3_en": "Align tractor and trailer correctly", "option3_es": "Alinear tractor y remolque correctamente", "correct_option": 3},
            {"question_en": "What must be completely closed before hooking up a trailer?", "question_es": "¿Qué debe estar completamente cerrado antes de enganchar un remolque?", "option1_en": "The fuel cap", "option1_es": "La tapa del combustible", "option2_en": "The coupler mouth (fifth wheel)", "option2_es": "La boca del acoplador (quinta rueda)", "option3_en": "The trailer door", "option3_es": "La puerta del remolque", "correct_option": 2},
            {"question_en": "What does the safety pin in the fifth wheel do?", "question_es": "¿Qué hace el pasador de seguridad en la quinta rueda?", "option1_en": "Secures the coupler", "option1_es": "Fija el acoplador", "option2_en": "Connects the lights", "option2_es": "Conecta las luces", "option3_en": "Activates the brake", "option3_es": "Activa el freno", "correct_option": 1},
            {"question_en": "What is the 'glad hand'?", "question_es": "¿Qué es el 'glad hand'?", "option1_en": "A safety lever", "option1_es": "Una palanca de seguridad", "option2_en": "An air hose connector", "option2_es": "Un conector de manguera de aire", "option3_en": "Part of the brake", "option3_es": "Parte del freno", "correct_option": 2},
            {"question_en": "What indicates an air leak in the glad hands?", "question_es": "¿Qué indica una fuga de aire en los glad hands?", "option1_en": "Pressure failure", "option1_es": "Falla de presión", "option2_en": "Lack of fuel", "option2_es": "Falta de combustible", "option3_en": "Lights off", "option3_es": "Luces apagadas", "correct_option": 1},
            {"question_en": "What does the trailer manual brake valve do?", "question_es": "¿Qué hace la válvula de freno manual del remolque?", "option1_en": "Applies only trailer brakes", "option1_es": "Aplica solo los frenos del remolque", "option2_en": "Activates ABS", "option2_es": "Activa ABS", "option3_en": "Uncouples the trailer", "option3_es": "Desacopla el remolque", "correct_option": 1},
            {"question_en": "What part supports the trailer when not connected?", "question_es": "¿Qué parte sostiene el remolque cuando no está conectado?", "option1_en": "Chassis", "option1_es": "Chasis", "option2_en": "Landing gear", "option2_es": "Landing gear (patas de apoyo)", "option3_en": "Rear lights", "option3_es": "Luces traseras", "correct_option": 2},
            {"question_en": "What should you do when uncoupling the trailer on a slope?", "question_es": "¿Qué debes hacer al desacoplar el remolque en una pendiente?", "option1_en": "Leave the engine running", "option1_es": "Dejar el motor encendido", "option2_en": "Use chocks", "option2_es": "Usar cuñas (calzas)", "option3_en": "Turn the steering wheel", "option3_es": "Girar el volante", "correct_option": 2},
            {"question_en": "What is the 'pull test'?", "question_es": "¿Qué es el 'pull test'?", "option1_en": "Accelerate quickly", "option1_es": "Acelerar rápido", "option2_en": "Pull the trailer gently to check coupling", "option2_es": "Tirar del remolque suavemente para comprobar acoplamiento", "option3_en": "Test the brakes", "option3_es": "Probar los frenos", "correct_option": 2},
            {"question_en": "Why is it important to check air lines between tractor and trailer?", "question_es": "¿Por qué es importante revisar las líneas de aire entre tractor y remolque?", "option1_en": "In case they have dust", "option1_es": "Por si tienen polvo", "option2_en": "In case they are broken, loose or leaking", "option2_es": "Por si están rotas, sueltas o con fugas", "option3_en": "To verify temperature", "option3_es": "Para verificar la temperatura", "correct_option": 2},
            {"question_en": "What happens if you connect air lines incorrectly between tractor and trailer?", "question_es": "¿Qué pasa si conectas mal las líneas de aire entre tractor y remolque?", "option1_en": "Brake failure", "option1_es": "Fallo de frenos", "option2_en": "Light failure", "option2_es": "Fallo de luces", "option3_en": "Engine shuts off", "option3_es": "Se apaga el motor", "correct_option": 1},
            {"question_en": "What should you check when doing a visual inspection of the coupling?", "question_es": "¿Qué debes revisar al hacer una inspección visual del acoplamiento?", "option1_en": "Color of the fifth wheel", "option1_es": "Color de la quinta rueda", "option2_en": "Locked pin and no gap between plate and trailer", "option2_es": "Pasador bloqueado y sin espacio entre el plato y remolque", "option3_en": "That there's mud", "option3_es": "Que haya lodo", "correct_option": 2}
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
        print(f"\nSuccessfully added {added_count} new questions to 'Vehículos Combinados' (Block 2)")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_combination_vehicles_block2() 