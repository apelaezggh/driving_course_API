from sqlalchemy import text
from .database import engine

def add_target_quiz_size():
    with engine.connect() as connection:
        try:
            # Add target_quiz_size column to topics table
            connection.execute(text("""
                ALTER TABLE topics 
                ADD COLUMN target_quiz_size INTEGER DEFAULT 10
            """))
            connection.commit()
            print("Successfully added target_quiz_size column to topics table")
            
            # Set the target quiz sizes based on the requirements
            target_sizes = {
                "Operación de Vehículos Comerciales de Texas": 20,
                "Conocimientos Generales": 50,
                "Frenos de Aire": 25,
                "Vehículos Combinados": 20,
                "Materiales Peligrosos": 30,
                "Cisterna": 20,
                "Dobles o Triples": 20,
                "Pasajeros": 20,
                "Autobús Escolar": 20
            }
            
            for topic_name, target_size in target_sizes.items():
                result = connection.execute(text("""
                    UPDATE topics 
                    SET target_quiz_size = :target_size 
                    WHERE name_es = :topic_name
                """), {"target_size": target_size, "topic_name": topic_name})
                
                if result.rowcount > 0:
                    print(f"Updated {topic_name} with target_quiz_size: {target_size}")
                else:
                    print(f"Topic not found: {topic_name}")
            
            connection.commit()
            print("Target quiz sizes updated successfully!")
            
            # Show the final state
            print("\n=== ESTADO FINAL ===")
            final_result = connection.execute(text("""
                SELECT 
                    t.name_es,
                    t.quiz_size,
                    t.target_quiz_size,
                    COUNT(q.id) as question_count
                FROM topics t
                LEFT JOIN questions q ON t.id = q.topic_id
                GROUP BY t.id, t.name_es, t.quiz_size, t.target_quiz_size
                ORDER BY t.name_es
            """))
            
            for row in final_result:
                name_es = row[0]
                quiz_size = row[1] or 0
                target_quiz_size = row[2] or 10
                question_count = row[3]
                
                print(f"{name_es}:")
                print(f"  - Target quiz size: {target_quiz_size} (debe tener)")
                print(f"  - Available questions: {question_count} (disponibles)")
                print(f"  - Current quiz size: {quiz_size} (actual)")
                
                if question_count >= target_quiz_size:
                    status = "✅ Suficientes preguntas"
                elif question_count > 0:
                    status = "⚠️ Preguntas insuficientes"
                else:
                    status = "❌ Sin preguntas"
                
                print(f"  - Status: {status}")
                print()
            
        except Exception as e:
            print(f"Error during migration: {e}")
            connection.rollback()

if __name__ == "__main__":
    add_target_quiz_size() 