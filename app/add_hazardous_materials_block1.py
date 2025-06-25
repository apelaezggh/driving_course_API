from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_hazardous_materials_block1():
    db = SessionLocal()
    try:
        topic = db.query(Topic).filter(Topic.id == 16).first()
        if not topic:
            print("Topic ID 16 (Materiales Peligrosos) not found!")
            return
        print(f"Found topic: {topic.name_es} (ID: {topic.id})")
        questions_data = [
            {"question_en": "What does an identification number (ID) indicate on a hazardous materials shipment?", "question_es": "¿Qué indica un número de identificación (ID) en una carga de materiales peligrosos?", "option1_en": "The driver's number", "option1_es": "El número del conductor", "option2_en": "The specific type of material being transported", "option2_es": "El tipo específico de material transportado", "option3_en": "The maximum speed allowed", "option3_es": "La velocidad máxima permitida", "correct_option": 2},
            {"question_en": "Where should the emergency response information (shipping papers) be placed?", "question_es": "¿Dónde se debe colocar la hoja de datos de emergencia (shipping papers)?", "option1_en": "In the engine compartment", "option1_es": "En el compartimento del motor", "option2_en": "Within reach of the driver in the cab", "option2_es": "Al alcance del conductor en la cabina", "option3_en": "In the trailer", "option3_es": "En el remolque", "correct_option": 2},
            {"question_en": "What does the red diamond on a hazardous materials label mean?", "question_es": "¿Qué significa el rombo rojo en una etiqueta de materiales peligrosos?", "option1_en": "Poisonous substances", "option1_es": "Sustancias venenosas", "option2_en": "Flammable liquids", "option2_es": "Líquidos inflamables", "option3_en": "Explosives", "option3_es": "Explosivos", "correct_option": 2},
            {"question_en": "Who is responsible for classifying a material as hazardous?", "question_es": "¿Quién es responsable de clasificar un material como peligroso?", "option1_en": "The carrier", "option1_es": "El transportista", "option2_en": "The driver", "option2_es": "El conductor", "option3_en": "The shipper", "option3_es": "El embarcador", "correct_option": 3},
            {"question_en": "What should the driver do if involved in an accident with hazardous materials?", "question_es": "¿Qué debe hacer el conductor si se involucra en un accidente con materiales peligrosos?", "option1_en": "Abandon the vehicle", "option1_es": "Abandonar el vehículo", "option2_en": "Protect the area and notify authorities", "option2_es": "Proteger el área y notificar a las autoridades", "option3_en": "Unload the material quickly", "option3_es": "Descargar el material rápidamente", "correct_option": 2},
            {"question_en": "How many warning labels (placards) are normally required on a vehicle transporting hazardous materials?", "question_es": "¿Cuántas etiquetas de advertencia (placards) se requieren normalmente en un vehículo que transporta materiales peligrosos?", "option1_en": "2", "option1_es": "2", "option2_en": "4", "option2_es": "4", "option3_en": "1", "option3_es": "1", "correct_option": 2},
            {"question_en": "What color label indicates explosive material?", "question_es": "¿Qué color de etiqueta indica material explosivo?", "option1_en": "Orange", "option1_es": "Naranja", "option2_en": "Blue", "option2_es": "Azul", "option3_en": "Green", "option3_es": "Verde", "correct_option": 1},
            {"question_en": "What document must the driver have when transporting hazardous materials?", "question_es": "¿Qué documento debe tener el conductor al transportar materiales peligrosos?", "option1_en": "A commercial invoice", "option1_es": "Una factura comercial", "option2_en": "A medical license", "option2_es": "Una licencia médica", "option3_en": "A hazardous materials permit (HazMat endorsement)", "option3_es": "Un permiso de materiales peligrosos (HazMat endorsement)", "correct_option": 3},
            {"question_en": "What type of materials require the use of gloves and special protection when handling?", "question_es": "¿Qué tipo de materiales requieren el uso de guantes y protección especial al manejar?", "option1_en": "Explosives", "option1_es": "Explosivos", "option2_en": "Corrosive materials", "option2_es": "Materiales corrosivos", "option3_en": "Frozen foods", "option3_es": "Alimentos congelados", "correct_option": 2},
            {"question_en": "What does the number 1 on a hazardous material class label mean?", "question_es": "¿Qué significa el número 1 en una etiqueta de clase de material peligroso?", "option1_en": "Poisonous material", "option1_es": "Material venenoso", "option2_en": "Explosive material", "option2_es": "Material explosivo", "option3_en": "Compressed gas", "option3_es": "Gas comprimido", "correct_option": 2},
            {"question_en": "What should be done before loading hazardous materials?", "question_es": "¿Qué se debe hacer antes de cargar materiales peligrosos?", "option1_en": "Sign the receipt", "option1_es": "Firmar el recibo", "option2_en": "Inspect the vehicle", "option2_es": "Inspeccionar el vehículo", "option3_en": "Fill the fuel tank", "option3_es": "Llenar el tanque de combustible", "correct_option": 2},
            {"question_en": "What does a white label with skull and crossbones mean?", "question_es": "¿Qué significa una etiqueta blanca con calavera y tibias cruzadas?", "option1_en": "Radioactive material", "option1_es": "Material radioactivo", "option2_en": "Flammable gas", "option2_es": "Gas inflamable", "option3_en": "Poison or toxic material", "option3_es": "Veneno o material tóxico", "correct_option": 3},
            {"question_en": "Which class of materials is most sensitive to heat or friction?", "question_es": "¿Qué clase de materiales es la más sensible al calor o fricción?", "option1_en": "Class 1 – Explosives", "option1_es": "Clase 1 – Explosivos", "option2_en": "Class 4 – Flammable solids", "option2_es": "Clase 4 – Sólidos inflamables", "option3_en": "Class 9 – Miscellaneous", "option3_es": "Clase 9 – Misceláneos", "correct_option": 1},
            {"question_en": "What does a white and black background label with vertical stripes indicate?", "question_es": "¿Qué indica una etiqueta de fondo blanco y negro con franjas verticales?", "option1_en": "Corrosive", "option1_es": "Corrosivo", "option2_en": "Radioactive", "option2_es": "Radioactivo", "option3_en": "Flammable liquid", "option3_es": "Líquido inflamable", "correct_option": 1},
            {"question_en": "What should the driver do if there is a leak of hazardous materials?", "question_es": "¿Qué debe hacer el conductor si hay una fuga de materiales peligrosos?", "option1_en": "Clean the leak", "option1_es": "Limpiar la fuga", "option2_en": "Ignore it if it's small", "option2_es": "Ignorarla si es pequeña", "option3_en": "Stop and report immediately", "option3_es": "Detenerse y reportar inmediatamente", "correct_option": 3}
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
        print(f"\nSuccessfully added {added_count} new questions to 'Materiales Peligrosos' (Block 1)")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_hazardous_materials_block1() 