from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_combination_vehicles_questions():
    db = SessionLocal()
    try:
        # Find the Combination Vehicles topic
        topic = db.query(Topic).filter(Topic.name_en == "Vehículos Combinados").first()
        
        if not topic:
            print("Topic 'Vehículos Combinados' not found!")
            return
        
        print(f"Found topic: {topic.name_en} (ID: {topic.id})")
        
        # Questions data with translations
        questions_data = [
            {
                "question_en": "What causes most rollovers in combination vehicles?",
                "question_es": "¿Qué causa la mayoría de los vuelcos en vehículos combinados?",
                "option1_en": "Braking hard",
                "option1_es": "Frenar con fuerza",
                "option2_en": "Taking curves too fast",
                "option2_es": "Tomar curvas demasiado rápido",
                "option3_en": "Bad road conditions",
                "option3_es": "Malas condiciones del camino",
                "correct_option": 2
            },
            {
                "question_en": "What is 'jackknife' in a combination vehicle?",
                "question_es": "¿Qué es el 'jackknife' en un vehículo combinado?",
                "option1_en": "A type of coupler",
                "option1_es": "Un tipo de acoplador",
                "option2_en": "An emergency tool",
                "option2_es": "Una herramienta de emergencia",
                "option3_en": "When the trailer folds against the tractor",
                "option3_es": "Cuando el remolque se pliega contra el tractor",
                "correct_option": 3
            },
            {
                "question_en": "What is the best way to avoid jackknife?",
                "question_es": "¿Cuál es la mejor forma de evitar el jackknife?",
                "option1_en": "Accelerate in curves",
                "option1_es": "Acelerar en curvas",
                "option2_en": "Brake early and gently",
                "option2_es": "Frenar temprano y suavemente",
                "option3_en": "Use emergency brake",
                "option3_es": "Usar el freno de emergencia",
                "correct_option": 2
            },
            {
                "question_en": "Why is it harder to brake a combination vehicle?",
                "question_es": "¿Por qué es más difícil frenar un vehículo combinado?",
                "option1_en": "Due to additional weight",
                "option1_es": "Por el peso adicional",
                "option2_en": "Because it has more wheels",
                "option2_es": "Por tener más ruedas",
                "option3_en": "Because it has more lights",
                "option3_es": "Porque tiene más luces",
                "correct_option": 1
            },
            {
                "question_en": "What part brakes first when using only the trailer brake?",
                "question_es": "¿Qué parte se frena primero cuando se usa solo el freno de remolque?",
                "option1_en": "Traction",
                "option1_es": "Tracción",
                "option2_en": "Trailer",
                "option2_es": "Remolque",
                "option3_en": "Tractor",
                "option3_es": "Tractor",
                "correct_option": 2
            },
            {
                "question_en": "What happens if the trailer doesn't have enough weight and brakes hard?",
                "question_es": "¿Qué pasa si el remolque no tiene suficiente peso y se frena bruscamente?",
                "option1_en": "The tractor can push it",
                "option1_es": "El tractor puede empujarlo",
                "option2_en": "The trailer can skid or roll over",
                "option2_es": "El remolque puede patinar o volcarse",
                "option3_en": "The brake regenerates",
                "option3_es": "El freno se regenera",
                "correct_option": 2
            },
            {
                "question_en": "What indicates that a trailer is not properly coupled?",
                "question_es": "¿Qué indica que un remolque no está bien acoplado?",
                "option1_en": "The parking brake activates",
                "option1_es": "El freno de estacionamiento se activa",
                "option2_en": "A whistle is heard",
                "option2_es": "Se oye un silbido",
                "option3_en": "The trailer falls off the tractor",
                "option3_es": "El remolque se cae del tractor",
                "correct_option": 3
            },
            {
                "question_en": "What is the correct use of the trailer emergency valve?",
                "question_es": "¿Cuál es el uso correcto de la válvula de emergencia del remolque?",
                "option1_en": "Disconnect ABS brake",
                "option1_es": "Desconectar el freno ABS",
                "option2_en": "Stop the trailer in case of pressure loss",
                "option2_es": "Detener el remolque en caso de pérdida de presión",
                "option3_en": "Turn off the engine",
                "option3_es": "Apagar el motor",
                "correct_option": 2
            },
            {
                "question_en": "What should be done before disconnecting a trailer?",
                "question_es": "¿Qué se debe hacer antes de desconectar un remolque?",
                "option1_en": "Turn off the lights",
                "option1_es": "Apagar las luces",
                "option2_en": "Lower the landing gear",
                "option2_es": "Bajar las patas de apoyo (landing gear)",
                "option3_en": "Increase air pressure",
                "option3_es": "Aumentar la presión de aire",
                "correct_option": 2
            },
            {
                "question_en": "Where is the tractor protection valve located?",
                "question_es": "¿Dónde se encuentra la válvula de protección del tractor?",
                "option1_en": "In the engine",
                "option1_es": "En el motor",
                "option2_en": "In the rear of the tractor",
                "option2_es": "En la parte trasera del tractor",
                "option3_en": "In the dashboard",
                "option3_es": "En el tablero",
                "correct_option": 2
            },
            {
                "question_en": "What does the tractor protection valve prevent?",
                "question_es": "¿Qué previene la válvula de protección del tractor?",
                "option1_en": "Loss of tractor air in case of trailer leak",
                "option1_es": "Pérdida de aire del tractor en caso de fuga en el remolque",
                "option2_en": "Engine damage",
                "option2_es": "Daños al motor",
                "option3_en": "Accidental uncoupling",
                "option3_es": "Desacoplamiento accidental",
                "correct_option": 1
            },
            {
                "question_en": "How is it verified that the trailer is properly coupled?",
                "question_es": "¿Cómo se verifica que el remolque está bien acoplado?",
                "option1_en": "By backing up",
                "option1_es": "Dando marcha atrás",
                "option2_en": "By checking that the locking pin is secured",
                "option2_es": "Revisando que el pasador de bloqueo esté asegurado",
                "option3_en": "By touching the lights",
                "option3_es": "Tocando las luces",
                "correct_option": 2
            },
            {
                "question_en": "What does 'unbalanced weight' mean in a trailer?",
                "question_es": "¿Qué significa 'peso desbalanceado' en un remolque?",
                "option1_en": "Poorly distributed load",
                "option1_es": "Carga mal distribuida",
                "option2_en": "Deflated tires",
                "option2_es": "Neumáticos desinflados",
                "option3_en": "Cold brakes",
                "option3_es": "Frenos fríos",
                "correct_option": 1
            },
            {
                "question_en": "When is the trailer service valve used?",
                "question_es": "¿Cuándo se usa la válvula de servicio del remolque?",
                "option1_en": "To turn on lights",
                "option1_es": "Para encender luces",
                "option2_en": "To brake with the main pedal",
                "option2_es": "Para frenar con el pedal principal",
                "option3_en": "To brake manually",
                "option3_es": "Para frenar manualmente",
                "correct_option": 2
            },
            {
                "question_en": "How should you drive when transporting an empty trailer?",
                "question_es": "¿Cómo debes conducir cuando transportas un remolque vacío?",
                "option1_en": "Same as loaded",
                "option1_es": "Igual que cargado",
                "option2_en": "Faster",
                "option2_es": "Más rápido",
                "option3_en": "More slowly and carefully",
                "option3_es": "Más despacio y con cuidado",
                "correct_option": 3
            },
            {
                "question_en": "What can cause poor trailer coupling?",
                "question_es": "¿Qué puede causar un mal acoplamiento del remolque?",
                "option1_en": "Damage to the fifth wheel",
                "option1_es": "Daños en la quinta rueda",
                "option2_en": "Full tank",
                "option2_es": "Tanque lleno",
                "option3_en": "Seat height",
                "option3_es": "Altura del asiento",
                "correct_option": 1
            },
            {
                "question_en": "What do you check in the fifth wheel when coupling?",
                "question_es": "¿Qué revisas en la quinta rueda al acoplar?",
                "option1_en": "That it's painted",
                "option1_es": "Que esté pintada",
                "option2_en": "That it has grease and is locked",
                "option2_es": "Que tenga grasa y esté bloqueada",
                "option3_en": "That it's rusty",
                "option3_es": "Que esté oxidada",
                "correct_option": 2
            },
            {
                "question_en": "What does a trailer pull to one side indicate?",
                "question_es": "¿Qué indica un tirón del remolque hacia un lado?",
                "option1_en": "Deflated tires",
                "option1_es": "Neumáticos desinflados",
                "option2_en": "Misadjusted brakes",
                "option2_es": "Frenos desajustados",
                "option3_en": "Light problem",
                "option3_es": "Problema con luces",
                "correct_option": 2
            },
            {
                "question_en": "What should be done when backing up to couple a trailer?",
                "question_es": "¿Qué se debe hacer al retroceder para acoplar un remolque?",
                "option1_en": "Go fast",
                "option1_es": "Ir rápido",
                "option2_en": "Use the right mirror",
                "option2_es": "Usar el espejo derecho",
                "option3_en": "Align tractor and trailer correctly",
                "option3_es": "Alinear tractor y remolque correctamente",
                "correct_option": 3
            },
            {
                "question_en": "What must be completely closed before hooking up a trailer?",
                "question_es": "¿Qué debe estar completamente cerrado antes de enganchar un remolque?",
                "option1_en": "The fuel cap",
                "option1_es": "La tapa del combustible",
                "option2_en": "The coupler mouth (fifth wheel)",
                "option2_es": "La boca del acoplador (quinta rueda)",
                "option3_en": "The trailer door",
                "option3_es": "La puerta del remolque",
                "correct_option": 2
            },
            {
                "question_en": "What does the safety pin in the fifth wheel do?",
                "question_es": "¿Qué hace el pasador de seguridad en la quinta rueda?",
                "option1_en": "Secures the coupler",
                "option1_es": "Fija el acoplador",
                "option2_en": "Connects the lights",
                "option2_es": "Conecta las luces",
                "option3_en": "Activates the brake",
                "option3_es": "Activa el freno",
                "correct_option": 1
            },
            {
                "question_en": "What is the 'glad hand'?",
                "question_es": "¿Qué es el 'glad hand'?",
                "option1_en": "A safety lever",
                "option1_es": "Una palanca de seguridad",
                "option2_en": "An air hose connector",
                "option2_es": "Un conector de manguera de aire",
                "option3_en": "Part of the brake",
                "option3_es": "Parte del freno",
                "correct_option": 2
            },
            {
                "question_en": "What does an air leak in the glad hands indicate?",
                "question_es": "¿Qué indica una fuga de aire en los glad hands?",
                "option1_en": "Pressure failure",
                "option1_es": "Falla de presión",
                "option2_en": "Lack of fuel",
                "option2_es": "Falta de combustible",
                "option3_en": "Lights off",
                "option3_es": "Luces apagadas",
                "correct_option": 1
            },
            {
                "question_en": "What does the trailer manual brake valve do?",
                "question_es": "¿Qué hace la válvula de freno manual del remolque?",
                "option1_en": "Applies only trailer brakes",
                "option1_es": "Aplica solo los frenos del remolque",
                "option2_en": "Activates ABS",
                "option2_es": "Activa ABS",
                "option3_en": "Uncouples the trailer",
                "option3_es": "Desacopla el remolque",
                "correct_option": 1
            },
            {
                "question_en": "What supports the trailer when it's not connected?",
                "question_es": "¿Qué parte sostiene el remolque cuando no está conectado?",
                "option1_en": "Chassis",
                "option1_es": "Chasis",
                "option2_en": "Landing gear",
                "option2_es": "Landing gear (patas de apoyo)",
                "option3_en": "Rear lights",
                "option3_es": "Luces traseras",
                "correct_option": 2
            },
            {
                "question_en": "What should you do when uncoupling the trailer on a slope?",
                "question_es": "¿Qué debes hacer al desacoplar el remolque en una pendiente?",
                "option1_en": "Leave the engine running",
                "option1_es": "Dejar el motor encendido",
                "option2_en": "Use chocks",
                "option2_es": "Usar cuñas (calzas)",
                "option3_en": "Turn the steering wheel",
                "option3_es": "Girar el volante",
                "correct_option": 2
            },
            {
                "question_en": "What is the 'pull test'?",
                "question_es": "¿Qué es el 'pull test'?",
                "option1_en": "Accelerate quickly",
                "option1_es": "Acelerar rápido",
                "option2_en": "Pull the trailer gently to check coupling",
                "option2_es": "Tirar del remolque suavemente para comprobar acoplamiento",
                "option3_en": "Test the brakes",
                "option3_es": "Probar los frenos",
                "correct_option": 2
            },
            {
                "question_en": "Why is it important to check air lines between tractor and trailer?",
                "question_es": "¿Por qué es importante revisar las líneas de aire entre tractor y remolque?",
                "option1_en": "In case they have dust",
                "option1_es": "Por si tienen polvo",
                "option2_en": "In case they are broken, loose or leaking",
                "option2_es": "Por si están rotas, sueltas o con fugas",
                "option3_en": "To verify temperature",
                "option3_es": "Para verificar la temperatura",
                "correct_option": 2
            },
            {
                "question_en": "What happens if you connect air lines incorrectly between tractor and trailer?",
                "question_es": "¿Qué pasa si conectas mal las líneas de aire entre tractor y remolque?",
                "option1_en": "Brake failure",
                "option1_es": "Fallo de frenos",
                "option2_en": "Light failure",
                "option2_es": "Fallo de luces",
                "option3_en": "Engine shuts off",
                "option3_es": "Se apaga el motor",
                "correct_option": 1
            },
            {
                "question_en": "What should you check when doing a visual inspection of the coupling?",
                "question_es": "¿Qué debes revisar al hacer una inspección visual del acoplamiento?",
                "option1_en": "Color of the fifth wheel",
                "option1_es": "Color de la quinta rueda",
                "option2_en": "Locked pin and no gap between plate and trailer",
                "option2_es": "Pasador bloqueado y sin espacio entre el plato y remolque",
                "option3_en": "That there's mud",
                "option3_es": "Que haya lodo",
                "correct_option": 2
            },
            {
                "question_en": "What happens if the tractor separates from the trailer while driving?",
                "question_es": "¿Qué ocurre si el tractor se separa del remolque mientras conduces?",
                "option1_en": "The parking brake activates",
                "option1_es": "Se activa el freno de estacionamiento",
                "option2_en": "The lights turn on",
                "option2_es": "Se encienden las luces",
                "option3_en": "The trailer emergency brakes activate",
                "option3_es": "Se activan los frenos de emergencia del remolque",
                "correct_option": 3
            },
            {
                "question_en": "What should you do immediately after coupling the trailer?",
                "question_es": "¿Qué debes hacer justo después de acoplar el remolque?",
                "option1_en": "Turn on lights",
                "option1_es": "Encender luces",
                "option2_en": "Perform a complete visual inspection",
                "option2_es": "Realizar una inspección visual completa",
                "option3_en": "Honk the horn",
                "option3_es": "Tocar la bocina",
                "correct_option": 2
            },
            {
                "question_en": "What do you check in the trailer's kingpin?",
                "question_es": "¿Qué revisas en el 'kingpin' del remolque?",
                "option1_en": "That it's bent",
                "option1_es": "Que esté doblado",
                "option2_en": "That it's clean",
                "option2_es": "Que esté limpio",
                "option3_en": "That it's not damaged or worn",
                "option3_es": "Que no esté dañado o gastado",
                "correct_option": 3
            },
            {
                "question_en": "Why should you avoid making tight turns with a trailer?",
                "question_es": "¿Por qué debes evitar hacer giros cerrados con remolque?",
                "option1_en": "Because tires wear out",
                "option1_es": "Porque se desgastan los neumáticos",
                "option2_en": "Because you can roll over or damage the cargo",
                "option2_es": "Porque puedes volcar o dañar la carga",
                "option3_en": "Because the engine strains",
                "option3_es": "Porque el motor se esfuerza",
                "correct_option": 2
            },
            {
                "question_en": "What should be checked before using trailer brakes on slopes?",
                "question_es": "¿Qué se debe revisar antes de usar los frenos del remolque en pendientes?",
                "option1_en": "That the air is complete",
                "option1_es": "Que el aire esté completo",
                "option2_en": "That the tank is full",
                "option2_es": "Que el tanque esté lleno",
                "option3_en": "That the lights are off",
                "option3_es": "Que las luces estén apagadas",
                "correct_option": 1
            },
            {
                "question_en": "When should tractor and trailer alignment be checked?",
                "question_es": "¿Cuándo se debe comprobar la alineación del tractor y remolque?",
                "option1_en": "During rain",
                "option1_es": "Durante la lluvia",
                "option2_en": "Before coupling",
                "option2_es": "Antes de acoplar",
                "option3_en": "When filling the tank",
                "option3_es": "Cuando llene el tanque",
                "correct_option": 2
            },
            {
                "question_en": "What happens if the fifth wheel coupler doesn't lock?",
                "question_es": "¿Qué ocurre si el acoplador de quinta rueda no se bloquea?",
                "option1_en": "The vehicle won't start",
                "option1_es": "El vehículo no arranca",
                "option2_en": "The trailer can come loose",
                "option2_es": "El remolque se puede soltar",
                "option3_en": "Air pressure drops",
                "option3_es": "La presión de aire baja",
                "correct_option": 2
            },
            {
                "question_en": "What is the greatest danger when uncoupling a trailer?",
                "question_es": "¿Cuál es el mayor peligro al desacoplar un remolque?",
                "option1_en": "Brake light off",
                "option1_es": "Luz de freno apagada",
                "option2_en": "That the trailer falls",
                "option2_es": "Que el remolque se caiga",
                "option3_en": "That brakes activate",
                "option3_es": "Que se activen los frenos",
                "correct_option": 2
            },
            {
                "question_en": "What indicates that the trailer is properly secured to the tractor?",
                "question_es": "¿Qué indica que el remolque está correctamente asegurado al tractor?",
                "option1_en": "Air flows well",
                "option1_es": "El aire fluye bien",
                "option2_en": "The pin is in place and the parking brake works",
                "option2_es": "El pasador está en su lugar y el freno de estacionamiento funciona",
                "option3_en": "The lights are on",
                "option3_es": "Las luces están encendidas",
                "correct_option": 2
            },
            {
                "question_en": "What part of the trailer couples with the fifth wheel?",
                "question_es": "¿Qué parte del remolque se acopla con la quinta rueda?",
                "option1_en": "The connection bar",
                "option1_es": "La barra de conexión",
                "option2_en": "The kingpin",
                "option2_es": "El kingpin",
                "option3_en": "The chassis",
                "option3_es": "El chasis",
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
        print(f"\nSuccessfully added {added_count} new questions to 'Vehículos Combinados'")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
        
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_combination_vehicles_questions() 