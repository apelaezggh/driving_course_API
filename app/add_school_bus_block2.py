from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_school_bus_block2():
    db = SessionLocal()
    try:
        # Find the School Bus topic by ID
        topic = db.query(Topic).filter(Topic.id == 20).first()
        
        if not topic:
            print("Topic ID 20 (Autobús Escolar) not found!")
            return
        
        print(f"Found topic: {topic.name_en} (ID: {topic.id})")
        
        # Questions data for Block 2 (remaining 15 questions)
        questions_data = [
            {
                "question_en": "What is the safest evacuation procedure?",
                "question_es": "¿Cuál es el procedimiento de evacuación más seguro?",
                "option1_en": "Let students decide",
                "option1_es": "Dejar a los estudiantes decidir",
                "option2_en": "Train them and practice periodic evacuations",
                "option2_es": "Entrenarlos y practicar evacuaciones periódicas",
                "option3_en": "Use only one exit",
                "option3_es": "Usar solo una salida",
                "correct_option": 2
            },
            {
                "question_en": "What type of brake should be especially checked on school buses?",
                "question_es": "¿Qué tipo de freno debe revisarse especialmente en autobuses escolares?",
                "option1_en": "Parking brake",
                "option1_es": "De estacionamiento",
                "option2_en": "Emergency brake",
                "option2_es": "Freno de emergencia",
                "option3_en": "Service brake and air brakes if it has them",
                "option3_es": "Freno de servicio y frenos de aire si los tiene",
                "correct_option": 3
            },
            {
                "question_en": "What is a valid reason to evacuate the school bus?",
                "question_es": "¿Cuál es una razón válida para evacuar el autobús escolar?",
                "option1_en": "Extreme heat",
                "option1_es": "Calor extremo",
                "option2_en": "Immediate risk such as fire, collision or fuel spill",
                "option2_es": "Riesgo inmediato como incendio, colisión o derrame de combustible",
                "option3_en": "Heavy traffic",
                "option3_es": "Tráfico pesado",
                "correct_option": 2
            },
            {
                "question_en": "What should be checked in a post-trip inspection?",
                "question_es": "¿Qué debe revisar en una inspección posterior al viaje?",
                "option1_en": "That there are no forgotten students or belongings",
                "option1_es": "Que no haya estudiantes o pertenencias olvidadas",
                "option2_en": "Only the engine",
                "option2_es": "Solo el motor",
                "option3_en": "That there's no exterior damage",
                "option3_es": "Que no haya daños exteriores",
                "correct_option": 1
            },
            {
                "question_en": "What should be done if a student causes distraction while driving?",
                "question_es": "¿Qué debe hacer si un estudiante causa distracción mientras conduce?",
                "option1_en": "Yell at them",
                "option1_es": "Gritarle",
                "option2_en": "Stop in a safe place and correct the situation",
                "option2_es": "Detenerse en un lugar seguro y corregir la situación",
                "option3_en": "Ignore it",
                "option3_es": "Ignorarlo",
                "correct_option": 2
            },
            {
                "question_en": "What is the best way to handle an emergency evacuation?",
                "question_es": "¿Cuál es la mejor forma de manejar una evacuación de emergencia?",
                "option1_en": "Exit one by one in silence",
                "option1_es": "Salir uno por uno en silencio",
                "option2_en": "With prior practice and driver guidance",
                "option2_es": "Con práctica previa y guía del conductor",
                "option3_en": "Always through the rear door",
                "option3_es": "Por la puerta trasera siempre",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if the bus breaks down on a railroad track?",
                "question_es": "¿Qué debe hacer si el autobús se descompone en una vía de tren?",
                "option1_en": "Call a tow truck",
                "option1_es": "Llamar a una grúa",
                "option2_en": "Evacuate immediately and move students away at a 45-degree angle",
                "option2_es": "Evacuar inmediatamente y alejar a los estudiantes en un ángulo de 45 grados",
                "option3_en": "Wait for help",
                "option3_es": "Esperar ayuda",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if there's bad weather and students are waiting on the street?",
                "question_es": "¿Qué debe hacer si hay mal clima y los estudiantes esperan en la calle?",
                "option1_en": "Make them get on quickly",
                "option1_es": "Hacerlos subir rápidamente",
                "option2_en": "Help them get on safely using warning lights",
                "option2_es": "Ayudarlos a subir de manera segura usando luces de advertencia",
                "option3_en": "Don't stop",
                "option3_es": "No detenerse",
                "correct_option": 2
            },
            {
                "question_en": "What additional precaution should be taken in school zones?",
                "question_es": "¿Qué precaución adicional debe tomarse en zonas escolares?",
                "option1_en": "Only brake more",
                "option1_es": "Solo frenar más",
                "option2_en": "Reduced speed and alert for children near the roadway",
                "option2_es": "Velocidad reducida y alerta por niños cerca de la vía",
                "option3_en": "Honk the horn",
                "option3_es": "Tocar la bocina",
                "correct_option": 2
            },
            {
                "question_en": "When is the STOP signal activated on a school bus?",
                "question_es": "¿Cuándo se activa la señal de STOP en un autobús escolar?",
                "option1_en": "Whenever the door opens",
                "option1_es": "Siempre que se abre la puerta",
                "option2_en": "When picking up or dropping off students and crossing the roadway",
                "option2_es": "Cuando se recogen o dejan estudiantes y hay que cruzar la vía",
                "option3_en": "Only in rural areas",
                "option3_es": "Solo en zona rural",
                "correct_option": 2
            },
            {
                "question_en": "What should be done when approaching a stop not visible due to a curve?",
                "question_es": "¿Qué debe hacer al acercarse a una parada no visible por una curva?",
                "option1_en": "Honk the horn",
                "option1_es": "Sonar la bocina",
                "option2_en": "Activate amber lights with sufficient advance notice",
                "option2_es": "Activar luces ámbar con suficiente anticipación",
                "option3_en": "Accelerate",
                "option3_es": "Acelerar",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if a student behaves violently?",
                "question_es": "¿Qué debe hacer si un estudiante se comporta violentamente?",
                "option1_en": "Report it upon arrival",
                "option1_es": "Reportarlo al llegar",
                "option2_en": "Stop the bus if safe and calm the situation",
                "option2_es": "Detener el autobús si es seguro y calmar la situación",
                "option3_en": "Ask another student to control them",
                "option3_es": "Pedirle a otro estudiante que lo controle",
                "correct_option": 2
            },
            {
                "question_en": "When should braking begin for a school stop?",
                "question_es": "¿Cuándo debe comenzar a frenar para una parada escolar?",
                "option1_en": "Immediately upon seeing it",
                "option1_es": "Inmediatamente al verla",
                "option2_en": "With anticipation and gradually",
                "option2_es": "Con anticipación y de manera gradual",
                "option3_en": "Upon arrival",
                "option3_es": "Al llegar",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if the mirrors are not adjusted?",
                "question_es": "¿Qué debe hacer si los espejos no están ajustados?",
                "option1_en": "Adjust them while driving",
                "option1_es": "Ajustarlos al conducir",
                "option2_en": "Adjust them before starting the trip",
                "option2_es": "Ajustarlos antes de iniciar el viaje",
                "option3_en": "Don't use them",
                "option3_es": "No usarlos",
                "correct_option": 2
            },
            {
                "question_en": "What is mandatory to have on a school bus by law?",
                "question_es": "¿Qué es obligatorio tener en un autobús escolar por ley?",
                "option1_en": "An experienced driver",
                "option1_es": "Un conductor con experiencia",
                "option2_en": "Stop sign, flashing lights, emergency equipment and emergency exit",
                "option2_es": "Señal de alto, luces intermitentes, equipo de emergencia y salida de emergencia",
                "option3_en": "Only seat belts",
                "option3_es": "Solo cinturones",
                "correct_option": 2
            }
        ]
        
        added_count = 0
        for question_data in questions_data:
            # Check if question already exists
            existing_question = db.query(Question).filter(
                Question.question_es == question_data["question_es"],
                Question.topic_id == topic.id
            ).first()
            
            if existing_question:
                print(f"Question already exists: {question_data['question_es']}")
                continue
            
            # Create new question
            new_question = Question(
                topic_id=topic.id,
                question_en=question_data["question_en"],
                question_es=question_data["question_es"],
                option1_en=question_data["option1_en"],
                option1_es=question_data["option1_es"],
                option2_en=question_data["option2_en"],
                option2_es=question_data["option2_es"],
                option3_en=question_data["option3_en"],
                option3_es=question_data["option3_es"],
                correct_option=question_data["correct_option"]
            )
            
            db.add(new_question)
            added_count += 1
            print(f"Added question: {question_data['question_es']}")
        
        db.commit()
        print(f"\nSuccessfully added {added_count} new questions to 'Autobús Escolar' (Block 2)")
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_school_bus_block2() 