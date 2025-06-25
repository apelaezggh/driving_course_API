from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_hazardous_materials_block3():
    db = SessionLocal()
    try:
        # Find the Hazardous Materials topic by ID
        topic = db.query(Topic).filter(Topic.id == 16).first()
        
        if not topic:
            print("Topic ID 16 (Materiales Peligrosos) not found!")
            return
        
        print(f"Found topic: {topic.name_en} (ID: {topic.id})")
        
        # Questions data for Block 3 (10 additional questions)
        questions_data = [
            {
                "question_en": "What should the driver verify before starting with a hazardous materials load?",
                "question_es": "¿Qué debe verificar el conductor antes de arrancar con una carga de materiales peligrosos?",
                "option1_en": "That the radio works correctly",
                "option1_es": "Que la radio funcione correctamente",
                "option2_en": "That the vehicle has fuel",
                "option2_es": "Que el vehículo tenga combustible",
                "option3_en": "That the placards are correctly placed and visible",
                "option3_es": "Que los rótulos (placards) estén correctamente colocados y visibles",
                "correct_option": 3
            },
            {
                "question_en": "What does a label with a yellow background mean?",
                "question_es": "¿Qué significa una etiqueta con un fondo amarillo?",
                "option1_en": "Explosives",
                "option1_es": "Explosivos",
                "option2_en": "Oxidizing material",
                "option2_es": "Material oxidante",
                "option3_en": "Toxic substance",
                "option3_es": "Sustancia tóxica",
                "correct_option": 2
            },
            {
                "question_en": "What is the function of the Emergency Response Guidebook (ERG)?",
                "question_es": "¿Cuál es la función del Emergency Response Guidebook (ERG)?",
                "option1_en": "Calculate salary per mile",
                "option1_es": "Calcular el salario por milla",
                "option2_en": "Indicate the fastest routes",
                "option2_es": "Indicar las rutas más rápidas",
                "option3_en": "Provide procedures in case of hazardous materials incidents",
                "option3_es": "Proporcionar procedimientos en caso de incidentes con materiales peligrosos",
                "correct_option": 3
            },
            {
                "question_en": "What should be done if transporting a HazMat load and noticing a strange odor or leak?",
                "question_es": "¿Qué debe hacer si transporta una carga HazMat y nota un olor extraño o fuga?",
                "option1_en": "Continue if there's no smoke",
                "option1_es": "Continuar si no hay humo",
                "option2_en": "Stop immediately and follow emergency procedures",
                "option2_es": "Detenerse de inmediato y seguir los procedimientos de emergencia",
                "option3_en": "Open the compartment and ventilate it",
                "option3_es": "Abrir el compartimento y ventilarlo",
                "correct_option": 2
            },
            {
                "question_en": "When is an escort or prior notification needed to transport hazardous materials?",
                "question_es": "¿Cuándo se necesita un escolta o notificación previa para transportar materiales peligrosos?",
                "option1_en": "When transporting on rural roads",
                "option1_es": "Cuando transporta en carreteras rurales",
                "option2_en": "Only if the vehicle has more than 3 axles",
                "option2_es": "Solo si el vehículo tiene más de 3 ejes",
                "option3_en": "When required by federal or state regulations",
                "option3_es": "Cuando así lo exigen las regulaciones federales o estatales",
                "correct_option": 3
            },
            {
                "question_en": "What does the number 6 mean in hazardous materials classification?",
                "question_es": "¿Qué significa el número 6 en la clasificación de materiales peligrosos?",
                "option1_en": "Corrosive material",
                "option1_es": "Material corrosivo",
                "option2_en": "Toxic or infectious material",
                "option2_es": "Material tóxico o infeccioso",
                "option3_en": "Flammable gas",
                "option3_es": "Gas inflamable",
                "correct_option": 2
            },
            {
                "question_en": "What action is prohibited when transporting hazardous materials?",
                "question_es": "¿Qué acción está prohibida cuando se transportan materiales peligrosos?",
                "option1_en": "Smoking near the vehicle",
                "option1_es": "Fumar cerca del vehículo",
                "option2_en": "Using gloves",
                "option2_es": "Usar guantes",
                "option3_en": "Talking on radio with other drivers",
                "option3_es": "Hablar por radio con otros conductores",
                "correct_option": 1
            },
            {
                "question_en": "What should the shipping documents contain when transporting HazMat?",
                "question_es": "¿Qué debe contener el envío de documentos al transportar HazMat?",
                "option1_en": "Driver's name",
                "option1_es": "Nombre del conductor",
                "option2_en": "Vehicle fuel type",
                "option2_es": "Tipo de combustible del vehículo",
                "option3_en": "Proper name of the material, class and identification number",
                "option3_es": "Nombre propio del material, clase y número de identificación",
                "correct_option": 3
            },
            {
                "question_en": "What should be done if you're not sure how to handle a hazardous material?",
                "question_es": "¿Qué se debe hacer si no estás seguro de cómo manejar un material peligroso?",
                "option1_en": "Transport it and resolve later",
                "option1_es": "Transportarlo y resolver luego",
                "option2_en": "Call dispatch",
                "option2_es": "Llamar al despacho",
                "option3_en": "Consult the ERG and notify the supervisor before moving it",
                "option3_es": "Consultar el ERG y notificar al supervisor antes de moverlo",
                "correct_option": 3
            },
            {
                "question_en": "What is the maximum fine for transporting hazardous materials without permission or incorrectly?",
                "question_es": "¿Cuál es la multa máxima por transportar materiales peligrosos sin permiso o de manera incorrecta?",
                "option1_en": "$500",
                "option1_es": "$500",
                "option2_en": "$5,000",
                "option2_es": "$5,000",
                "option3_en": "More than $75,000",
                "option3_es": "Más de $75,000",
                "correct_option": 3
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
        print(f"\nSuccessfully added {added_count} new questions to 'Materiales Peligrosos' (Block 3)")
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_hazardous_materials_block3() 