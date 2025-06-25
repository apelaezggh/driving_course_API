from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_school_bus_block1():
    db = SessionLocal()
    try:
        # Find the School Bus topic by ID
        topic = db.query(Topic).filter(Topic.id == 20).first()
        
        if not topic:
            print("Topic ID 20 (Autobús Escolar) not found!")
            return
        
        print(f"Found topic: {topic.name_en} (ID: {topic.id})")
        
        # Questions data for Block 1 (first 15 questions)
        questions_data = [
            {
                "question_en": "What is the main priority of a school bus driver?",
                "question_es": "¿Cuál es la principal prioridad del conductor de autobús escolar?",
                "option1_en": "Arrive on time",
                "option1_es": "Llegar a tiempo",
                "option2_en": "Student safety",
                "option2_es": "La seguridad de los estudiantes",
                "option3_en": "Save fuel",
                "option3_es": "Ahorrar combustible",
                "correct_option": 2
            },
            {
                "question_en": "What should a driver do before crossing a railroad track?",
                "question_es": "¿Qué debe hacer un conductor antes de cruzar una vía del tren?",
                "option1_en": "Look both ways while crossing",
                "option1_es": "Mirar a ambos lados mientras cruza",
                "option2_en": "Stop between 15 and 50 feet before the tracks",
                "option2_es": "Detenerse entre 15 y 50 pies antes de las vías",
                "option3_en": "Honk and accelerate",
                "option3_es": "Tocar la bocina y acelerar",
                "correct_option": 2
            },
            {
                "question_en": "What should be done when stopping on a railroad track with students on board?",
                "question_es": "¿Qué debe hacer al detenerse en una vía del tren con estudiantes a bordo?",
                "option1_en": "Turn off lights and wait",
                "option1_es": "Apagar las luces y esperar",
                "option2_en": "Open the door and driver's window to hear better",
                "option2_es": "Abrir la puerta y la ventana del conductor para escuchar mejor",
                "option3_en": "Change gear quickly",
                "option3_es": "Cambiar de marcha rápido",
                "correct_option": 2
            },
            {
                "question_en": "When should the STOP sign on a school bus be used?",
                "question_es": "¿Cuándo se debe usar la señal de alto (STOP sign) del autobús escolar?",
                "option1_en": "Only on rural roads",
                "option1_es": "Solo en carreteras rurales",
                "option2_en": "When picking up or dropping off students",
                "option2_es": "Cuando se recoge o deja estudiantes",
                "option3_en": "Only if there's traffic",
                "option3_es": "Solo si hay tráfico",
                "correct_option": 2
            },
            {
                "question_en": "What should be checked daily on a school bus?",
                "question_es": "¿Qué debe revisar diariamente en un autobús escolar?",
                "option1_en": "Only fuel level",
                "option1_es": "Solo el nivel de combustible",
                "option2_en": "Brake system, lights, stop sign, doors and emergency",
                "option2_es": "Sistema de frenos, luces, señal de alto, puertas y emergencia",
                "option3_en": "The radio",
                "option3_es": "El radio",
                "correct_option": 2
            },
            {
                "question_en": "When should the amber flashing light on a school bus be used?",
                "question_es": "¿Cuándo debe usarse la luz ámbar intermitente del autobús escolar?",
                "option1_en": "After stopping",
                "option1_es": "Después de detenerse",
                "option2_en": "At least 200 feet before a planned stop",
                "option2_es": "Al menos a 200 pies antes de una parada planificada",
                "option3_en": "While loading students",
                "option3_es": "Mientras se cargan estudiantes",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if a driver ignores the school bus STOP sign?",
                "question_es": "¿Qué debe hacer si un conductor ignora la señal de alto del autobús escolar?",
                "option1_en": "Take note of the vehicle and report it",
                "option1_es": "Tomar nota del vehículo y reportarlo",
                "option2_en": "Yell at the driver",
                "option2_es": "Gritarle al conductor",
                "option3_en": "Ignore it if there was no accident",
                "option3_es": "Ignorarlo si no hubo accidente",
                "correct_option": 1
            },
            {
                "question_en": "What is the correct action when dropping off or picking up students?",
                "question_es": "¿Cuál es la acción correcta al dejar o recoger estudiantes?",
                "option1_en": "Stop anywhere",
                "option1_es": "Detenerse en cualquier lugar",
                "option2_en": "Use warning lights and follow protocol",
                "option2_es": "Usar las luces de advertencia y seguir protocolo",
                "option3_en": "Use only hand signals",
                "option3_es": "Usar solo señales manuales",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if there are students crossing in front of the bus?",
                "question_es": "¿Qué debe hacer si hay estudiantes cruzando frente al autobús?",
                "option1_en": "Honk the horn",
                "option1_es": "Hacer sonar el claxon",
                "option2_en": "Wait until they are completely safe on the other side",
                "option2_es": "Esperar hasta que estén completamente seguros del otro lado",
                "option3_en": "Accelerate slowly",
                "option3_es": "Acelerar lentamente",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if a student drops something in front of the bus?",
                "question_es": "¿Qué debe hacer si un estudiante deja caer algo al frente del autobús?",
                "option1_en": "Help them pick it up immediately",
                "option1_es": "Ayudarlo a recogerlo inmediatamente",
                "option2_en": "Tell them not to pick it up and notify the driver",
                "option2_es": "Indicarle que no lo recoja y avisarle al conductor",
                "option3_en": "Ignore it if there's no traffic",
                "option3_es": "Ignorarlo si no hay tráfico",
                "correct_option": 2
            },
            {
                "question_en": "What is the 'danger blind spot' on a school bus?",
                "question_es": "¿Qué es el 'punto ciego de peligro' en un autobús escolar?",
                "option1_en": "Area in front of the bus that the driver cannot see",
                "option1_es": "Área frente al autobús que el conductor no puede ver",
                "option2_en": "Rear cargo area",
                "option2_es": "Área trasera de carga",
                "option3_en": "Back seats",
                "option3_es": "Asientos del fondo",
                "correct_option": 1
            },
            {
                "question_en": "What should the driver do if a student is in danger while crossing the street?",
                "question_es": "¿Qué debe hacer el conductor si un estudiante está en peligro al cruzar la calle?",
                "option1_en": "Use the horn immediately to alert them",
                "option1_es": "Usar la bocina de inmediato para alertarlo",
                "option2_en": "Wait for them to cross",
                "option2_es": "Esperar a que cruce",
                "option3_en": "Get out of the bus",
                "option3_es": "Salirse del autobús",
                "correct_option": 1
            },
            {
                "question_en": "How many feet should the student be in front of the bus when crossing?",
                "question_es": "¿Cuántos pies debe estar el estudiante frente al autobús al cruzar?",
                "option1_en": "3 feet",
                "option1_es": "3 pies",
                "option2_en": "10 feet",
                "option2_es": "10 pies",
                "option3_en": "20 feet",
                "option3_es": "20 pies",
                "correct_option": 2
            },
            {
                "question_en": "When should the school bus door be closed when dropping off students?",
                "question_es": "¿Cuándo debe cerrar la puerta del autobús escolar al dejar estudiantes?",
                "option1_en": "Immediately when stopping",
                "option1_es": "Inmediatamente al detenerse",
                "option2_en": "Only when moving away from the stop",
                "option2_es": "Solo al alejarse de la parada",
                "option3_en": "Before they get off",
                "option3_es": "Antes de que bajen",
                "correct_option": 2
            },
            {
                "question_en": "What distance should be maintained from a railroad crossing before stopping?",
                "question_es": "¿Qué distancia debe mantenerse desde un cruce de ferrocarril antes de detenerse?",
                "option1_en": "5-10 feet",
                "option1_es": "5-10 pies",
                "option2_en": "15-50 feet",
                "option2_es": "15-50 pies",
                "option3_en": "Right on the track",
                "option3_es": "Justo en la vía",
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
        print(f"\nSuccessfully added {added_count} new questions to 'Autobús Escolar' (Block 1)")
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_school_bus_block1() 