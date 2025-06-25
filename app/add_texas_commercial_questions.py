from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Question, Topic

def add_texas_commercial_questions():
    db = SessionLocal()
    
    try:
        # Get the Texas Commercial Vehicle Operation topic
        topic = db.query(Topic).filter(Topic.name_en == "Texas Commercial Vehicle Operation").first()
        if not topic:
            print("❌ Topic 'Texas Commercial Vehicle Operation' not found!")
            return
        
        print(f"✅ Found topic: {topic.name_en} (ID: {topic.id})")
        
        # Define the questions
        questions = [
            {
                "question_en": "To which authority must commercial drivers report serious accidents in Texas?",
                "question_es": "¿A qué autoridad deben reportarse los conductores comerciales en Texas tras un accidente grave?",
                "option1_en": "Interstate Department of Transportation",
                "option1_es": "Departamento de Transporte Interestatal",
                "option2_en": "Texas Department of Public Safety (DPS)",
                "option2_es": "Departamento de Seguridad Pública de Texas (DPS)",
                "option3_en": "Federal Court",
                "option3_es": "Tribunal Federal",
                "correct_option": 2
            },
            {
                "question_en": "What is the maximum blood alcohol concentration (BAC) allowed for commercial drivers in Texas?",
                "question_es": "¿Cuál es el nivel máximo permitido de alcohol en sangre (BAC) para conductores comerciales en Texas?",
                "option1_en": "0.08%",
                "option1_es": "0.08%",
                "option2_en": "0.04%",
                "option2_es": "0.04%",
                "option3_en": "0.02%",
                "option3_es": "0.02%",
                "correct_option": 2
            },
            {
                "question_en": "How many hours can a commercial driver drive in a 24-hour period according to federal laws adopted by Texas?",
                "question_es": "¿Cuántas horas puede conducir un conductor comercial en un período de 24 horas según las leyes federales adoptadas por Texas?",
                "option1_en": "10 hours",
                "option1_es": "10 horas",
                "option2_en": "12 hours",
                "option2_es": "12 horas",
                "option3_en": "14 hours",
                "option3_es": "14 horas",
                "correct_option": 1
            },
            {
                "question_en": "What type of license is required to drive a vehicle over 26,001 pounds in Texas?",
                "question_es": "¿Qué tipo de licencia se requiere para manejar un vehículo de más de 26,001 libras en Texas?",
                "option1_en": "Class B",
                "option1_es": "Clase B",
                "option2_en": "Class C",
                "option2_es": "Clase C",
                "option3_en": "Class A",
                "option3_es": "Clase A",
                "correct_option": 1
            },
            {
                "question_en": "When must a driver carry their DOT medical card in Texas?",
                "question_es": "¿Cuándo debe un conductor portar su tarjeta médica del DOT en Texas?",
                "option1_en": "Only on interstate trips",
                "option1_es": "Solo en viajes interestatales",
                "option2_en": "Whenever driving a commercial vehicle",
                "option2_es": "Siempre que conduzca un vehículo comercial",
                "option3_en": "Only during inspections",
                "option3_es": "Solo durante inspecciones",
                "correct_option": 2
            },
            {
                "question_en": "What information must be in a commercial vehicle maintenance record?",
                "question_es": "¿Qué información debe tener el registro de mantenimiento de un vehículo comercial?",
                "option1_en": "Date and time of trip",
                "option1_es": "Fecha y hora del viaje",
                "option2_en": "Repairs, inspections and maintenance performed",
                "option2_es": "Reparaciones, inspecciones y mantenimiento realizados",
                "option3_en": "Number of passengers transported",
                "option3_es": "Número de pasajeros transportados",
                "correct_option": 2
            },
            {
                "question_en": "What is the maximum speed for commercial vehicles on Texas highways (unless otherwise posted)?",
                "question_es": "¿Cuál es la velocidad máxima para vehículos comerciales en autopistas de Texas (salvo señalización)?",
                "option1_en": "60 mph",
                "option1_es": "60 mph",
                "option2_en": "65 mph",
                "option2_es": "65 mph",
                "option3_en": "70 mph (may vary by road type and load)",
                "option3_es": "70 mph (puede variar por tipo de vía y carga)",
                "correct_option": 3
            },
            {
                "question_en": "What should the driver do if a DPS officer requests a vehicle inspection?",
                "question_es": "¿Qué debe hacer el conductor si un oficial de DPS solicita una inspección del vehículo?",
                "option1_en": "Refuse if running late",
                "option1_es": "Negarse si va retrasado",
                "option2_en": "Allow the inspection",
                "option2_es": "Permitir la inspección",
                "option3_en": "Only show license",
                "option3_es": "Solo mostrar licencia",
                "correct_option": 2
            },
            {
                "question_en": "What penalty can a driver receive if they refuse an alcohol test in Texas?",
                "question_es": "¿Qué sanción puede recibir un conductor si se niega a una prueba de alcohol en Texas?",
                "option1_en": "Fine and points",
                "option1_es": "Multa y puntos",
                "option2_en": "Automatic license suspension",
                "option2_es": "Suspensión automática de la licencia",
                "option3_en": "Warning only",
                "option3_es": "Solo advertencia",
                "correct_option": 2
            },
            {
                "question_en": "How long must the hours record (logbook) be kept?",
                "question_es": "¿Cuánto tiempo debe mantenerse el registro de horas (logbook)?",
                "option1_en": "1 month",
                "option1_es": "1 mes",
                "option2_en": "7 days",
                "option2_es": "7 días",
                "option3_en": "8 days minimum",
                "option3_es": "8 días como mínimo",
                "correct_option": 3
            },
            {
                "question_en": "Who regulates commercial cargo transportation in Texas?",
                "question_es": "¿Quién regula el transporte de carga comercial en Texas?",
                "option1_en": "Department of Treasury",
                "option1_es": "Departamento de Hacienda",
                "option2_en": "Texas Department of Transportation (TxDOT)",
                "option2_es": "Departamento de Transporte de Texas (TxDOT)",
                "option3_en": "National Guard",
                "option3_es": "Guardia Nacional",
                "correct_option": 2
            },
            {
                "question_en": "What does a red plate with numbers on a commercial vehicle mean?",
                "question_es": "¿Qué significa una placa roja con números en un vehículo comercial?",
                "option1_en": "Temporary permit",
                "option1_es": "Permiso temporal",
                "option2_en": "Hazardous materials cargo",
                "option2_es": "Carga de materiales peligrosos",
                "option3_en": "Additional weight",
                "option3_es": "Peso adicional",
                "correct_option": 2
            },
            {
                "question_en": "When is a HazMat Endorsement required in Texas?",
                "question_es": "¿Cuándo se requiere un Endoso HazMat en Texas?",
                "option1_en": "Whenever liquids are transported",
                "option1_es": "Siempre que se transporten líquidos",
                "option2_en": "Only for international cargo",
                "option2_es": "Solo para carga internacional",
                "option3_en": "When transporting regulated hazardous materials",
                "option3_es": "Cuando se transportan materiales peligrosos regulados",
                "correct_option": 3
            },
            {
                "question_en": "What should a driver do before climbing a steep hill?",
                "question_es": "¿Qué debe hacer un conductor antes de subir una pendiente empinada?",
                "option1_en": "Accelerate to maximum",
                "option1_es": "Acelerar al máximo",
                "option2_en": "Downshift and prepare to control speed",
                "option2_es": "Reducir la marcha y prepararse para controlar la velocidad",
                "option3_en": "Uncouple the trailer",
                "option3_es": "Desacoplar el remolque",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if a commercial vehicle partially blocks a highway?",
                "question_es": "¿Qué se debe hacer si un vehículo comercial bloquea parcialmente una carretera?",
                "option1_en": "Call by phone",
                "option1_es": "Avisar por teléfono",
                "option2_en": "Place warning triangles at 10, 100 and 200 feet",
                "option2_es": "Colocar triángulos de advertencia en 10, 100 y 200 pies",
                "option3_en": "Turn on high beams",
                "option3_es": "Encender luces largas",
                "correct_option": 2
            },
            {
                "question_en": "What does the 'No Trucks' sign on some roads indicate?",
                "question_es": "¿Qué indica el letrero 'No Trucks' en algunas carreteras?",
                "option1_en": "That trucks must brake",
                "option1_es": "Que los camiones deben frenar",
                "option2_en": "That commercial vehicles are prohibited from passing",
                "option2_es": "Que está prohibido el paso a vehículos comerciales",
                "option3_en": "That there is a dangerous curve",
                "option3_es": "Que hay curva peligrosa",
                "correct_option": 2
            },
            {
                "question_en": "What does the term 'Gross Vehicle Weight Rating (GVWR)' mean?",
                "question_es": "¿Qué significa el término 'Gross Vehicle Weight Rating (GVWR)'?",
                "option1_en": "Net vehicle weight",
                "option1_es": "Peso neto del vehículo",
                "option2_en": "Maximum weight a vehicle can weigh with cargo",
                "option2_es": "Peso máximo que puede pesar un vehículo con carga",
                "option3_en": "Engine weight",
                "option3_es": "Peso del motor",
                "correct_option": 2
            },
            {
                "question_en": "What is the minimum distance to signal a stopped vehicle on a two-way highway?",
                "question_es": "¿Cuál es la distancia mínima para señalizar un vehículo detenido en carretera de dos vías?",
                "option1_en": "50 feet",
                "option1_es": "50 pies",
                "option2_en": "100 feet",
                "option2_es": "100 pies",
                "option3_en": "25 feet",
                "option3_es": "25 pies",
                "correct_option": 2
            },
            {
                "question_en": "What should a driver do if the parking brake doesn't work?",
                "question_es": "¿Qué debe hacer un conductor si el freno de estacionamiento no funciona?",
                "option1_en": "Do not drive the vehicle",
                "option1_es": "No conducir el vehículo",
                "option2_en": "Accelerate slowly",
                "option2_es": "Acelerar despacio",
                "option3_en": "Brake with the engine",
                "option3_es": "Frenar con el motor",
                "correct_option": 1
            },
            {
                "question_en": "What sign warns about restrictions for long or tall vehicles?",
                "question_es": "¿Qué señal advierte sobre restricciones para vehículos largos o altos?",
                "option1_en": "No parking",
                "option1_es": "Prohibido estacionar",
                "option2_en": "Maximum height or length allowed",
                "option2_es": "Altura o longitud máxima permitida",
                "option3_en": "Trucks only",
                "option3_es": "Solo camiones",
                "correct_option": 2
            },
            {
                "question_en": "What is the penalty for not stopping at a mandatory railroad crossing?",
                "question_es": "¿Cuál es la sanción por no detenerse en un cruce ferroviario obligatorio?",
                "option1_en": "Warning",
                "option1_es": "Advertencia",
                "option2_en": "Fine and license suspension",
                "option2_es": "Multa y suspensión de licencia",
                "option3_en": "Minor citation",
                "option3_es": "Citación menor",
                "correct_option": 2
            },
            {
                "question_en": "When must a commercial vehicle be inspected in Texas?",
                "question_es": "¿Cuándo debe inspeccionarse un vehículo comercial en Texas?",
                "option1_en": "Only at the beginning of the month",
                "option1_es": "Solo al inicio del mes",
                "option2_en": "Before each trip",
                "option2_es": "Antes de cada viaje",
                "option3_en": "At the end of the day",
                "option3_es": "Al terminar el día",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if the driver sees a crack in a wheel?",
                "question_es": "¿Qué debe hacerse si el conductor ve una grieta en una rueda?",
                "option1_en": "Continue the trip",
                "option1_es": "Continuar el viaje",
                "option2_en": "Stop the vehicle and report the failure",
                "option2_es": "Detener el vehículo y reportar la falla",
                "option3_en": "Brake harder",
                "option3_es": "Frenar con más fuerza",
                "correct_option": 2
            },
            {
                "question_en": "What is an IRP permit in Texas?",
                "question_es": "¿Qué es un permiso IRP en Texas?",
                "option1_en": "Permit to operate outside hours",
                "option1_es": "Permiso para operar fuera de horario",
                "option2_en": "International Registration Plan for Commercial Vehicles",
                "option2_es": "Registro Internacional de Vehículos Comerciales",
                "option3_en": "Temporary license",
                "option3_es": "Licencia temporal",
                "correct_option": 2
            },
            {
                "question_en": "What documents must always be carried in a commercial vehicle?",
                "question_es": "¿Qué documentos deben portarse siempre en un vehículo comercial?",
                "option1_en": "License and music",
                "option1_es": "Licencia y música",
                "option2_en": "License, registration, insurance and necessary permits",
                "option2_es": "Licencia, registro, seguro y permisos necesarios",
                "option3_en": "Gas receipt",
                "option3_es": "Recibo de gasolina",
                "correct_option": 2
            },
            {
                "question_en": "What does the acronym CDL mean?",
                "question_es": "¿Qué significa el acrónimo CDL?",
                "option1_en": "Certified Driving License",
                "option1_es": "Licencia de Conducción Certificada",
                "option2_en": "Commercial Driver License",
                "option2_es": "Licencia de Conductor Comercial",
                "option3_en": "Control Driving Law",
                "option3_es": "Ley de Control de Conducción",
                "correct_option": 2
            },
            {
                "question_en": "Who must have a CDL in Texas?",
                "question_es": "¿Quién debe tener un CDL en Texas?",
                "option1_en": "Any driver",
                "option1_es": "Cualquier conductor",
                "option2_en": "Driver of vehicles with trailer or cargo over 26,001 pounds",
                "option2_es": "Conductor de vehículos con remolque o carga mayor de 26,001 libras",
                "option3_en": "Motorcycle drivers",
                "option3_es": "Conductores de motocicletas",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if transporting cargo that protrudes from the rear?",
                "question_es": "¿Qué debe hacer si transporta carga que sobresale por la parte trasera?",
                "option1_en": "Call by radio",
                "option1_es": "Avisar por radio",
                "option2_en": "Mark it with red flag (day) or red light (night)",
                "option2_es": "Marcarla con bandera roja (de día) o luz roja (de noche)",
                "option3_en": "Cover it",
                "option3_es": "Cubrirla",
                "correct_option": 2
            },
            {
                "question_en": "What type of insurance is required for commercial vehicles?",
                "question_es": "¿Qué tipo de seguro se requiere para vehículos comerciales?",
                "option1_en": "Home insurance",
                "option1_es": "Seguro de casa",
                "option2_en": "Commercial liability insurance",
                "option2_es": "Seguro de responsabilidad comercial",
                "option3_en": "Personal insurance",
                "option3_es": "Seguro personal",
                "correct_option": 2
            },
            {
                "question_en": "What document does the state issue to authorize truck operation in Texas?",
                "question_es": "¿Qué documento emite el estado para autorizar la operación de un camión en Texas?",
                "option1_en": "State license",
                "option1_es": "Licencia estatal",
                "option2_en": "Commercial operation permit (TxDMV)",
                "option2_es": "Permiso de operación comercial (TxDMV)",
                "option3_en": "Purchase invoice",
                "option3_es": "Factura de compra",
                "correct_option": 2
            }
        ]
        
        # Add questions to database
        added_count = 0
        for question_data in questions:
            # Check if question already exists
            existing_question = db.query(Question).filter(
                Question.topic_id == topic.id,
                Question.question_en == question_data["question_en"]
            ).first()
            
            if existing_question:
                print(f"⚠️  Question already exists: {question_data['question_en'][:50]}...")
                continue
            
            question = Question(
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
            
            db.add(question)
            added_count += 1
            print(f"✅ Added question {added_count}: {question_data['question_en'][:50]}...")
        
        db.commit()
        print(f"\n🎉 Successfully added {added_count} questions to 'Texas Commercial Vehicle Operation' topic!")
        
    except Exception as e:
        print(f"❌ Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_texas_commercial_questions() 