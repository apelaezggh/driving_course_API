from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Topic, Question

def add_doubles_triples_questions():
    db = SessionLocal()
    try:
        # Find the Doubles or Triples topic
        topic = db.query(Topic).filter(Topic.name_en == "Doubles or Triples").first()
        
        if not topic:
            print("Topic 'Doubles or Triples' not found!")
            return
        
        print(f"Found topic: {topic.name_en} (ID: {topic.id})")
        
        # Questions data with translations
        questions_data = [
            {
                "question_en": "What type of license do you need to drive double or triple combinations?",
                "question_es": "¿Qué tipo de licencia necesitas para conducir combinaciones dobles o triples?",
                "option1_en": "Class D",
                "option1_es": "Clase D",
                "option2_en": "Class A with T endorsement",
                "option2_es": "Clase A con endoso T",
                "option3_en": "Class B",
                "option3_es": "Clase B",
                "correct_option": 2
            },
            {
                "question_en": "What is the biggest difference when driving double or triple combinations?",
                "question_es": "¿Cuál es la mayor diferencia al conducir combinaciones dobles o triples?",
                "option1_en": "More fuel consumption",
                "option1_es": "Más consumo de combustible",
                "option2_en": "Greater length and difficulty turning and stopping",
                "option2_es": "Mayor longitud y dificultad para virar y detenerse",
                "option3_en": "Greater stability",
                "option3_es": "Mayor estabilidad",
                "correct_option": 2
            },
            {
                "question_en": "Which combination is more prone to rollover?",
                "question_es": "¿Qué combinación es más propensa al vuelco?",
                "option1_en": "The power unit",
                "option1_es": "La unidad motriz",
                "option2_en": "The first trailer",
                "option2_es": "El primer remolque",
                "option3_en": "The last trailer",
                "option3_es": "El último remolque",
                "correct_option": 3
            },
            {
                "question_en": "Which trailer is most prone to swerve or roll over?",
                "question_es": "¿Cuál es el remolque más propenso a desviarse o volcar?",
                "option1_en": "The first one",
                "option1_es": "El primero",
                "option2_en": "The longest one",
                "option2_es": "El más largo",
                "option3_en": "The rear trailer (last)",
                "option3_es": "El remolque trasero (último)",
                "correct_option": 3
            },
            {
                "question_en": "What is a converter dolly?",
                "question_es": "¿Qué es un convertidor dolly?",
                "option1_en": "A type of brake",
                "option1_es": "Un tipo de freno",
                "option2_en": "A device that connects double or triple trailers",
                "option2_es": "Un dispositivo que conecta remolques dobles o triples",
                "option3_en": "A loading tool",
                "option3_es": "Una herramienta para cargar",
                "correct_option": 2
            },
            {
                "question_en": "What should you especially check on a converter dolly?",
                "question_es": "¿Qué debes revisar especialmente en un convertidor dolly?",
                "option1_en": "Electrical cables",
                "option1_es": "Cables eléctricos",
                "option2_en": "Safety chains, fifth wheel, and brakes",
                "option2_es": "Cadenas de seguridad, quinta rueda, y frenos",
                "option3_en": "Seats",
                "option3_es": "Asientos",
                "correct_option": 2
            },
            {
                "question_en": "What should you do when parking a trailer combination on a slope?",
                "question_es": "¿Qué debes hacer al estacionar una combinación de remolques en una pendiente?",
                "option1_en": "Turn off the engine",
                "option1_es": "Apagar el motor",
                "option2_en": "Leave it in neutral",
                "option2_es": "Dejarlo en neutro",
                "option3_en": "Use chocks on the converter dolly wheels",
                "option3_es": "Usar cuñas en las ruedas del convertidor dolly",
                "correct_option": 3
            },
            {
                "question_en": "What problem can occur if you don't align the dolly well with the second trailer?",
                "question_es": "¿Qué problema puede ocurrir si no alineas bien el dolly con el segundo remolque?",
                "option1_en": "Nothing",
                "option1_es": "Nada",
                "option2_en": "Tire damage",
                "option2_es": "Daños al neumático",
                "option3_en": "The fifth wheel doesn't engage properly",
                "option3_es": "La quinta rueda no engancha correctamente",
                "correct_option": 3
            },
            {
                "question_en": "Where should air lines be connected first when adding a second trailer?",
                "question_es": "¿Dónde se deben conectar primero las líneas de aire al añadir un segundo remolque?",
                "option1_en": "To the front trailer",
                "option1_es": "Al remolque frontal",
                "option2_en": "To the converter dolly",
                "option2_es": "Al convertidor dolly",
                "option3_en": "To the power unit",
                "option3_es": "A la unidad motriz",
                "correct_option": 2
            },
            {
                "question_en": "What is the best practice when backing up a double or triple set?",
                "question_es": "¿Cuál es la mejor práctica al retroceder un conjunto de dobles o triples?",
                "option1_en": "Do it quickly",
                "option1_es": "Hacerlo rápido",
                "option2_en": "Only back up straight very slowly",
                "option2_es": "Solo retroceder recto muy lentamente",
                "option3_en": "Turn toward the shorter trailer",
                "option3_es": "Virar hacia el remolque más corto",
                "correct_option": 2
            },
            {
                "question_en": "What is important when uncoupling the second trailer?",
                "question_es": "¿Qué es importante al desacoplar el segundo remolque?",
                "option1_en": "Brake the power unit",
                "option1_es": "Frenar la unidad motriz",
                "option2_en": "Brake the dolly to prevent it from rolling",
                "option2_es": "Frenar el dolly para evitar que ruede",
                "option3_en": "Accelerate while uncoupling",
                "option3_es": "Acelerar mientras se desacopla",
                "correct_option": 2
            },
            {
                "question_en": "How should you drive in curves with doubles or triples?",
                "question_es": "¿Cómo debes conducir en curvas con dobles o triples?",
                "option1_en": "At normal speed",
                "option1_es": "A velocidad normal",
                "option2_en": "At reduced speed, turning wider",
                "option2_es": "A velocidad reducida, girando más ancho",
                "option3_en": "Braking in the curve",
                "option3_es": "Frenando en la curva",
                "correct_option": 2
            },
            {
                "question_en": "What should you do if the last trailer starts to fishtail?",
                "question_es": "¿Qué debes hacer si el último remolque comienza a serpentear (fishtail)?",
                "option1_en": "Accelerate",
                "option1_es": "Acelerar",
                "option2_en": "Brake immediately",
                "option2_es": "Frenar inmediatamente",
                "option3_en": "Release the accelerator gently and correct the steering",
                "option3_es": "Soltar el acelerador suavemente y corregir la dirección",
                "correct_option": 3
            },
            {
                "question_en": "What happens if you brake too hard with doubles or triples?",
                "question_es": "¿Qué sucede si frenas demasiado fuerte con dobles o triples?",
                "option1_en": "Nothing",
                "option1_es": "Nada",
                "option2_en": "You can lose control of the rear trailers",
                "option2_es": "Puedes perder el control de los remolques traseros",
                "option3_en": "Increases braking power",
                "option3_es": "Aumenta el poder de frenado",
                "correct_option": 2
            },
            {
                "question_en": "Why should hard braking be avoided with long combinations?",
                "question_es": "¿Por qué se debe evitar frenar bruscamente con combinaciones largas?",
                "option1_en": "Because ABS doesn't work",
                "option1_es": "Porque no funciona el ABS",
                "option2_en": "Because it can make trailers skid or roll over",
                "option2_es": "Porque puede hacer que los remolques patinen o se volteen",
                "option3_en": "Because it consumes more air",
                "option3_es": "Porque consume más aire",
                "correct_option": 2
            },
            {
                "question_en": "How is dolly alignment checked?",
                "question_es": "¿Cómo se revisa la alineación del dolly?",
                "option1_en": "Looking at mirror angles",
                "option1_es": "Mirando el ángulo de los espejos",
                "option2_en": "Verifying it's centered and straight with the second trailer",
                "option2_es": "Verificando que esté centrado y derecho con el segundo remolque",
                "option3_en": "Measuring the space between axles",
                "option3_es": "Midiendo el espacio entre ejes",
                "correct_option": 2
            },
            {
                "question_en": "Which trailer should be hooked to the tractor first?",
                "question_es": "¿Qué remolque se debe enganchar primero al tractor?",
                "option1_en": "The shortest one",
                "option1_es": "El más corto",
                "option2_en": "The heaviest and closest to the tractor",
                "option2_es": "El más pesado y cercano al tractor",
                "option3_en": "Any one",
                "option3_es": "Cualquiera",
                "correct_option": 2
            },
            {
                "question_en": "What should be done when checking air and electrical connections in doubles?",
                "question_es": "¿Qué se debe hacer al revisar conexiones de aire y electricidad en dobles?",
                "option1_en": "Kick them",
                "option1_es": "Patearlas",
                "option2_en": "Check for leaks, adjustment and firm connections",
                "option2_es": "Revisar fugas, ajuste y conexiones firmes",
                "option3_en": "Ignore them if they work",
                "option3_es": "Ignorarlas si funcionan",
                "correct_option": 2
            },
            {
                "question_en": "What can happen if the rear trailer is not properly secured?",
                "question_es": "¿Qué puede pasar si el remolque trasero no está bien asegurado?",
                "option1_en": "Nothing",
                "option1_es": "Nada",
                "option2_en": "It can come loose while moving",
                "option2_es": "Puede soltarse en movimiento",
                "option3_en": "Only the emergency brake activates",
                "option3_es": "Solo se activa el freno de emergencia",
                "correct_option": 2
            },
            {
                "question_en": "How should brakes be applied on long descents with doubles or triples?",
                "question_es": "¿Cómo se deben aplicar los frenos en bajadas largas con dobles o triples?",
                "option1_en": "Hard and continuous",
                "option1_es": "Fuerte y continuo",
                "option2_en": "In short pulses",
                "option2_es": "Por pulsos cortos",
                "option3_en": "With controlled and brief pressures",
                "option3_es": "Con presiones controladas y breves",
                "correct_option": 3
            },
            {
                "question_en": "What is most important when hooking a converter dolly to the tractor?",
                "question_es": "¿Qué es lo más importante al enganchar un convertidor dolly al tractor?",
                "option1_en": "Check the dolly color",
                "option1_es": "Revisar el color del dolly",
                "option2_en": "Align it correctly and secure the fifth wheel",
                "option2_es": "Alinearlo correctamente y asegurar la quinta rueda",
                "option3_en": "Make sure it has brakes",
                "option3_es": "Asegurarse de que tenga frenos",
                "correct_option": 2
            },
            {
                "question_en": "What should you do if the last trailer sways or moves too much?",
                "question_es": "¿Qué debes hacer si el último remolque se balancea o se mueve demasiado?",
                "option1_en": "Accelerate",
                "option1_es": "Acelerar",
                "option2_en": "Reduce speed gently",
                "option2_es": "Reducir la velocidad suavemente",
                "option3_en": "Brake hard",
                "option3_es": "Frenar bruscamente",
                "correct_option": 2
            },
            {
                "question_en": "What indicates that the fifth wheel coupling is properly closed?",
                "question_es": "¿Qué indica que el enganche de la quinta rueda está bien cerrado?",
                "option1_en": "The trailer lifts",
                "option1_es": "El remolque se eleva",
                "option2_en": "The latch locks properly and there's no visible gap",
                "option2_es": "El pestillo se traba correctamente y no hay espacio visible",
                "option3_en": "A click is heard",
                "option3_es": "Se escucha un clic",
                "correct_option": 2
            },
            {
                "question_en": "What does an air leak in a service line between trailers indicate?",
                "question_es": "¿Qué indica una fuga de aire en una línea de servicio entre remolques?",
                "option1_en": "Less air consumption",
                "option1_es": "Menos consumo de aire",
                "option2_en": "Service brake failure",
                "option2_es": "Fallo en los frenos de servicio",
                "option3_en": "Light activation",
                "option3_es": "Activación de luces",
                "correct_option": 2
            },
            {
                "question_en": "What can a poor electrical cable connection between trailers cause?",
                "question_es": "¿Qué puede causar una mala conexión del cable eléctrico entre remolques?",
                "option1_en": "ABS failure, lights or electric brake failure",
                "option1_es": "Fallo del ABS, luces o frenos eléctricos",
                "option2_en": "Higher speed",
                "option2_es": "Mayor velocidad",
                "option3_en": "More traction",
                "option3_es": "Más tracción",
                "correct_option": 1
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
        print(f"\nSuccessfully added {added_count} new questions to 'Doubles or Triples'")
        print(f"Total questions in topic: {db.query(Question).filter(Question.topic_id == topic.id).count()}")
        
    except Exception as e:
        print(f"Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_doubles_triples_questions() 