from sqlalchemy import text
from .database import engine

def fix_target_quiz_sizes():
    with engine.connect() as connection:
        try:
            print("=== CORRIGIENDO TARGET QUIZ SIZES ===")
            
            # Fix specific topics that have incorrect target_quiz_size
            corrections = {
                "Cisterna": 20,  # Should be 20, not 10
                "Pasajeros": 20  # Should be 20, not 10
            }
            
            for topic_name, correct_target_size in corrections.items():
                # First, let's see the current value
                current_result = connection.execute(text("""
                    SELECT id, name_es, target_quiz_size 
                    FROM topics 
                    WHERE name_es LIKE :topic_name
                """), {"topic_name": f"%{topic_name}%"}).fetchone()
                
                if current_result:
                    topic_id = current_result[0]
                    name_es = current_result[1]
                    current_target_size = current_result[2]
                    
                    print(f"Tema: {name_es}")
                    print(f"  - Target quiz size actual: {current_target_size}")
                    print(f"  - Target quiz size correcto: {correct_target_size}")
                    
                    if current_target_size != correct_target_size:
                        # Update the target_quiz_size
                        connection.execute(text("""
                            UPDATE topics 
                            SET target_quiz_size = :correct_size 
                            WHERE id = :topic_id
                        """), {
                            "correct_size": correct_target_size,
                            "topic_id": topic_id
                        })
                        print(f"  ✅ Actualizado: {current_target_size} → {correct_target_size}")
                    else:
                        print(f"  ✅ Ya está correcto")
                else:
                    print(f"❌ Tema no encontrado: {topic_name}")
                
                print()
            
            connection.commit()
            print("✅ Target quiz sizes corregidos exitosamente!")
            
            # Show final state
            print("\n=== ESTADO FINAL ===")
            final_result = connection.execute(text("""
                SELECT 
                    t.name_es,
                    t.target_quiz_size,
                    t.quiz_size,
                    COUNT(q.id) as question_count
                FROM topics t
                LEFT JOIN questions q ON t.id = q.topic_id
                GROUP BY t.id, t.name_es, t.target_quiz_size, t.quiz_size
                ORDER BY t.name_es
            """))
            
            for row in final_result:
                name_es = row[0]
                target_quiz_size = row[1] or 10
                quiz_size = row[2] or 0
                question_count = row[3]
                
                print(f"{name_es}:")
                print(f"  - Target quiz size: {target_quiz_size} (debe tener)")
                print(f"  - Available questions: {question_count} (disponibles)")
                print(f"  - Current quiz size: {quiz_size} (actual)")
                
                if question_count == 0:
                    status = "❌ Sin preguntas"
                elif question_count >= target_quiz_size:
                    status = "✅ Suficientes preguntas"
                else:
                    status = f"⚠️ Necesita {target_quiz_size - question_count} preguntas más"
                
                print(f"  - Status: {status}")
                print()
            
        except Exception as e:
            print(f"Error fixing target quiz sizes: {e}")
            connection.rollback()

if __name__ == "__main__":
    fix_target_quiz_sizes() 