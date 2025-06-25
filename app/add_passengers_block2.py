from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_passengers_block2():
    db = SessionLocal()
    try:
        # Find the Passengers topic by ID
        topic = db.query(Topic).filter(Topic.id == 19).first()
        
        if not topic:
            print("Topic ID 19 (Pasajeros) not found!")
            return
        
        print(f"Found topic: {topic.name_en} (ID: {topic.id})")
        
        # Questions data for Block 2 (remaining 15 questions)
        questions_data = [
            {
                "question_en": "How should a bus be driven on sharp curves?",
                "question_es": "¿Cómo debe conducirse un autobús en curvas cerradas?",
                "option1_en": "Fast to get out soon",
                "option1_es": "Rápido para salir pronto",
                "option2_en": "Always use the hand brake",
                "option2_es": "Usar siempre el freno de mano",
                "option3_en": "Slowly and carefully",
                "option3_es": "Despacio y con cuidado",
                "correct_option": 3
            },
            {
                "question_en": "What should the driver do if a passenger refuses to follow safety instructions?",
                "question_es": "¿Qué debe hacer el conductor si un pasajero se niega a seguir instrucciones de seguridad?",
                "option1_en": "Call police if necessary",
                "option1_es": "Llamar a la policía si es necesario",
                "option2_en": "Ignore it",
                "option2_es": "Ignorarlo",
                "option3_en": "Give them a fine",
                "option3_es": "Ponerle una multa",
                "correct_option": 1
            },
            {
                "question_en": "What is the recommended following distance with a bus?",
                "question_es": "¿Cuál es la distancia de seguimiento recomendada con un autobús?",
                "option1_en": "1 second for every 10 feet of the vehicle",
                "option1_es": "1 segundo por cada 10 pies del vehículo",
                "option2_en": "2 seconds",
                "option2_es": "2 segundos",
                "option3_en": "There's no rule",
                "option3_es": "No hay una regla",
                "correct_option": 1
            },
            {
                "question_en": "What does the 'NO STANDEES FORWARD OF WHITE LINE' sign mean?",
                "question_es": "¿Qué significa el letrero de 'NO STANDEES FORWARD OF WHITE LINE'?",
                "option1_en": "Only employees can be in front",
                "option1_es": "Solo empleados pueden estar al frente",
                "option2_en": "Passengers should not stand in front of that white line",
                "option2_es": "Los pasajeros no deben estar de pie frente a esa línea blanca",
                "option3_en": "No one can sit",
                "option3_es": "Nadie puede sentarse",
                "correct_option": 2
            },
            {
                "question_en": "What should the driver do if the bus stops on a train track?",
                "question_es": "¿Qué debe hacer el conductor si el autobús se detiene en una vía de tren?",
                "option1_en": "Call 911",
                "option1_es": "Llamar al 911",
                "option2_en": "Evacuate passengers immediately",
                "option2_es": "Evacuar a los pasajeros inmediatamente",
                "option3_en": "Wait for help",
                "option3_es": "Esperar ayuda",
                "correct_option": 2
            },
            {
                "question_en": "How should a bus be handled if there's rain or snow?",
                "question_es": "¿Cómo se debe manejar un autobús si hay lluvia o nieve?",
                "option1_en": "At normal speed",
                "option1_es": "A velocidad normal",
                "option2_en": "At higher speed",
                "option2_es": "A mayor velocidad",
                "option3_en": "Reducing speed and increasing following distance",
                "option3_es": "Reduciendo la velocidad y aumentando la distancia de seguimiento",
                "correct_option": 3
            },
            {
                "question_en": "What is the best way to avoid sudden passenger movements?",
                "question_es": "¿Cuál es la mejor forma de evitar movimientos bruscos de pasajeros?",
                "option1_en": "Maintain a constant speed",
                "option1_es": "Mantener una velocidad constante",
                "option2_en": "Avoid changing lanes",
                "option2_es": "Evitar cambiar de carril",
                "option3_en": "Avoid honking",
                "option3_es": "Evitar tocar el claxon",
                "correct_option": 1
            },
            {
                "question_en": "What action is recommended when crossing train tracks with passengers?",
                "question_es": "¿Qué acción se recomienda al cruzar vías del tren con pasajeros?",
                "option1_en": "Accelerate",
                "option1_es": "Acelerar",
                "option2_en": "Reduce speed and verify visually and audibly before crossing",
                "option2_es": "Disminuir la velocidad y verificar visual y auditivamente antes de cruzar",
                "option3_en": "Wait for a green signal",
                "option3_es": "Esperar una señal verde",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if there's an emergency evacuation?",
                "question_es": "¿Qué debe hacer si hay una evacuación de emergencia?",
                "option1_en": "Open emergency exits and calmly guide passengers",
                "option1_es": "Abrir las salidas de emergencia y guiar con calma a los pasajeros",
                "option2_en": "Wait for orders",
                "option2_es": "Esperar órdenes",
                "option3_en": "Exit first and wait outside",
                "option3_es": "Salir primero y esperar afuera",
                "correct_option": 1
            },
            {
                "question_en": "What should the bus carry according to regulations?",
                "question_es": "¿Qué debe llevar el autobús según el reglamento?",
                "option1_en": "Seat belts for everyone",
                "option1_es": "Cinturones para todos",
                "option2_en": "Fire extinguisher, reflective triangles and first aid kit",
                "option2_es": "Extintor, triángulos reflectantes y botiquín",
                "option3_en": "Only fire extinguisher",
                "option3_es": "Solo extintor",
                "correct_option": 2
            },
            {
                "question_en": "What does a poorly closed door during the journey indicate?",
                "question_es": "¿Qué indica una puerta mal cerrada durante el trayecto?",
                "option1_en": "Possible accidental opening and risk to passengers",
                "option1_es": "Posible apertura accidental y riesgo para los pasajeros",
                "option2_en": "Increased noise",
                "option2_es": "Aumento de ruido",
                "option3_en": "Nothing",
                "option3_es": "Nada",
                "correct_option": 1
            },
            {
                "question_en": "What should be done if a passenger has a medical emergency?",
                "question_es": "¿Qué se debe hacer si un pasajero tiene una emergencia médica?",
                "option1_en": "Stop, contact emergency services and assist if possible",
                "option1_es": "Detenerse, comunicarse con servicios de emergencia y asistir si es posible",
                "option2_en": "Give them water",
                "option2_es": "Darle agua",
                "option3_en": "Ask them to get off",
                "option3_es": "Pedirle que se baje",
                "correct_option": 1
            },
            {
                "question_en": "When is the driver allowed to talk to passengers?",
                "question_es": "¿Cuándo se permite al conductor hablar con los pasajeros?",
                "option1_en": "At any time",
                "option1_es": "En cualquier momento",
                "option2_en": "Only when necessary and doesn't affect driving",
                "option2_es": "Solo cuando sea necesario y no afecte la conducción",
                "option3_en": "While stopped",
                "option3_es": "Mientras está detenido",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if the rearview mirror is not well adjusted?",
                "question_es": "¿Qué debe hacer si el espejo retrovisor no está bien ajustado?",
                "option1_en": "Continue driving",
                "option1_es": "Seguir conduciendo",
                "option2_en": "Adjust it before moving the bus",
                "option2_es": "Ajustarlo antes de mover el autobús",
                "option3_en": "Wait for it to adjust itself",
                "option3_es": "Esperar que se ajuste solo",
                "correct_option": 2
            },
            {
                "question_en": "How many emergency exits should a bus with more than 36 passengers have?",
                "question_es": "¿Cuántas salidas de emergencia debe tener un autobús con más de 36 pasajeros?",
                "option1_en": "1",
                "option1_es": "1",
                "option2_en": "2",
                "option2_es": "2",
                "option3_en": "None",
                "option3_es": "Ninguna",
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
        print(f"\nSuccessfully added {added_count} new questions to 'Pasajeros' (Block 2)")
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_passengers_block2() 