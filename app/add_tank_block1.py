from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_tank_block1():
    db = SessionLocal()
    try:
        topic = db.query(Topic).filter(Topic.id == 17).first()
        if not topic:
            print("Topic ID 17 (Cisterna) not found!")
            return
        print(f"Found topic: {topic.name_es} (ID: {topic.id})")
        questions_data = [
            {"question_en": "What effect can the movement of liquid inside a tank cause during driving?", "question_es": "¿Qué efecto puede causar el movimiento del líquido dentro de una cisterna durante la conducción?", "option1_en": "Speed reduction", "option1_es": "Reducción de velocidad", "option2_en": "Loss of traction", "option2_es": "Pérdida de tracción", "option3_en": "Surge, affecting vehicle control", "option3_es": "Oleaje (surge), afectando el control del vehículo", "correct_option": 3},
            {"question_en": "What type of liquid is most dangerous to transport due to its movement?", "question_es": "¿Qué tipo de líquido es más peligroso de transportar por su movimiento?", "option1_en": "Frozen liquid", "option1_es": "Líquido congelado", "option2_en": "Very dense liquid", "option2_es": "Líquido muy denso", "option3_en": "Partially filled liquid", "option3_es": "Líquido parcialmente lleno", "correct_option": 3},
            {"question_en": "What should the driver do to control surge?", "question_es": "¿Qué debe hacer el conductor para controlar el oleaje (surge)?", "option1_en": "Accelerate when turning", "option1_es": "Acelerar al girar", "option2_en": "Brake smoothly", "option2_es": "Frenar suavemente", "option3_en": "Brake abruptly", "option3_es": "Frenar bruscamente", "correct_option": 2},
            {"question_en": "What feature do many tanks have to prevent surge?", "question_es": "¿Qué característica tienen muchas cisternas para evitar el oleaje?", "option1_en": "Thermal lining", "option1_es": "Revestimiento térmico", "option2_en": "Baffles or deflectors", "option2_es": "Baffles o deflectores", "option3_en": "Interior lights", "option3_es": "Luces interiores", "correct_option": 2},
            {"question_en": "What should be especially checked in a tank vehicle before departure?", "question_es": "¿Qué debe revisarse especialmente en un vehículo cisterna antes de salir?", "option1_en": "Exhaust system", "option1_es": "Sistema de escape", "option2_en": "Leaks and valves", "option2_es": "Fugas y válvulas", "option3_en": "Interior lights", "option3_es": "Luces interiores", "correct_option": 2},
            {"question_en": "Why is it more difficult to brake with a partially filled tank?", "question_es": "¿Por qué es más difícil frenar con una cisterna llena parcialmente?", "option1_en": "Due to total weight", "option1_es": "Por el peso total", "option2_en": "Due to air pressure", "option2_es": "Por la presión de aire", "option3_en": "Due to liquid movement", "option3_es": "Por el movimiento del líquido", "correct_option": 3},
            {"question_en": "What is a baffle (deflector)?", "question_es": "¿Qué es un baffle (deflector)?", "option1_en": "A rigid separator inside the tank that controls liquid movement", "option1_es": "Un separador rígido dentro del tanque que controla el movimiento del líquido", "option2_en": "A type of brake", "option2_es": "Un tipo de freno", "option3_en": "A liquid level sensor", "option3_es": "Un sensor de nivel de líquido", "correct_option": 1},
            {"question_en": "What additional precaution should a driver take when driving a tank?", "question_es": "¿Qué precaución adicional debe tomar un conductor al manejar una cisterna?", "option1_en": "Use low gear at all times", "option1_es": "Usar marcha baja en todo momento", "option2_en": "Maintain greater following distance", "option2_es": "Mantener mayor distancia de seguimiento", "option3_en": "Turn faster", "option3_es": "Girar más rápido", "correct_option": 2},
            {"question_en": "Why do tanks have an identification plate?", "question_es": "¿Por qué las cisternas tienen una placa de identificación?", "option1_en": "To know the type of vehicle", "option1_es": "Para saber el tipo de vehículo", "option2_en": "To know the maximum volume and type of liquid it can transport", "option2_es": "Para saber el volumen máximo y el tipo de líquido que puede transportar", "option3_en": "For decoration", "option3_es": "Para decoración", "correct_option": 2},
            {"question_en": "What does the data plate attached to the tank indicate?", "question_es": "¿Qué indica la placa (data plate) adherida al tanque?", "option1_en": "The driver's name", "option1_es": "El nombre del conductor", "option2_en": "Information about the type of liquid and tank capacity", "option2_es": "Información sobre el tipo de líquido y capacidad del tanque", "option3_en": "The maximum allowed speed", "option3_es": "La velocidad máxima permitida", "correct_option": 2},
            {"question_en": "What should be done if the liquid in the tank starts to splash violently?", "question_es": "¿Qué se debe hacer si el líquido en la cisterna comienza a salpicar violentamente?", "option1_en": "Brake hard", "option1_es": "Frenar de golpe", "option2_en": "Accelerate", "option2_es": "Acelerar", "option3_en": "Brake smoothly and maintain control", "option3_es": "Frenar suavemente y mantener control", "correct_option": 3},
            {"question_en": "What is one of the greatest risks when transporting flammable liquids in a tank?", "question_es": "¿Cuál es uno de los mayores riesgos al transportar líquidos inflamables en cisterna?", "option1_en": "That it evaporates", "option1_es": "Que se evapore", "option2_en": "That the tank rusts", "option2_es": "Que se oxide el tanque", "option3_en": "Explosion or fire", "option3_es": "Explosión o incendio", "correct_option": 3},
            {"question_en": "What type of brake can be dangerously used in a tank during a curve?", "question_es": "¿Qué tipo de freno puede usarse peligrosamente en una cisterna durante una curva?", "option1_en": "Service brake", "option1_es": "Freno de servicio", "option2_en": "Hand brake", "option2_es": "Freno de mano", "option3_en": "Engine brake (Jake Brake)", "option3_es": "Freno de motor (Jake Brake)", "correct_option": 3},
            {"question_en": "What can overfilling the tank cause?", "question_es": "¿Qué puede provocar un llenado excesivo de la cisterna?", "option1_en": "Improved performance", "option1_es": "Mejora del rendimiento", "option2_en": "Expansion of liquid and spills", "option2_es": "Expansión del líquido y derrames", "option3_en": "Improves stability", "option3_es": "Mejora la estabilidad", "correct_option": 2},
            {"question_en": "What should be done during an inspection at a weigh station with a full tank?", "question_es": "¿Qué se debe hacer durante una inspección en una estación de pesaje con un tanque lleno?", "option1_en": "Open the valves", "option1_es": "Abrir las válvulas", "option2_en": "Check air pressure", "option2_es": "Verificar la presión del aire", "option3_en": "Report the contents and show documentation", "option3_es": "Reportar el contenido y mostrar documentación", "correct_option": 3}
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
        print(f"\nSuccessfully added {added_count} new questions to 'Cisterna' (Block 1)")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_tank_block1() 