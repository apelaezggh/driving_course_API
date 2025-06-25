from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_passengers_questions():
    db = SessionLocal()
    try:
        # Find the Passengers topic
        topic = db.query(Topic).filter(Topic.name_en == "Passengers").first()
        
        if not topic:
            print("Topic 'Passengers' not found!")
            return
        
        print(f"Found topic: {topic.name_en} (ID: {topic.id})")
        
        # Questions data with translations
        questions_data = [
            {
                "question_en": "What should be checked before starting a trip with passengers?",
                "question_es": "¿Qué debe revisarse antes de iniciar un viaje con pasajeros?",
                "option1_en": "Only oil level",
                "option1_es": "Solo el nivel de aceite",
                "option2_en": "Brake conditions, lights, emergency exit and safety equipment",
                "option2_es": "Condiciones de los frenos, luces, salida de emergencia y equipo de seguridad",
                "option3_en": "If there's enough gasoline",
                "option3_es": "Si hay suficiente gasolina",
                "correct_option": 2
            },
            {
                "question_en": "When should emergency equipment be checked on a bus?",
                "question_es": "¿Cuándo debe revisarse el equipo de emergencia en un autobús?",
                "option1_en": "Only in winter",
                "option1_es": "Solo en invierno",
                "option2_en": "Every 5,000 miles",
                "option2_es": "Cada 5.000 millas",
                "option3_en": "Before each trip",
                "option3_es": "Antes de cada viaje",
                "correct_option": 3
            },
            {
                "question_en": "Is it allowed to transport standing passengers on the front stairs?",
                "question_es": "¿Está permitido transportar pasajeros que estén de pie en la escalera delantera?",
                "option1_en": "Yes, if in a hurry",
                "option1_es": "Sí, si hay prisa",
                "option2_en": "Only if the bus is full",
                "option2_es": "Solo si el autobús está lleno",
                "option3_en": "No, it's never allowed",
                "option3_es": "No, nunca está permitido",
                "correct_option": 3
            },
            {
                "question_en": "What should the driver do if there's a gasoline leak or mechanical problem?",
                "question_es": "¿Qué debe hacer el conductor si hay una fuga de gasolina o un problema mecánico?",
                "option1_en": "Continue to the next destination",
                "option1_es": "Seguir hasta el próximo destino",
                "option2_en": "Call a mechanic",
                "option2_es": "Llamar a un mecánico",
                "option3_en": "Stop the vehicle and evacuate if necessary",
                "option3_es": "Detener el vehículo y evacuar si es necesario",
                "correct_option": 3
            },
            {
                "question_en": "What is prohibited to carry on a passenger bus?",
                "question_es": "¿Qué está prohibido llevar en un autobús de pasajeros?",
                "option1_en": "Luggage in the aisles",
                "option1_es": "Equipaje en los pasillos",
                "option2_en": "Closed suitcases",
                "option2_es": "Maletas cerradas",
                "option3_en": "Water bottles",
                "option3_es": "Botellas de agua",
                "correct_option": 1
            },
            {
                "question_en": "What should be done if transporting luggage inside the bus?",
                "question_es": "¿Qué debe hacer si transporta equipaje dentro del autobús?",
                "option1_en": "Secure it to prevent blocking aisles and exits",
                "option1_es": "Asegurarlo para evitar que obstruya pasillos y salidas",
                "option2_en": "Allow passengers to place it wherever they want",
                "option2_es": "Permitir que los pasajeros lo coloquen donde quieran",
                "option3_en": "Store it on the roof",
                "option3_es": "Guardarlo en el techo",
                "correct_option": 1
            },
            {
                "question_en": "What is the maximum number of emergencies a bus must have for evacuation?",
                "question_es": "¿Cuál es el número máximo de emergencias que un autobús debe tener para evacuar?",
                "option1_en": "None",
                "option1_es": "Ninguna",
                "option2_en": "At least one emergency exit",
                "option2_es": "Al menos una salida de emergencia",
                "option3_en": "Depends on size",
                "option3_es": "Depende del tamaño",
                "correct_option": 2
            },
            {
                "question_en": "Is it allowed to transport hazardous materials on a passenger bus?",
                "question_es": "¿Está permitido transportar materiales peligrosos en un autobús de pasajeros?",
                "option1_en": "No",
                "option1_es": "No",
                "option2_en": "Yes, if properly labeled",
                "option2_es": "Sí, si están debidamente etiquetados",
                "option3_en": "Yes, but only limited quantities allowed by law",
                "option3_es": "Sí, pero solo cantidades limitadas permitidas por ley",
                "correct_option": 3
            },
            {
                "question_en": "What should the driver do when approaching a railroad crossing?",
                "question_es": "¿Qué debe hacer el conductor al acercarse a un cruce ferroviario?",
                "option1_en": "Reduce speed",
                "option1_es": "Reducir la velocidad",
                "option2_en": "Always stop, open the door and look",
                "option2_es": "Detenerse siempre, abrir la puerta y mirar",
                "option3_en": "Pass slowly",
                "option3_es": "Pasar lentamente",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if a passenger creates an unsafe situation?",
                "question_es": "¿Qué debe hacer si un pasajero crea una situación insegura?",
                "option1_en": "Ignore it",
                "option1_es": "Ignorarlo",
                "option2_en": "Remove them without saying anything",
                "option2_es": "Sacarlo sin decir nada",
                "option3_en": "Stop the bus and resolve the situation safely",
                "option3_es": "Detener el autobús y resolver la situación de manera segura",
                "correct_option": 3
            },
            {
                "question_en": "What should be done before moving the bus from a stop?",
                "question_es": "¿Qué debe hacer antes de mover el autobús desde una parada?",
                "option1_en": "Honk the horn",
                "option1_es": "Tocar la bocina",
                "option2_en": "Verify all passengers are seated and secure",
                "option2_es": "Verificar que todos los pasajeros estén sentados y seguros",
                "option3_en": "Check fuel level",
                "option3_es": "Verificar el nivel de gasolina",
                "correct_option": 2
            },
            {
                "question_en": "When can a driver block a pedestrian crossing?",
                "question_es": "¿Cuándo puede un conductor bloquear un cruce peatonal?",
                "option1_en": "Never",
                "option1_es": "Nunca",
                "option2_en": "If there's heavy traffic",
                "option2_es": "Si hay mucho tráfico",
                "option3_en": "Only if unloading",
                "option3_es": "Solo si está descargando",
                "correct_option": 1
            },
            {
                "question_en": "What should be done when braking with a bus full of passengers?",
                "question_es": "¿Qué debe hacer al frenar con un autobús lleno de pasajeros?",
                "option1_en": "Brake hard",
                "option1_es": "Frenar bruscamente",
                "option2_en": "Brake smoothly and progressively",
                "option2_es": "Frenar de forma suave y progresiva",
                "option3_en": "Use only the parking brake",
                "option3_es": "Usar solo el freno de estacionamiento",
                "correct_option": 2
            },
            {
                "question_en": "When is it allowed to drive a bus with an open door?",
                "question_es": "¿Cuándo se permite conducir un autobús con una puerta abierta?",
                "option1_en": "Only in rural areas",
                "option1_es": "Solo en zonas rurales",
                "option2_en": "Never",
                "option2_es": "Nunca",
                "option3_en": "If going less than 5 mph",
                "option3_es": "Si se va a menos de 5 mph",
                "correct_option": 2
            },
            {
                "question_en": "What should be done when picking up passengers?",
                "question_es": "¿Qué debe hacer al recoger pasajeros?",
                "option1_en": "Park in a safe place and use signals",
                "option1_es": "Estacionar en un lugar seguro y usar señales",
                "option2_en": "Stop wherever there's space",
                "option2_es": "Detenerse donde haya espacio",
                "option3_en": "Use the horn",
                "option3_es": "Usar el claxon",
                "correct_option": 1
            },
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
                "option1_en": "1 second for every 10 feet of vehicle",
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
        
        # Add questions to database
        added_count = 0
        for q_data in questions_data:
            # Check if question already exists
            existing_question = db.query(Question).filter(
                Question.question_en == q_data["question_en"],
                Question.topic_id == topic.id
            ).first()
            
            if not existing_question:
                question = Question(topic_id=topic.id, **q_data)
                db.add(question)
                added_count += 1
                print(f"Added question: {q_data['question_en']}")
            else:
                print(f"Question already exists: {q_data['question_en']}")
        
        db.commit()
        print(f"\nSuccessfully added {added_count} new questions to 'Passengers'")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
        
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_passengers_questions() 