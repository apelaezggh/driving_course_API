from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_hazardous_materials_block2():
    db = SessionLocal()
    try:
        topic = db.query(Topic).filter(Topic.id == 16).first()
        if not topic:
            print("Topic ID 16 (Materiales Peligrosos) not found!")
            return
        print(f"Found topic: {topic.name_es} (ID: {topic.id})")
        questions_data = [
            {"question_en": "Who can open a hazardous materials shipment?", "question_es": "¿Quién puede abrir un envío de materiales peligrosos?", "option1_en": "Any supervisor", "option1_es": "Cualquier supervisor", "option2_en": "Only trained personnel", "option2_es": "Solamente personal capacitado", "option3_en": "Any driver with CDL license", "option3_es": "Cualquier conductor con licencia CDL", "correct_option": 2},
            {"question_en": "What class covers flammable gases?", "question_es": "¿Qué clase cubre gases inflamables?", "option1_en": "Class 2", "option1_es": "Clase 2", "option2_en": "Class 3", "option2_es": "Clase 3", "option3_en": "Class 6", "option3_es": "Clase 6", "correct_option": 1},
            {"question_en": "What should the driver do if transporting hazardous materials and stopped by police?", "question_es": "¿Qué debe hacer el conductor si transporta materiales peligrosos y es detenido por la policía?", "option1_en": "Keep hands on the steering wheel", "option1_es": "Mantener las manos en el volante", "option2_en": "Show HazMat shipping documents", "option2_es": "Mostrar los documentos de envío HazMat", "option3_en": "Remain silent", "option3_es": "Guardar silencio", "correct_option": 2},
            {"question_en": "What type of materials belong to Class 7?", "question_es": "¿Qué tipo de materiales pertenecen a la Clase 7?", "option1_en": "Explosives", "option1_es": "Explosivos", "option2_en": "Radioactive materials", "option2_es": "Materiales radioactivos", "option3_en": "Toxic gases", "option3_es": "Gases tóxicos", "correct_option": 2},
            {"question_en": "What does a green label on a container mean?", "question_es": "¿Qué significa una etiqueta verde en un contenedor?", "option1_en": "Non-flammable gas", "option1_es": "Gas no inflamable", "option2_en": "Flammable liquid", "option2_es": "Líquido inflamable", "option3_en": "Corrosive substance", "option3_es": "Sustancia corrosiva", "correct_option": 1},
            {"question_en": "Where should the warning diamond be placed on a vehicle?", "question_es": "¿Dónde se debe colocar el rombo de advertencia en un vehículo?", "option1_en": "Only in the back", "option1_es": "Solo atrás", "option2_en": "On the sides", "option2_es": "A los lados", "option3_en": "Front, back and both sides", "option3_es": "Adelante, atrás y ambos lados", "correct_option": 3},
            {"question_en": "What can cause penalties or fines when transporting hazardous materials?", "question_es": "¿Qué puede causar sanciones o multas al transportar materiales peligrosos?", "option1_en": "Not having insurance", "option1_es": "No llevar seguro", "option2_en": "Not carrying the HazMat permit", "option2_es": "No portar el permiso HazMat", "option3_en": "Using turn signals late", "option3_es": "Usar señales de giro tarde", "correct_option": 2},
            {"question_en": "What document specifies how to respond to a hazardous materials emergency?", "question_es": "¿Qué documento especifica cómo responder a una emergencia con materiales peligrosos?", "option1_en": "Driver's manual", "option1_es": "Manual del conductor", "option2_en": "Emergency response guide (ERG)", "option2_es": "Guía de emergencia (ERG)", "option3_en": "Payroll sheet", "option3_es": "Hoja de salario", "correct_option": 2},
            {"question_en": "What happens if hazardous materials labels are not used correctly?", "question_es": "¿Qué pasa si no se usan correctamente las etiquetas de materiales peligrosos?", "option1_en": "No consequences", "option1_es": "No tiene consecuencias", "option2_en": "Can result in fines and serious risks", "option2_es": "Puede resultar en multas y riesgos graves", "option3_en": "Only the shipper is penalized", "option3_es": "Solo se sanciona al embarcador", "correct_option": 2},
            {"question_en": "What is the best way to identify a hazardous material?", "question_es": "¿Cuál es la mejor manera de identificar un material peligroso?", "option1_en": "By the color of the truck", "option1_es": "Por el color del camión", "option2_en": "By the identification number on the label", "option2_es": "Por el número de identificación en la etiqueta", "option3_en": "By the weight of the package", "option3_es": "Por el peso del paquete", "correct_option": 2}
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
        print(f"\nSuccessfully added {added_count} new questions to 'Materiales Peligrosos' (Block 2)")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_hazardous_materials_block2() 