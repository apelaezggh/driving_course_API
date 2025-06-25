from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Question, Topic

def add_general_knowledge_questions():
    db = SessionLocal()
    
    try:
        # Get the General Knowledge topic
        topic = db.query(Topic).filter(Topic.name_en == "General Knowledge").first()
        if not topic:
            print("❌ Topic 'General Knowledge' not found!")
            return
        
        print(f"✅ Found topic: {topic.name_en} (ID: {topic.id})")
        
        # Define the questions
        questions = [
            {
                "question_en": "What should you always do before driving a commercial vehicle?",
                "question_es": "¿Qué debe hacer siempre antes de conducir un vehículo comercial?",
                "option1_en": "Check social media",
                "option1_es": "Revisar redes sociales",
                "option2_en": "Pre-trip inspection",
                "option2_es": "Inspección previa al viaje",
                "option3_en": "Adjust rearview mirrors only",
                "option3_es": "Ajustar los espejos retrovisores únicamente",
                "correct_option": 2
            },
            {
                "question_en": "What can cause an accident with a large vehicle?",
                "question_es": "¿Qué puede causar un accidente con un vehículo grande?",
                "option1_en": "Bad music",
                "option1_es": "Mala música",
                "option2_en": "Distraction and poor space calculation",
                "option2_es": "Distracción y mal cálculo del espacio",
                "option3_en": "Too much visibility",
                "option3_es": "Mucha visibilidad",
                "correct_option": 2
            },
            {
                "question_en": "What is the legal minimum depth in the main grooves of front tires?",
                "question_es": "¿Cuál es el mínimo legal de profundidad en las ranuras principales de las llantas delanteras?",
                "option1_en": "1/16 inch",
                "option1_es": "1/16 pulgada",
                "option2_en": "2/32 inch",
                "option2_es": "2/32 pulgada",
                "option3_en": "4/32 inch",
                "option3_es": "4/32 pulgada",
                "correct_option": 3
            },
            {
                "question_en": "What does 'perception time' mean?",
                "question_es": "¿Qué significa 'tiempo de percepción'?",
                "option1_en": "Time it takes to brake",
                "option1_es": "Tiempo que toma frenar",
                "option2_en": "Time between seeing the danger and reacting",
                "option2_es": "Tiempo entre ver el peligro y reaccionar",
                "option3_en": "Time it takes the truck to stop",
                "option3_es": "Tiempo que tarda el camión en detenerse",
                "correct_option": 2
            },
            {
                "question_en": "What is 'hydroplaning'?",
                "question_es": "¿Qué es el 'hidroplaneo'?",
                "option1_en": "Engine wear",
                "option1_es": "Desgaste del motor",
                "option2_en": "When tires lose contact with pavement due to water",
                "option2_es": "Cuando las llantas pierden contacto con el pavimento por agua",
                "option3_en": "Hydraulic system failure",
                "option3_es": "Falla del sistema hidráulico",
                "correct_option": 2
            },
            {
                "question_en": "When should side mirrors be checked?",
                "question_es": "¿Cuándo se deben revisar los espejos laterales?",
                "option1_en": "Every hour",
                "option1_es": "Cada hora",
                "option2_en": "Constantly while driving",
                "option2_es": "Constantemente mientras se conduce",
                "option3_en": "Only before parking",
                "option3_es": "Solo antes de estacionarse",
                "correct_option": 2
            },
            {
                "question_en": "What is a good way to drive on a steep downhill?",
                "question_es": "¿Cuál es una buena forma de manejar en una bajada empinada?",
                "option1_en": "In neutral",
                "option1_es": "En punto muerto",
                "option2_en": "In the same gear or a lower one than when going uphill",
                "option2_es": "En la misma marcha o una menor que al subir",
                "option3_en": "Accelerating to not lose momentum",
                "option3_es": "Acelerando para no perder impulso",
                "correct_option": 2
            },
            {
                "question_en": "How far ahead should you look while driving a truck?",
                "question_es": "¿Qué tan lejos debe mirar hacia adelante mientras conduce un camión?",
                "option1_en": "3 seconds",
                "option1_es": "3 segundos",
                "option2_en": "12-15 seconds",
                "option2_es": "12-15 segundos",
                "option3_en": "Only the next traffic light",
                "option3_es": "Solo el siguiente semáforo",
                "correct_option": 2
            },
            {
                "question_en": "What should you do if your vehicle pulls to one side when braking?",
                "question_es": "¿Qué debe hacer si su vehículo se desvía hacia un lado cuando frena?",
                "option1_en": "Brake harder",
                "option1_es": "Frenar más fuerte",
                "option2_en": "Check brakes immediately",
                "option2_es": "Revisar los frenos inmediatamente",
                "option3_en": "Accelerate",
                "option3_es": "Acelerar",
                "correct_option": 2
            },
            {
                "question_en": "What does a leak in the exhaust system near the cab indicate?",
                "question_es": "¿Qué indica una fuga en el sistema de escape cerca de la cabina?",
                "option1_en": "Performance improvement",
                "option1_es": "Mejora de rendimiento",
                "option2_en": "Danger of carbon monoxide poisoning",
                "option2_es": "Peligro de envenenamiento por monóxido de carbono",
                "option3_en": "Greater fuel savings",
                "option3_es": "Mayor ahorro de combustible",
                "correct_option": 2
            },
            {
                "question_en": "What should you do if your brakes fail on a downhill?",
                "question_es": "¿Qué debe hacer si sus frenos fallan en una bajada?",
                "option1_en": "Shift to neutral",
                "option1_es": "Cambiar a neutral",
                "option2_en": "Use the escape ramp",
                "option2_es": "Usar la rampa de escape",
                "option3_en": "Jump from the vehicle",
                "option3_es": "Saltar del vehículo",
                "correct_option": 2
            },
            {
                "question_en": "What should you do if you need to make an emergency stop on a highway?",
                "question_es": "¿Qué debe hacer si necesita parar de emergencia en una autopista?",
                "option1_en": "Stop in the slow lane",
                "option1_es": "Detenerse en el carril lento",
                "option2_en": "Place emergency triangles",
                "option2_es": "Colocar los triángulos de emergencia",
                "option3_en": "Continue to a service station",
                "option3_es": "Seguir hasta una estación de servicio",
                "correct_option": 2
            },
            {
                "question_en": "When should you use the air horn?",
                "question_es": "¿Cuándo debe usar la bocina de aire?",
                "option1_en": "To greet",
                "option1_es": "Para saludar",
                "option2_en": "Only to warn of danger",
                "option2_es": "Solo para advertir un peligro",
                "option3_en": "When changing lanes",
                "option3_es": "Al cambiar de carril",
                "correct_option": 2
            },
            {
                "question_en": "What can cause loss of air pressure in brakes?",
                "question_es": "¿Qué puede causar una pérdida de presión de aire en frenos?",
                "option1_en": "Rain",
                "option1_es": "Lluvia",
                "option2_en": "Leaks in air lines",
                "option2_es": "Fugas en las líneas de aire",
                "option3_en": "Direct sunlight",
                "option3_es": "Luz solar directa",
                "correct_option": 2
            },
            {
                "question_en": "What is a common cause of fire in commercial vehicles?",
                "question_es": "¿Cuál es una causa común de incendio en vehículos comerciales?",
                "option1_en": "Overinflated tires",
                "option1_es": "Neumáticos sobreinflados",
                "option2_en": "Premium fuel",
                "option2_es": "Combustible premium",
                "option3_en": "Dirty air filter",
                "option3_es": "Filtro de aire sucio",
                "correct_option": 1
            },
            {
                "question_en": "When is a driver considered fatigued?",
                "question_es": "¿Cuándo se considera que el conductor está fatigado?",
                "option1_en": "When driving at night",
                "option1_es": "Cuando maneja de noche",
                "option2_en": "When experiencing loss of attention or drowsiness",
                "option2_es": "Cuando sufre pérdida de atención o somnolencia",
                "option3_en": "When eating too much",
                "option3_es": "Cuando come en exceso",
                "correct_option": 2
            },
            {
                "question_en": "How can you reduce the risk of accidents when changing lanes?",
                "question_es": "¿Cómo puede reducir el riesgo de accidentes al cambiar de carril?",
                "option1_en": "Changing quickly",
                "option1_es": "Cambiando rápido",
                "option2_en": "Checking mirrors and blind spots constantly",
                "option2_es": "Revisando espejos y puntos ciegos constantemente",
                "option3_en": "Without using signal",
                "option3_es": "Sin usar señal",
                "correct_option": 2
            },
            {
                "question_en": "What is the main purpose of the parking brake?",
                "question_es": "¿Cuál es el principal propósito del freno de estacionamiento?",
                "option1_en": "Keep the engine running",
                "option1_es": "Mantener el motor encendido",
                "option2_en": "Prevent the vehicle from rolling",
                "option2_es": "Evitar que el vehículo ruede",
                "option3_en": "Turn off the vehicle",
                "option3_es": "Apagar el vehículo",
                "correct_option": 2
            },
            {
                "question_en": "What does a warning signal with flashing lights on the dashboard indicate?",
                "question_es": "¿Qué indica una señal de advertencia con luces intermitentes en el tablero?",
                "option1_en": "Visual warning only",
                "option1_es": "Aviso visual solamente",
                "option2_en": "Critical system failure",
                "option2_es": "Fallo en sistema crítico",
                "option3_en": "Speed excess",
                "option3_es": "Exceso de velocidad",
                "correct_option": 2
            },
            {
                "question_en": "What does the speed limiter do in some commercial vehicles?",
                "question_es": "¿Qué hace el limitador de velocidad en algunos vehículos comerciales?",
                "option1_en": "Accelerate on hills",
                "option1_es": "Acelera en cuestas",
                "option2_en": "Restrict maximum speed",
                "option2_es": "Restringe velocidad máxima",
                "option3_en": "Adjust tire pressure",
                "option3_es": "Ajusta presión de neumáticos",
                "correct_option": 2
            },
            {
                "question_en": "When should brakes be checked?",
                "question_es": "¿Cuándo deben revisarse los frenos?",
                "option1_en": "Weekly",
                "option1_es": "Semanalmente",
                "option2_en": "Before each trip",
                "option2_es": "Antes de cada viaje",
                "option3_en": "Only on long trips",
                "option3_es": "Solo en viajes largos",
                "correct_option": 2
            },
            {
                "question_en": "What is the first step if your vehicle breaks down on the road?",
                "question_es": "¿Cuál es el primer paso si su vehículo se avería en la carretera?",
                "option1_en": "Turn off the engine",
                "option1_es": "Apagar el motor",
                "option2_en": "Turn on emergency lights and signal",
                "option2_es": "Encender luces de emergencia y señalizar",
                "option3_en": "Run away",
                "option3_es": "Salir corriendo",
                "correct_option": 2
            },
            {
                "question_en": "What is the 'blind spot' in a truck?",
                "question_es": "¿Qué es la 'zona ciega' (punto ciego) en un camión?",
                "option1_en": "Area without lighting",
                "option1_es": "Área sin iluminación",
                "option2_en": "Areas where other vehicles cannot be seen from mirrors",
                "option2_es": "Áreas donde otros vehículos no se ven desde los espejos",
                "option3_en": "Loading area",
                "option3_es": "Zona de carga",
                "correct_option": 2
            },
            {
                "question_en": "What should you do when driving in fog conditions?",
                "question_es": "¿Qué debe hacer al conducir en condiciones de niebla?",
                "option1_en": "Use high beams",
                "option1_es": "Usar luces altas",
                "option2_en": "Reduce speed and use low beams",
                "option2_es": "Reducir velocidad y usar luces bajas",
                "option3_en": "Brake constantly",
                "option3_es": "Frenar constantemente",
                "correct_option": 2
            },
            {
                "question_en": "What happens if you don't adjust cargo straps correctly?",
                "question_es": "¿Qué ocurre si no ajusta las correas de carga correctamente?",
                "option1_en": "Nothing",
                "option1_es": "Nada",
                "option2_en": "Risk of loose cargo",
                "option2_es": "Riesgo de carga suelta",
                "option3_en": "Improve efficiency",
                "option3_es": "Mejora la eficiencia",
                "correct_option": 2
            },
            {
                "question_en": "What type of CDL license is needed to drive heavy trailers?",
                "question_es": "¿Qué tipo de licencia CDL se necesita para manejar remolques pesados?",
                "option1_en": "Class B",
                "option1_es": "Clase B",
                "option2_en": "Class C",
                "option2_es": "Clase C",
                "option3_en": "Class A",
                "option3_es": "Clase A",
                "correct_option": 3
            },
            {
                "question_en": "What should be done if there is a flammable liquid spill?",
                "question_es": "¿Qué se debe hacer si hay derrame de líquido inflamable?",
                "option1_en": "Clean it with water",
                "option1_es": "Limpiarlo con agua",
                "option2_en": "Stop, notify and evacuate",
                "option2_es": "Detenerse, notificar y evacuar",
                "option3_en": "Light a flare",
                "option3_es": "Encender una bengala",
                "correct_option": 2
            },
            {
                "question_en": "What action is unsafe in a tight downhill curve?",
                "question_es": "¿Qué acción es insegura en una curva cerrada cuesta abajo?",
                "option1_en": "Reduce speed before",
                "option1_es": "Reducir la velocidad antes",
                "option2_en": "Brake during the curve",
                "option2_es": "Frenar durante la curva",
                "option3_en": "Use a low gear",
                "option3_es": "Usar una marcha baja",
                "correct_option": 2
            },
            {
                "question_en": "What should you do if a tire blows out at high speed?",
                "question_es": "¿Qué debe hacer si una llanta revienta a alta velocidad?",
                "option1_en": "Brake hard",
                "option1_es": "Frenar fuertemente",
                "option2_en": "Hold steering wheel firm, don't brake, and reduce speed gradually",
                "option2_es": "Agarrar el volante firme, no frenar, y reducir velocidad poco a poco",
                "option3_en": "Turn on windshield wipers",
                "option3_es": "Encender los limpia parabrisas",
                "correct_option": 2
            },
            {
                "question_en": "What does 'total stopping distance' mean?",
                "question_es": "¿Qué significa 'distancia total de detención'?",
                "option1_en": "Braking time",
                "option1_es": "Tiempo de frenado",
                "option2_en": "Perception time + reaction + braking",
                "option2_es": "Tiempo de percepción + reacción + frenado",
                "option3_en": "Response time",
                "option3_es": "Tiempo de respuesta",
                "correct_option": 2
            },
            {
                "question_en": "When is hydroplaning most likely to occur?",
                "question_es": "¿Cuándo es más probable que ocurra el hidroplaneo?",
                "option1_en": "Light rain",
                "option1_es": "Lluvia ligera",
                "option2_en": "Heavy rain and oily road",
                "option2_es": "Lluvia intensa y carretera con aceite",
                "option3_en": "Dry weather",
                "option3_es": "Tiempo seco",
                "correct_option": 2
            },
            {
                "question_en": "What is a 'Post-Trip Inspection Report'?",
                "question_es": "¿Qué es un 'Informe de Inspección Post-Viaje'?",
                "option1_en": "A trip summary",
                "option1_es": "Un resumen del viaje",
                "option2_en": "Report on defects found at end of trip",
                "option2_es": "Informe sobre fallas encontradas al final del viaje",
                "option3_en": "Document for the client",
                "option3_es": "Documento para el cliente",
                "correct_option": 2
            },
            {
                "question_en": "What is the effect of driving with poorly adjusted brakes?",
                "question_es": "¿Cuál es el efecto de conducir con frenos mal ajustados?",
                "option1_en": "Normal wear",
                "option1_es": "Desgaste normal",
                "option2_en": "Loss of control",
                "option2_es": "Pérdida de control",
                "option3_en": "Greater power",
                "option3_es": "Mayor potencia",
                "correct_option": 2
            },
            {
                "question_en": "What should you do if a train is approaching and the crossing lights are flashing?",
                "question_es": "¿Qué debe hacer si se aproxima un tren y las luces del cruce parpadean?",
                "option1_en": "Accelerate",
                "option1_es": "Acelerar",
                "option2_en": "Stop completely",
                "option2_es": "Detenerse completamente",
                "option3_en": "Wait for someone else to pass",
                "option3_es": "Esperar a que alguien más pase",
                "correct_option": 2
            },
            {
                "question_en": "What is 'escape space'?",
                "question_es": "¿Qué es 'espacio de escape'?",
                "option1_en": "Area to stop in emergencies",
                "option1_es": "Área para detenerse en emergencias",
                "option2_en": "Space between vehicles",
                "option2_es": "Espacio entre vehículos",
                "option3_en": "Driver refuge",
                "option3_es": "Refugio de choferes",
                "correct_option": 1
            },
            {
                "question_en": "What is required when transporting cargo on a platform?",
                "question_es": "¿Qué se requiere cuando se transporta carga sobre una plataforma?",
                "option1_en": "Nothing",
                "option1_es": "Nada",
                "option2_en": "Straps, chains or other secure fasteners",
                "option2_es": "Correas, cadenas u otros amarres seguros",
                "option3_en": "Plastic cover",
                "option3_es": "Cubierta plástica",
                "correct_option": 2
            },
            {
                "question_en": "What does steering wheel vibration when braking indicate?",
                "question_es": "¿Qué indica una vibración del volante al frenar?",
                "option1_en": "Steering failure",
                "option1_es": "Fallo en la dirección",
                "option2_en": "Brake problems",
                "option2_es": "Problemas en los frenos",
                "option3_en": "Poor alignment",
                "option3_es": "Mal alineación",
                "correct_option": 2
            },
            {
                "question_en": "What should you check at the start of each day?",
                "question_es": "¿Qué debe revisar al inicio de cada día?",
                "option1_en": "Only tires",
                "option1_es": "Solo los neumáticos",
                "option2_en": "Entire vehicle: lights, brakes, tires, steering",
                "option2_es": "Todo el vehículo: luces, frenos, neumáticos, dirección",
                "option3_en": "Only fuel level",
                "option3_es": "Solo nivel de combustible",
                "correct_option": 2
            },
            {
                "question_en": "What is a sign of dangerous fatigue?",
                "question_es": "¿Cuál es una señal de fatiga peligrosa?",
                "option1_en": "Hunger",
                "option1_es": "Hambre",
                "option2_en": "Frequent blinking and not remembering the last few kilometers",
                "option2_es": "Pestañeo frecuente y no recordar los últimos kilómetros",
                "option3_en": "Leg pain",
                "option3_es": "Dolor de piernas",
                "correct_option": 2
            },
            {
                "question_en": "What is the best time to reduce speed in a curve?",
                "question_es": "¿Cuál es el mejor momento para reducir la velocidad en una curva?",
                "option1_en": "At the end of the curve",
                "option1_es": "Al final de la curva",
                "option2_en": "Before entering",
                "option2_es": "Antes de entrar",
                "option3_en": "Right in the middle",
                "option3_es": "Justo en la mitad",
                "correct_option": 2
            },
            {
                "question_en": "What should you do if you start to skid?",
                "question_es": "¿Qué debe hacer si comienza a patinar (derrapar)?",
                "option1_en": "Brake hard",
                "option1_es": "Frenar fuerte",
                "option2_en": "Release accelerator and turn gently",
                "option2_es": "Soltar el acelerador y girar suavemente",
                "option3_en": "Turn on lights",
                "option3_es": "Encender luces",
                "correct_option": 2
            },
            {
                "question_en": "What is a DOT inspection?",
                "question_es": "¿Qué es una inspección del DOT?",
                "option1_en": "Tax inspection",
                "option1_es": "Inspección de impuestos",
                "option2_en": "Mandatory safety and mechanical review",
                "option2_es": "Revisión obligatoria de seguridad y mecánica",
                "option3_en": "Satisfaction survey",
                "option3_es": "Encuesta de satisfacción",
                "correct_option": 2
            },
            {
                "question_en": "What to do if you see smoke coming from the dashboard?",
                "question_es": "¿Qué hacer si ve humo saliendo del tablero?",
                "option1_en": "Continue to a gas station",
                "option1_es": "Continuar hasta una gasolinera",
                "option2_en": "Stop immediately and evacuate",
                "option2_es": "Detenerse inmediatamente y evacuar",
                "option3_en": "Turn on air conditioning",
                "option3_es": "Encender el aire acondicionado",
                "correct_option": 2
            },
            {
                "question_en": "What determines vehicle stability in a curve?",
                "question_es": "¿Qué determina la estabilidad de un vehículo en curva?",
                "option1_en": "Driver weight",
                "option1_es": "El peso del conductor",
                "option2_en": "Speed and center of gravity",
                "option2_es": "La velocidad y centro de gravedad",
                "option3_en": "Windshield size",
                "option3_es": "Tamaño del parabrisas",
                "correct_option": 2
            },
            {
                "question_en": "When should the driver get out to check the cargo?",
                "question_es": "¿Cuándo debe bajarse el conductor para revisar la carga?",
                "option1_en": "When passing through tolls",
                "option1_es": "Al pasar por peajes",
                "option2_en": "Before, during and after the trip",
                "option2_es": "Antes, durante y después del viaje",
                "option3_en": "Never",
                "option3_es": "Nunca",
                "correct_option": 2
            },
            {
                "question_en": "What does it mean if an inspector places a vehicle 'out of service'?",
                "question_es": "¿Qué significa si un inspector coloca un vehículo 'fuera de servicio'?",
                "option1_en": "That it can travel slower",
                "option1_es": "Que puede viajar más lento",
                "option2_en": "That it cannot operate until a serious defect is corrected",
                "option2_es": "Que no puede operar hasta que se corrija un defecto grave",
                "option3_en": "Just a warning",
                "option3_es": "Solo advertencia",
                "correct_option": 2
            },
            {
                "question_en": "What causes 'brake fade'?",
                "question_es": "¿Qué causa el 'frenado en ráfagas'?",
                "option1_en": "Good control",
                "option1_es": "Buen control",
                "option2_en": "Loss of air pressure and overheating",
                "option2_es": "Pérdida de presión de aire y sobrecalentamiento",
                "option3_en": "Improved stability",
                "option3_es": "Mejora de estabilidad",
                "correct_option": 2
            },
            {
                "question_en": "What should you do when crossing a railroad track with a long trailer?",
                "question_es": "¿Qué debe hacer al cruzar una vía ferroviaria con un remolque largo?",
                "option1_en": "Go fast",
                "option1_es": "Ir rápido",
                "option2_en": "Cross in a straight line and without stopping",
                "option2_es": "Cruzarlo en línea recta y sin detenerse",
                "option3_en": "Reverse first",
                "option3_es": "Dar reversa primero",
                "correct_option": 2
            },
            {
                "question_en": "What should you do if the steering wheel vibrates abnormally while driving?",
                "question_es": "¿Qué debe hacer si el volante vibra anormalmente al conducir?",
                "option1_en": "Accelerate more",
                "option1_es": "Acelerar más",
                "option2_en": "Stop and check steering or suspension",
                "option2_es": "Detenerse y revisar dirección o suspensión",
                "option3_en": "Ignore it",
                "option3_es": "Ignorarlo",
                "correct_option": 2
            },
            {
                "question_en": "What should you avoid when driving in a storm?",
                "question_es": "¿Qué debe evitar cuando conduce en una tormenta?",
                "option1_en": "Lights on",
                "option1_es": "Luces encendidas",
                "option2_en": "Sudden braking and excessive speed",
                "option2_es": "Frenado repentino y exceso de velocidad",
                "option3_en": "Following trucks",
                "option3_es": "Seguir camiones",
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
        print(f"\n🎉 Successfully added {added_count} questions to 'General Knowledge' topic!")
        
    except Exception as e:
        print(f"❌ Error adding questions: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_general_knowledge_questions() 