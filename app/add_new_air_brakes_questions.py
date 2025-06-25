from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_new_air_brakes_questions():
    db = SessionLocal()
    try:
        # Find the Air Brakes topic
        topic = db.query(Topic).filter(Topic.name_es == "Frenos de Aire").first()
        
        if not topic:
            print("Topic 'Frenos de Aire' not found!")
            return
        
        print(f"Found topic: {topic.name_es} (ID: {topic.id})")
        
        # Questions data with translations
        questions_data = [
            {
                "question_en": "What is the typical working pressure range in an air brake system?",
                "question_es": "¿Cuál es el rango típico de presión de trabajo en un sistema de frenos de aire?",
                "option1_en": "50-75 psi",
                "option1_es": "50-75 psi",
                "option2_en": "100-125 psi",
                "option2_es": "100-125 psi",
                "option3_en": "150-200 psi",
                "option3_es": "150-200 psi",
                "correct_option": 2
            },
            {
                "question_en": "What part of the air brake system is used to release spring brakes?",
                "question_es": "¿Qué parte del sistema de frenos de aire se utiliza para liberar los frenos de resorte?",
                "option1_en": "Compressor",
                "option1_es": "Compresor",
                "option2_en": "Control valve",
                "option2_es": "Válvula de control",
                "option3_en": "Air pressure",
                "option3_es": "Presión de aire",
                "correct_option": 3
            },
            {
                "question_en": "What happens if the air system pressure drops too low?",
                "question_es": "¿Qué sucede si la presión del sistema de aire baja demasiado?",
                "option1_en": "The vehicle accelerates",
                "option1_es": "El vehículo se acelera",
                "option2_en": "The emergency brake activates automatically",
                "option2_es": "El freno de emergencia se activa automáticamente",
                "option3_en": "The horn turns on",
                "option3_es": "El claxon se enciende",
                "correct_option": 2
            },
            {
                "question_en": "What is the purpose of the air compressor?",
                "question_es": "¿Cuál es el propósito del compresor de aire?",
                "option1_en": "Cool the engine",
                "option1_es": "Refrigerar el motor",
                "option2_en": "Charge the air brake system",
                "option2_es": "Cargar el sistema de frenos de aire",
                "option3_en": "Turn on the lights",
                "option3_es": "Encender las luces",
                "correct_option": 2
            },
            {
                "question_en": "What is the brake called that activates automatically if there is air pressure loss?",
                "question_es": "¿Cómo se llama el freno que se activa automáticamente si hay pérdida de presión de aire?",
                "option1_en": "Service brake",
                "option1_es": "Freno de servicio",
                "option2_en": "Emergency brake",
                "option2_es": "Freno de emergencia",
                "option3_en": "Parking brake",
                "option3_es": "Freno de estacionamiento",
                "correct_option": 2
            },
            {
                "question_en": "What is the purpose of the air dryer in an air brake system?",
                "question_es": "¿Cuál es el propósito del secador de aire en un sistema de frenos?",
                "option1_en": "Increase pressure",
                "option1_es": "Aumentar la presión",
                "option2_en": "Cool the air",
                "option2_es": "Enfriar el aire",
                "option3_en": "Remove moisture and contaminants",
                "option3_es": "Eliminar humedad y contaminantes",
                "correct_option": 3
            },
            {
                "question_en": "What should be done before checking spring brakes?",
                "question_es": "¿Qué se debe hacer antes de revisar los frenos de resorte?",
                "option1_en": "Remove air from the system",
                "option1_es": "Quitar el aire del sistema",
                "option2_en": "Start the engine",
                "option2_es": "Encender el motor",
                "option3_en": "Uncouple the trailer",
                "option3_es": "Desacoplar el remolque",
                "correct_option": 1
            },
            {
                "question_en": "When is the parking brake released in vehicles with air brakes?",
                "question_es": "¿Cuándo se libera el freno de estacionamiento en vehículos con frenos de aire?",
                "option1_en": "When the hand brake lever is activated",
                "option1_es": "Cuando se acciona la palanca de freno de mano",
                "option2_en": "When air pressure is applied to the brake",
                "option2_es": "Cuando se aplica presión de aire al freno",
                "option3_en": "When the vehicle is turned off",
                "option3_es": "Cuando el vehículo se apaga",
                "correct_option": 2
            },
            {
                "question_en": "What is a dual service control valve?",
                "question_es": "¿Qué es una válvula de control de doble servicio?",
                "option1_en": "A valve to adjust suspension",
                "option1_es": "Una válvula para ajustar la suspensión",
                "option2_en": "A valve that controls emergency and service brakes",
                "option2_es": "Una válvula que controla el freno de emergencia y servicio",
                "option3_en": "A valve for the fuel tank",
                "option3_es": "Una válvula para el tanque de combustible",
                "correct_option": 2
            },
            {
                "question_en": "What does a red low air pressure warning light indicate?",
                "question_es": "¿Qué indica una luz de advertencia roja de baja presión de aire?",
                "option1_en": "That the engine needs oil",
                "option1_es": "Que el motor necesita aceite",
                "option2_en": "That ABS brakes are active",
                "option2_es": "Que los frenos ABS están activos",
                "option3_en": "That air pressure is dangerously low",
                "option3_es": "Que la presión de aire es peligrosamente baja",
                "correct_option": 3
            },
            {
                "question_en": "How often should the air tank be manually drained?",
                "question_es": "¿Cada cuánto tiempo se debe drenar manualmente el tanque de aire?",
                "option1_en": "Once a week",
                "option1_es": "Una vez por semana",
                "option2_en": "After each trip",
                "option2_es": "Después de cada viaje",
                "option3_en": "Daily",
                "option3_es": "Diariamente",
                "correct_option": 3
            },
            {
                "question_en": "What causes air brakes to fade or fail?",
                "question_es": "¿Qué causa que los frenos de aire se desvanezcan o fallen?",
                "option1_en": "Low pressure",
                "option1_es": "Baja presión",
                "option2_en": "Excessive use and overheating",
                "option2_es": "Uso excesivo y calentamiento",
                "option3_en": "Too much brake fluid",
                "option3_es": "Demasiado líquido de frenos",
                "correct_option": 2
            },
            {
                "question_en": "Which tank fills first in an air brake system?",
                "question_es": "¿Qué tanque se llena primero en un sistema de frenos de aire?",
                "option1_en": "Primary tank",
                "option1_es": "Tanque primario",
                "option2_en": "Emergency tank",
                "option2_es": "Tanque de emergencia",
                "option3_en": "Service system tank",
                "option3_es": "Tanque del sistema de servicio",
                "correct_option": 3
            },
            {
                "question_en": "What is the 'spring brake'?",
                "question_es": "¿Qué es el 'freno de resorte'?",
                "option1_en": "Brake used to maintain speed",
                "option1_es": "Freno usado para mantener la velocidad",
                "option2_en": "Emergency or parking brake activated by springs",
                "option2_es": "Freno de emergencia o estacionamiento activado por resortes",
                "option3_en": "Brake that activates with electricity",
                "option3_es": "Freno que se activa con electricidad",
                "correct_option": 2
            },
            {
                "question_en": "How is an air brake system leak verified?",
                "question_es": "¿Cómo se verifica una fuga del sistema de frenos de aire?",
                "option1_en": "By listening to the engine",
                "option1_es": "Escuchando el motor",
                "option2_en": "By applying the service brake and observing pressure drop",
                "option2_es": "Aplicando el freno de servicio y observando la caída de presión",
                "option3_en": "By turning on the lights",
                "option3_es": "Encendiendo las luces",
                "correct_option": 2
            },
            {
                "question_en": "When is the tractor protection valve activated?",
                "question_es": "¿Cuándo se activa la válvula de protección del tractor?",
                "option1_en": "When the hand brake is applied",
                "option1_es": "Cuando se aplica el freno de mano",
                "option2_en": "When air pressure drops below a safe level",
                "option2_es": "Cuando la presión de aire cae por debajo de un nivel seguro",
                "option3_en": "When the steering wheel is turned",
                "option3_es": "Cuando se gira el volante",
                "correct_option": 2
            },
            {
                "question_en": "What can cause moisture in the air system?",
                "question_es": "¿Qué puede causar humedad en el sistema de aire?",
                "option1_en": "Unfiltered compressed air",
                "option1_es": "Aire comprimido sin filtrado",
                "option2_en": "Excess oil",
                "option2_es": "Exceso de aceite",
                "option3_en": "Dirty filters",
                "option3_es": "Filtros sucios",
                "correct_option": 1
            },
            {
                "question_en": "What does 'controlled braking' mean?",
                "question_es": "¿Qué significa 'frenado controlado'?",
                "option1_en": "Apply brakes suddenly",
                "option1_es": "Aplicar frenos de golpe",
                "option2_en": "Brake hard all the time",
                "option2_es": "Frenar fuerte todo el tiempo",
                "option3_en": "Apply brakes firmly without locking wheels",
                "option3_es": "Aplicar frenos firmemente sin bloquear ruedas",
                "correct_option": 3
            },
            {
                "question_en": "What should you do if your vehicle has ABS brake system?",
                "question_es": "¿Qué debe hacer si su vehículo tiene sistema de frenos ABS?",
                "option1_en": "Brake normally",
                "option1_es": "Frenar normalmente",
                "option2_en": "Use only engine brake",
                "option2_es": "Usar solo el freno de motor",
                "option3_en": "Brake more slowly",
                "option3_es": "Frenar más despacio",
                "correct_option": 1
            },
            {
                "question_en": "What does the ABS system do?",
                "question_es": "¿Qué hace el sistema ABS?",
                "option1_en": "Reduces tire wear",
                "option1_es": "Reduce el desgaste de llantas",
                "option2_en": "Prevents wheels from locking when braking",
                "option2_es": "Evita que las ruedas se bloqueen al frenar",
                "option3_en": "Decreases brake pressure",
                "option3_es": "Disminuye la presión de los frenos",
                "correct_option": 2
            },
            {
                "question_en": "How is the ABS system operation tested?",
                "question_es": "¿Cómo se prueba el funcionamiento del sistema ABS?",
                "option1_en": "By checking the air valve",
                "option1_es": "Revisando la válvula de aire",
                "option2_en": "By verifying that the ABS light turns on and off",
                "option2_es": "Verificando que se encienda y apague la luz de ABS",
                "option3_en": "By braking hard",
                "option3_es": "Frenando a fondo",
                "correct_option": 2
            },
            {
                "question_en": "What part of the brake system maintains pressure to apply service brakes?",
                "question_es": "¿Qué parte del sistema de frenos mantiene presión para aplicar los frenos de servicio?",
                "option1_en": "Reserve tank",
                "option1_es": "Tanque de reserva",
                "option2_en": "Supply tank",
                "option2_es": "Tanque de suministro",
                "option3_en": "Control valve",
                "option3_es": "Válvula de control",
                "correct_option": 2
            },
            {
                "question_en": "What happens if the brake is pressed repeatedly in an air system?",
                "question_es": "¿Qué ocurre si se pisa el freno repetidamente en un sistema de aire?",
                "option1_en": "It cools down",
                "option1_es": "Se enfría",
                "option2_en": "It recharges",
                "option2_es": "Se recarga",
                "option3_en": "It loses pressure rapidly",
                "option3_es": "Se pierde presión rápidamente",
                "correct_option": 3
            },
            {
                "question_en": "What function does the brake pedal have in vehicles with air brakes?",
                "question_es": "¿Qué función tiene el pedal de freno en vehículos con frenos de aire?",
                "option1_en": "Releases the parking brake",
                "option1_es": "Libera el freno de estacionamiento",
                "option2_en": "Controls the amount of pressure sent to the brakes",
                "option2_es": "Controla la cantidad de presión enviada a los frenos",
                "option3_en": "Activates the air compressor",
                "option3_es": "Activa el compresor de aire",
                "correct_option": 2
            },
            {
                "question_en": "What should be done if an air leak is heard in the brake system?",
                "question_es": "¿Qué se debe hacer si se escucha una fuga de aire en el sistema de frenos?",
                "option1_en": "Ignore it",
                "option1_es": "Ignorarla",
                "option2_en": "Report it and repair it before driving",
                "option2_es": "Reportarla y repararla antes de conducir",
                "option3_en": "Cover it with tape",
                "option3_es": "Taparla con cinta",
                "correct_option": 2
            },
            {
                "question_en": "What is the minimum air pressure required before driving?",
                "question_es": "¿Cuál es el mínimo de presión de aire requerida antes de conducir?",
                "option1_en": "50 psi",
                "option1_es": "50 psi",
                "option2_en": "100 psi",
                "option2_es": "100 psi",
                "option3_en": "30 psi",
                "option3_es": "30 psi",
                "correct_option": 2
            },
            {
                "question_en": "What should you do when stopping on a steep slope?",
                "question_es": "¿Qué debes hacer al detenerte en una pendiente pronunciada?",
                "option1_en": "Turn off the engine",
                "option1_es": "Apagar el motor",
                "option2_en": "Use spring brakes and chocks",
                "option2_es": "Usar los frenos de resorte y calzas",
                "option3_en": "Only hand brake",
                "option3_es": "Solo freno de mano",
                "correct_option": 2
            },
            {
                "question_en": "What does a front brake limiting valve do?",
                "question_es": "¿Qué hace una válvula limitadora de freno delantero?",
                "option1_en": "Reduces brake noise",
                "option1_es": "Reduce el ruido del freno",
                "option2_en": "Reduces air pressure in front brakes to prevent locking",
                "option2_es": "Reduce la presión de aire en los frenos delanteros para evitar bloqueo",
                "option3_en": "Increases pressure",
                "option3_es": "Aumenta la presión",
                "correct_option": 2
            },
            {
                "question_en": "What pressure is required for the low pressure warning signal to turn off?",
                "question_es": "¿Qué presión se requiere para que se desactive la señal de advertencia de presión baja?",
                "option1_en": "60 psi",
                "option1_es": "60 psi",
                "option2_en": "20 psi",
                "option2_es": "20 psi",
                "option3_en": "80 psi",
                "option3_es": "80 psi",
                "correct_option": 1
            },
            {
                "question_en": "What can happen if spring brakes fail?",
                "question_es": "¿Qué puede ocurrir si los frenos de resorte fallan?",
                "option1_en": "The vehicle won't start",
                "option1_es": "El vehículo no arranca",
                "option2_en": "The vehicle may be left without parking brake",
                "option2_es": "El vehículo puede quedarse sin freno de estacionamiento",
                "option3_en": "The engine turns off",
                "option3_es": "El motor se apaga",
                "correct_option": 2
            },
            {
                "question_en": "What does it indicate if the low air pressure warning light stays on after starting the engine?",
                "question_es": "¿Qué indica si la luz de advertencia de baja presión de aire permanece encendida después de arrancar el motor?",
                "option1_en": "That the ABS system is active",
                "option1_es": "Que el sistema ABS está activo",
                "option2_en": "That the brake system has not yet reached safe pressure",
                "option2_es": "Que el sistema de frenos aún no ha alcanzado presión segura",
                "option3_en": "That the brakes are in good condition",
                "option3_es": "Que los frenos están en buenas condiciones",
                "correct_option": 2
            },
            {
                "question_en": "At what pressure should the compressor cut off in most air brake systems?",
                "question_es": "¿A qué presión debe cortarse el compresor en la mayoría de los sistemas de frenos de aire?",
                "option1_en": "100 psi",
                "option1_es": "100 psi",
                "option2_en": "125 psi",
                "option2_es": "125 psi",
                "option3_en": "150 psi",
                "option3_es": "150 psi",
                "correct_option": 2
            },
            {
                "question_en": "What is the function of the air compressor governor?",
                "question_es": "¿Cuál es la función del gobernador del compresor de aire?",
                "option1_en": "Cool the compressor",
                "option1_es": "Enfriar el compresor",
                "option2_en": "Control when the compressor charges and discharges air",
                "option2_es": "Controlar cuándo el compresor carga y descarga aire",
                "option3_en": "Regulate fuel level",
                "option3_es": "Regular el nivel de combustible",
                "correct_option": 2
            },
            {
                "question_en": "What should you do if during inspection you hear a continuous air leak?",
                "question_es": "¿Qué debes hacer si durante la inspección escuchas una fuga continua de aire?",
                "option1_en": "Use emergency brakes",
                "option1_es": "Usar los frenos de emergencia",
                "option2_en": "Ignore it if the vehicle brakes well",
                "option2_es": "Ignorarla si el vehículo frena bien",
                "option3_en": "Repair it before operating the vehicle",
                "option3_es": "Repararla antes de operar el vehículo",
                "correct_option": 3
            },
            {
                "question_en": "What part of the system maintains the air pressure necessary for the emergency brake?",
                "question_es": "¿Qué parte del sistema mantiene la presión de aire necesaria para el freno de emergencia?",
                "option1_en": "Safety valve",
                "option1_es": "Válvula de seguridad",
                "option2_en": "Emergency tank",
                "option2_es": "Tanque de emergencia",
                "option3_en": "Compressor",
                "option3_es": "Compresor",
                "correct_option": 2
            },
            {
                "question_en": "What can cause brakes to 'freeze' in cold weather?",
                "question_es": "¿Qué puede causar que los frenos se 'congelen' en climas fríos?",
                "option1_en": "Lack of brake fluid",
                "option1_es": "Falta de líquido de frenos",
                "option2_en": "Excess pressure",
                "option2_es": "Exceso de presión",
                "option3_en": "Moisture in the air system",
                "option3_es": "Humedad en el sistema de aire",
                "correct_option": 3
            },
            {
                "question_en": "What should be done if air brakes become excessively hot?",
                "question_es": "¿Qué se debe hacer si los frenos de aire se calientan excesivamente?",
                "option1_en": "Brake harder",
                "option1_es": "Frenar con más fuerza",
                "option2_en": "Use engine brake or retarder instead of service brakes",
                "option2_es": "Usar el freno del motor o retardador en lugar de los frenos de servicio",
                "option3_en": "Stop and turn off the engine",
                "option3_es": "Detenerse y apagar el motor",
                "correct_option": 2
            },
            {
                "question_en": "What is the pressure range for emergency brake activation due to low air pressure?",
                "question_es": "¿Cuál es el rango de presión de activación del freno de emergencia debido a baja presión de aire?",
                "option1_en": "60-80 psi",
                "option1_es": "60-80 psi",
                "option2_en": "20-45 psi",
                "option2_es": "20-45 psi",
                "option3_en": "100-120 psi",
                "option3_es": "100-120 psi",
                "correct_option": 2
            },
            {
                "question_en": "Why do vehicles with air brakes have dual systems?",
                "question_es": "¿Por qué los vehículos con frenos de aire tienen doble sistema?",
                "option1_en": "To brake faster",
                "option1_es": "Para frenar más rápido",
                "option2_en": "To separate front and rear brakes for safety",
                "option2_es": "Para separar frenos delanteros y traseros por seguridad",
                "option3_en": "To reduce air consumption",
                "option3_es": "Para reducir consumo de aire",
                "correct_option": 2
            },
            {
                "question_en": "What does it indicate if the spring brake does not release after pressurizing the system?",
                "question_es": "¿Qué indica si el freno de resorte no se libera después de presurizar el sistema?",
                "option1_en": "The service brake is activated",
                "option1_es": "El freno de servicio está activado",
                "option2_en": "There is a leak or failure in the system",
                "option2_es": "Hay una fuga o falla en el sistema",
                "option3_en": "The brake is working correctly",
                "option3_es": "El freno está funcionando correctamente",
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
        print(f"\nSuccessfully added {added_count} new questions to 'Frenos de Aire'")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
        
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_new_air_brakes_questions() 