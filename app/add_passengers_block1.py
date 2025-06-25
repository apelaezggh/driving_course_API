from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_passengers_block1():
    db = SessionLocal()
    try:
        # Find the Passengers topic by ID
        topic = db.query(Topic).filter(Topic.id == 19).first()
        
        if not topic:
            print("Topic ID 19 (Pasajeros) not found!")
            return
        
        print(f"Found topic: {topic.name_en} (ID: {topic.id})")
        
        # Questions data for Block 1 (first 15 questions)
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
        print(f"\nSuccessfully added {added_count} new questions to 'Pasajeros' (Block 1)")
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_passengers_block1() 