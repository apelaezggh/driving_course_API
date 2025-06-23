from sqlalchemy import text
from .database import engine

def fix_quiz_sizes():
    with engine.connect() as connection:
        try:
            # First, let's see the current state
            print("=== ESTADO ACTUAL ===")
            result = connection.execute(text("""
                SELECT 
                    t.id,
                    t.name_es,
                    t.quiz_size,
                    COUNT(q.id) as question_count
                FROM topics t
                LEFT JOIN questions q ON t.id = q.topic_id
                GROUP BY t.id, t.name_es, t.quiz_size
                ORDER BY t.name_es
            """))
            
            topics_to_update = []
            for row in result:
                topic_id = row[0]
                name_es = row[1]
                current_quiz_size = row[2] or 10
                question_count = row[3]
                
                print(f"Tema: {name_es}")
                print(f"  - Quiz size actual: {current_quiz_size}")
                print(f"  - Preguntas disponibles: {question_count}")
                
                # Determine the appropriate quiz_size
                if question_count == 0:
                    # No questions available, set to 0 to disable quiz
                    new_quiz_size = 0
                    print(f"  - Nuevo quiz size: {new_quiz_size} (sin preguntas)")
                elif question_count < current_quiz_size:
                    # Not enough questions, set to available count
                    new_quiz_size = question_count
                    print(f"  - Nuevo quiz size: {new_quiz_size} (ajustado a preguntas disponibles)")
                else:
                    # Enough questions, keep current size
                    new_quiz_size = current_quiz_size
                    print(f"  - Nuevo quiz size: {new_quiz_size} (sin cambios)")
                
                print()
                
                if new_quiz_size != current_quiz_size:
                    topics_to_update.append({
                        'id': topic_id,
                        'name_es': name_es,
                        'old_size': current_quiz_size,
                        'new_size': new_quiz_size
                    })
            
            # Update the quiz_sizes
            if topics_to_update:
                print("=== ACTUALIZANDO QUIZ SIZES ===")
                for topic in topics_to_update:
                    connection.execute(text("""
                        UPDATE topics 
                        SET quiz_size = :new_size 
                        WHERE id = :topic_id
                    """), {
                        "new_size": topic['new_size'],
                        "topic_id": topic['id']
                    })
                    print(f"✅ {topic['name_es']}: {topic['old_size']} → {topic['new_size']}")
                
                connection.commit()
                print("\n✅ Quiz sizes actualizados exitosamente!")
            else:
                print("\n✅ No se necesitan cambios en los quiz sizes.")
            
            # Show final state
            print("\n=== ESTADO FINAL ===")
            final_result = connection.execute(text("""
                SELECT 
                    t.name_es,
                    t.quiz_size,
                    COUNT(q.id) as question_count
                FROM topics t
                LEFT JOIN questions q ON t.id = q.topic_id
                GROUP BY t.id, t.name_es, t.quiz_size
                ORDER BY t.name_es
            """))
            
            for row in final_result:
                name_es = row[0]
                quiz_size = row[1] or 0
                question_count = row[2]
                
                if quiz_size == 0:
                    status = "❌ Quiz deshabilitado (sin preguntas)"
                elif question_count >= quiz_size:
                    status = "✅ Quiz habilitado"
                else:
                    status = "⚠️ Quiz habilitado pero con pocas preguntas"
                
                print(f"{name_es}: {quiz_size} preguntas por quiz - {status}")
            
        except Exception as e:
            print(f"Error fixing quiz sizes: {e}")
            connection.rollback()

if __name__ == "__main__":
    fix_quiz_sizes() 