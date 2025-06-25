from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_tank_questions():
    db = SessionLocal()
    try:
        # Find the Tank topic
        topic = db.query(Topic).filter(Topic.name_en == "Tank").first()
        
        if not topic:
            print("Topic 'Tank' not found!")
            return
        
        print(f"Found topic: {topic.name_en} (ID: {topic.id})")
        
        # Questions data with translations
        questions_data = [
            {
                "question_en": "What effect can the movement of liquid inside a tank cause during driving?",
                "question_es": "¿Qué efecto puede causar el movimiento del líquido dentro de una cisterna durante la conducción?",
                "option1_en": "Speed reduction",
                "option1_es": "Reducción de velocidad",
                "option2_en": "Loss of traction",
                "option2_es": "Pérdida de tracción",
                "option3_en": "Surge, affecting vehicle control",
                "option3_es": "Oleaje (surge), afectando el control del vehículo",
                "correct_option": 3
            },
            {
                "question_en": "What type of liquid is most dangerous to transport due to its movement?",
                "question_es": "¿Qué tipo de líquido es más peligroso de transportar por su movimiento?",
                "option1_en": "Frozen liquid",
                "option1_es": "Líquido congelado",
                "option2_en": "Very dense liquid",
                "option2_es": "Líquido muy denso",
                "option3_en": "Partially filled liquid",
                "option3_es": "Líquido parcialmente lleno",
                "correct_option": 3
            },
            {
                "question_en": "What should the driver do to control surge?",
                "question_es": "¿Qué debe hacer el conductor para controlar el oleaje (surge)?",
                "option1_en": "Accelerate when turning",
                "option1_es": "Acelerar al girar",
                "option2_en": "Brake gently",
                "option2_es": "Frenar suavemente",
                "option3_en": "Brake hard",
                "option3_es": "Frenar bruscamente",
                "correct_option": 2
            },
            {
                "question_en": "What feature do many tanks have to prevent surge?",
                "question_es": "¿Qué característica tienen muchas cisternas para evitar el oleaje?",
                "option1_en": "Thermal lining",
                "option1_es": "Revestimiento térmico",
                "option2_en": "Baffles or deflectors",
                "option2_es": "Baffles o deflectores",
                "option3_en": "Interior lights",
                "option3_es": "Luces interiores",
                "correct_option": 2
            },
            {
                "question_en": "What should be especially checked on a tank vehicle before departure?",
                "question_es": "¿Qué debe revisarse especialmente en un vehículo cisterna antes de salir?",
                "option1_en": "Exhaust system",
                "option1_es": "Sistema de escape",
                "option2_en": "Leaks and valves",
                "option2_es": "Fugas y válvulas",
                "option3_en": "Interior lights",
                "option3_es": "Luces interiores",
                "correct_option": 2
            },
            {
                "question_en": "Why is it harder to brake with a partially filled tank?",
                "question_es": "¿Por qué es más difícil frenar con una cisterna llena parcialmente?",
                "option1_en": "Due to total weight",
                "option1_es": "Por el peso total",
                "option2_en": "Due to air pressure",
                "option2_es": "Por la presión de aire",
                "option3_en": "Due to liquid movement",
                "option3_es": "Por el movimiento del líquido",
                "correct_option": 3
            },
            {
                "question_en": "What is a baffle (deflector)?",
                "question_es": "¿Qué es un baffle (deflector)?",
                "option1_en": "A rigid separator inside the tank that controls liquid movement",
                "option1_es": "Un separador rígido dentro del tanque que controla el movimiento del líquido",
                "option2_en": "A type of brake",
                "option2_es": "Un tipo de freno",
                "option3_en": "A liquid level sensor",
                "option3_es": "Un sensor de nivel de líquido",
                "correct_option": 1
            },
            {
                "question_en": "What additional precaution should a driver take when operating a tank?",
                "question_es": "¿Qué precaución adicional debe tomar un conductor al manejar una cisterna?",
                "option1_en": "Use low gear at all times",
                "option1_es": "Usar marcha baja en todo momento",
                "option2_en": "Maintain greater following distance",
                "option2_es": "Mantener mayor distancia de seguimiento",
                "option3_en": "Turn faster",
                "option3_es": "Girar más rápido",
                "correct_option": 2
            },
            {
                "question_en": "Why do tanks have an identification plate?",
                "question_es": "¿Por qué las cisternas tienen una placa de identificación?",
                "option1_en": "To know the type of vehicle",
                "option1_es": "Para saber el tipo de vehículo",
                "option2_en": "To know the maximum volume and type of liquid it can transport",
                "option2_es": "Para saber el volumen máximo y el tipo de líquido que puede transportar",
                "option3_en": "For decoration",
                "option3_es": "Para decoración",
                "correct_option": 2
            },
            {
                "question_en": "What does the data plate attached to the tank indicate?",
                "question_es": "¿Qué indica la placa (data plate) adherida al tanque?",
                "option1_en": "The driver's name",
                "option1_es": "El nombre del conductor",
                "option2_en": "Information about the type of liquid and tank capacity",
                "option2_es": "Información sobre el tipo de líquido y capacidad del tanque",
                "option3_en": "The maximum speed allowed",
                "option3_es": "La velocidad máxima permitida",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if the liquid in the tank begins to splash violently?",
                "question_es": "¿Qué se debe hacer si el líquido en la cisterna comienza a salpicar violentamente?",
                "option1_en": "Brake hard",
                "option1_es": "Frenar de golpe",
                "option2_en": "Accelerate",
                "option2_es": "Acelerar",
                "option3_en": "Brake gently and maintain control",
                "option3_es": "Frenar suavemente y mantener control",
                "correct_option": 3
            },
            {
                "question_en": "What is one of the greatest risks when transporting flammable liquids in a tank?",
                "question_es": "¿Cuál es uno de los mayores riesgos al transportar líquidos inflamables en cisterna?",
                "option1_en": "That it evaporates",
                "option1_es": "Que se evapore",
                "option2_en": "That the tank rusts",
                "option2_es": "Que se oxide el tanque",
                "option3_en": "Explosion or fire",
                "option3_es": "Explosión o incendio",
                "correct_option": 3
            },
            {
                "question_en": "What type of brake can be dangerously used in a tank during a curve?",
                "question_es": "¿Qué tipo de freno puede usarse peligrosamente en una cisterna durante una curva?",
                "option1_en": "Service brake",
                "option1_es": "Freno de servicio",
                "option2_en": "Hand brake",
                "option2_es": "Freno de mano",
                "option3_en": "Engine brake (Jake Brake)",
                "option3_es": "Freno de motor (Jake Brake)",
                "correct_option": 3
            },
            {
                "question_en": "What can excessive filling of the tank cause?",
                "question_es": "¿Qué puede provocar un llenado excesivo de la cisterna?",
                "option1_en": "Improve performance",
                "option1_es": "Mejora del rendimiento",
                "option2_en": "Liquid expansion and spills",
                "option2_es": "Expansión del líquido y derrames",
                "option3_en": "Improve stability",
                "option3_es": "Mejora la estabilidad",
                "correct_option": 2
            },
            {
                "question_en": "What should be done during an inspection at a weigh station with a full tank?",
                "question_es": "¿Qué se debe hacer durante una inspección en una estación de pesaje con un tanque lleno?",
                "option1_en": "Open the valves",
                "option1_es": "Abrir las válvulas",
                "option2_en": "Check air pressure",
                "option2_es": "Verificar la presión del aire",
                "option3_en": "Report the contents and show documentation",
                "option3_es": "Reportar el contenido y mostrar documentación",
                "correct_option": 3
            },
            {
                "question_en": "What class of CDL permit is required to drive a tank?",
                "question_es": "¿Qué clase de permiso CDL se requiere para conducir una cisterna?",
                "option1_en": "Class D",
                "option1_es": "Clase D",
                "option2_en": "Class B with N endorsement",
                "option2_es": "Clase B con endoso N",
                "option3_en": "Only HazMat",
                "option3_es": "Solo HazMat",
                "correct_option": 2
            },
            {
                "question_en": "When is the N endorsement (Tank Vehicle) mandatory?",
                "question_es": "¿Cuándo es obligatorio tener el endoso N (Tank Vehicle)?",
                "option1_en": "Only if the liquid is toxic",
                "option1_es": "Solo si el líquido es tóxico",
                "option2_en": "When transporting liquids or gases in containers of 1,000 gallons or more",
                "option2_es": "Cuando se transportan líquidos o gases en contenedores de 1,000 galones o más",
                "option3_en": "Only if there are multiple compartments",
                "option3_es": "Solo si hay múltiples compartimentos",
                "correct_option": 2
            },
            {
                "question_en": "What can cause a spill in a poorly sealed tank?",
                "question_es": "¿Qué puede causar un derrame en una cisterna mal sellada?",
                "option1_en": "Heat",
                "option1_es": "El calor",
                "option2_en": "Evaporation",
                "option2_es": "La evaporación",
                "option3_en": "Liquid expansion with temperature changes",
                "option3_es": "La expansión del líquido con cambios de temperatura",
                "correct_option": 3
            },
            {
                "question_en": "How can terrain slope affect liquid transport?",
                "question_es": "¿Cómo puede afectar la pendiente del terreno al transportar líquidos?",
                "option1_en": "Increases fuel level",
                "option1_es": "Aumenta el nivel de combustible",
                "option2_en": "Changes the vehicle's center of gravity",
                "option2_es": "Cambia el centro de gravedad del vehículo",
                "option3_en": "Reduces liquid pressure",
                "option3_es": "Reduce la presión del líquido",
                "correct_option": 2
            },
            {
                "question_en": "Why does it take more time to brake a tank than a dry truck?",
                "question_es": "¿Por qué se requiere más tiempo para frenar una cisterna que un camión seco?",
                "option1_en": "Due to additional weight",
                "option1_es": "Por el peso adicional",
                "option2_en": "Due to power steering",
                "option2_es": "Por la dirección asistida",
                "option3_en": "Due to liquid movement pushing forward",
                "option3_es": "Por el movimiento del líquido que empuja hacia adelante",
                "correct_option": 3
            },
            {
                "question_en": "What special precaution should be taken when driving an empty tank?",
                "question_es": "¿Qué precaución especial se debe tener al conducir una cisterna vacía?",
                "option1_en": "None",
                "option1_es": "Ninguna",
                "option2_en": "It can slide more easily because it weighs less",
                "option2_es": "Puede deslizarse más fácilmente porque pesa menos",
                "option3_en": "It can roll over less",
                "option3_es": "Puede volcarse menos",
                "correct_option": 2
            },
            {
                "question_en": "What should the driver do when loading a tank with multiple compartments?",
                "question_es": "¿Qué debe hacer el conductor al cargar una cisterna con varios compartimentos?",
                "option1_en": "Fill only one",
                "option1_es": "Llenar solo uno",
                "option2_en": "Balance weight in all compartments",
                "option2_es": "Equilibrar el peso en todos los compartimentos",
                "option3_en": "Fill from back to front",
                "option3_es": "Llenar de atrás hacia adelante",
                "correct_option": 2
            },
            {
                "question_en": "What does a tank 'without baffles' mean?",
                "question_es": "¿Qué significa un tanque 'sin baffles'?",
                "option1_en": "Faster to fill",
                "option1_es": "Más rápido de llenar",
                "option2_en": "No compartments to reduce surge, requires more careful handling",
                "option2_es": "No tiene compartimentos que reduzcan el oleaje, requiere manejo más cuidadoso",
                "option3_en": "No valves",
                "option3_es": "No tiene válvulas",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if a tank valve drips slightly?",
                "question_es": "¿Qué debe hacer si una válvula del tanque gotea ligeramente?",
                "option1_en": "Ignore it",
                "option1_es": "Ignorarla",
                "option2_en": "Cover it with a rag",
                "option2_es": "Taparla con trapo",
                "option3_en": "Report and repair before driving",
                "option3_es": "Reportar y reparar antes de conducir",
                "correct_option": 3
            },
            {
                "question_en": "What is 'lateral surge' in a tank?",
                "question_es": "¿Qué es el 'oleaje lateral' en una cisterna?",
                "option1_en": "Forward movement of liquid",
                "option1_es": "Movimiento hacia adelante del líquido",
                "option2_en": "Side-to-side movement that can cause rollover",
                "option2_es": "Movimiento de lado a lado, que puede causar vuelco",
                "option3_en": "Engine vibration",
                "option3_es": "Vibración del motor",
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
        print(f"\nSuccessfully added {added_count} new questions to 'Tank'")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
        
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_tank_questions() 