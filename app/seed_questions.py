from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from app import models, auth

def seed_database():
    db = SessionLocal()
    try:
        # Create roles
        admin_role = db.query(models.Role).filter(models.Role.name == "admin").first()
        if not admin_role:
            admin_role = models.Role(name="admin")
            db.add(admin_role)
            db.commit()
            db.refresh(admin_role)
        
        user_role = db.query(models.Role).filter(models.Role.name == "user").first()
        if not user_role:
            user_role = models.Role(name="user")
            db.add(user_role)
            db.commit()
            db.refresh(user_role)
        
        # Create admin user
        admin_user = db.query(models.User).filter(models.User.username == "admin").first()
        if not admin_user:
            hashed_password = auth.get_password_hash("admin123")
            admin_user = models.User(
                email="admin@drivingcourse.com",
                username="admin",
                hashed_password=hashed_password
            )
            admin_user.roles.append(admin_role)
            db.add(admin_user)
            db.commit()
            db.refresh(admin_user)
            print("Admin user created: admin/admin123")
        
        # Create test user
        test_user = db.query(models.User).filter(models.User.username == "testuser").first()
        if not test_user:
            hashed_password = auth.get_password_hash("test123")
            test_user = models.User(
                email="test@drivingcourse.com",
                username="testuser",
                hashed_password=hashed_password
            )
            test_user.roles.append(user_role)
            db.add(test_user)
            db.commit()
            db.refresh(test_user)
            print("Test user created: testuser/test123")
        
        # Create topics
        topics_data = [
            {
                "name_en": "Traffic Signs",
                "name_es": "Señales de Tránsito",
                "description_en": "Learn about traffic signs and their meanings",
                "description_es": "Aprende sobre las señales de tránsito y sus significados"
            },
            {
                "name_en": "Traffic Rules",
                "name_es": "Reglas de Tránsito",
                "description_en": "Basic traffic rules and regulations",
                "description_es": "Reglas básicas de tránsito y regulaciones"
            },
            {
                "name_en": "Road Safety",
                "name_es": "Seguridad Vial",
                "description_en": "Road safety practices and guidelines",
                "description_es": "Prácticas y guías de seguridad vial"
            },
            {
                "name_en": "Vehicle Control",
                "name_es": "Control del Vehículo",
                "description_en": "Vehicle control and handling techniques",
                "description_es": "Técnicas de control y manejo del vehículo"
            },
            {
                "name_en": "Emergency Procedures",
                "name_es": "Procedimientos de Emergencia",
                "description_en": "What to do in emergency situations",
                "description_es": "Qué hacer en situaciones de emergencia"
            },
            {
                "name_en": "Parking",
                "name_es": "Estacionamiento",
                "description_en": "Parking rules and techniques",
                "description_es": "Reglas y técnicas de estacionamiento"
            },
            {
                "name_en": "Highway Driving",
                "name_es": "Conducción en Autopista",
                "description_en": "Highway driving rules and safety",
                "description_es": "Reglas y seguridad para conducir en autopista"
            },
            {
                "name_en": "Night Driving",
                "name_es": "Conducción Nocturna",
                "description_en": "Night driving safety and techniques",
                "description_es": "Seguridad y técnicas para conducir de noche"
            },
            {
                "name_en": "Weather Conditions",
                "name_es": "Condiciones Climáticas",
                "description_en": "Driving in different weather conditions",
                "description_es": "Conducir en diferentes condiciones climáticas"
            }
        ]
        
        topics = []
        for topic_data in topics_data:
            topic = db.query(models.Topic).filter(
                models.Topic.name_en == topic_data["name_en"]
            ).first()
            if not topic:
                topic = models.Topic(**topic_data)
                db.add(topic)
                db.commit()
                db.refresh(topic)
                print(f"Created topic: {topic.name_en}")
            topics.append(topic)
        
        # Create questions for each topic
        questions_data = {
            "Traffic Signs": [
                {
                    "question_en": "What does a red octagon sign mean?",
                    "question_es": "¿Qué significa una señal octagonal roja?",
                    "option1_en": "Stop",
                    "option1_es": "Pare",
                    "option2_en": "Yield",
                    "option2_es": "Ceda el paso",
                    "option3_en": "Speed limit",
                    "option3_es": "Límite de velocidad",
                    "correct_option": 1
                },
                {
                    "question_en": "What does a yellow triangle sign indicate?",
                    "question_es": "¿Qué indica una señal triangular amarilla?",
                    "option1_en": "Warning",
                    "option1_es": "Advertencia",
                    "option2_en": "Prohibition",
                    "option2_es": "Prohibición",
                    "option3_en": "Information",
                    "option3_es": "Información",
                    "correct_option": 1
                }
            ],
            "Traffic Rules": [
                {
                    "question_en": "What is the speed limit in residential areas?",
                    "question_es": "¿Cuál es el límite de velocidad en áreas residenciales?",
                    "option1_en": "30 mph",
                    "option1_es": "30 mph",
                    "option2_en": "50 mph",
                    "option2_es": "50 mph",
                    "option3_en": "70 mph",
                    "option3_es": "70 mph",
                    "correct_option": 1
                },
                {
                    "question_en": "When should you use your turn signals?",
                    "question_es": "¿Cuándo debes usar las luces direccionales?",
                    "option1_en": "Only when turning left",
                    "option1_es": "Solo al girar a la izquierda",
                    "option2_en": "Before changing lanes or turning",
                    "option2_es": "Antes de cambiar de carril o girar",
                    "option3_en": "Only at night",
                    "option3_es": "Solo de noche",
                    "correct_option": 2
                }
            ],
            "Road Safety": [
                {
                    "question_en": "What is the safe following distance?",
                    "question_es": "¿Cuál es la distancia segura de seguimiento?",
                    "option1_en": "1 second",
                    "option1_es": "1 segundo",
                    "option2_en": "2-3 seconds",
                    "option2_es": "2-3 segundos",
                    "option3_en": "5 seconds",
                    "option3_es": "5 segundos",
                    "correct_option": 2
                },
                {
                    "question_en": "What should you do at a yellow light?",
                    "question_es": "¿Qué debes hacer en una luz amarilla?",
                    "option1_en": "Speed up to cross",
                    "option1_es": "Acelerar para cruzar",
                    "option2_en": "Stop if safe to do so",
                    "option2_es": "Parar si es seguro hacerlo",
                    "option3_en": "Ignore it",
                    "option3_es": "Ignorarla",
                    "correct_option": 2
                }
            ]
        }
        
        for topic_name, questions in questions_data.items():
            topic = db.query(models.Topic).filter(models.Topic.name_en == topic_name).first()
            if topic:
                for q_data in questions:
                    existing_question = db.query(models.Question).filter(
                        models.Question.question_en == q_data["question_en"]
                    ).first()
                    if not existing_question:
                        question = models.Question(topic_id=topic.id, **q_data)
                        db.add(question)
                        print(f"Created question for {topic_name}")
        
        # Grant some permissions to test user
        test_user = db.query(models.User).filter(models.User.username == "testuser").first()
        if test_user:
            # Grant permission to first 3 topics (Traffic Signs, Traffic Rules, Road Safety)
            topic_names_to_grant = ["Traffic Signs", "Traffic Rules", "Road Safety"]
            for topic_name in topic_names_to_grant:
                topic = db.query(models.Topic).filter(models.Topic.name_en == topic_name).first()
                if topic:
                    existing_permission = db.query(models.UserTopicPermission).filter(
                        models.UserTopicPermission.user_id == test_user.id,
                        models.UserTopicPermission.topic_id == topic.id
                    ).first()
                    if not existing_permission:
                        permission = models.UserTopicPermission(
                            user_id=test_user.id,
                            topic_id=topic.id,
                            granted_by=admin_user.id
                        )
                        db.add(permission)
                        print(f"Granted permission to topic '{topic_name}' for testuser")
        
        db.commit()
        print("Database seeded successfully!")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database() 