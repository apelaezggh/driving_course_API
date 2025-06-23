from sqlalchemy import text
from .database import engine

def check_topic_questions():
    with engine.connect() as connection:
        try:
            # Get all topics with their question counts
            result = connection.execute(text("""
                SELECT 
                    t.id,
                    t.name_es,
                    t.name_en,
                    t.quiz_size,
                    t.target_quiz_size,
                    COUNT(q.id) as question_count
                FROM topics t
                LEFT JOIN questions q ON t.id = q.topic_id
                GROUP BY t.id, t.name_es, t.name_en, t.quiz_size, t.target_quiz_size
                ORDER BY t.name_es
            """))
            
            print("=== VERIFICACIÓN DE PREGUNTAS POR TEMA ===")
            print(f"{'ID':<3} {'Nombre':<40} {'Target':<6} {'Actual':<6} {'Preguntas':<10}")
            print("-" * 75)
            
            topics_data = []
            for row in result:
                topic_id = row[0]
                name_es = row[1]
                name_en = row[2]
                quiz_size = row[3] or 0
                target_quiz_size = row[4] or 10
                question_count = row[5]
                
                print(f"{topic_id:<3} {name_es:<40} {target_quiz_size:<6} {quiz_size:<6} {question_count:<10}")
                topics_data.append({
                    'id': topic_id,
                    'name_es': name_es,
                    'name_en': name_en,
                    'quiz_size': quiz_size,
                    'target_quiz_size': target_quiz_size,
                    'question_count': question_count
                })
            
            print("\n=== ANÁLISIS ===")
            for topic in topics_data:
                if topic['question_count'] == 0:
                    print(f"❌ {topic['name_es']}: Sin preguntas disponibles")
                elif topic['question_count'] < topic['target_quiz_size']:
                    print(f"⚠️  {topic['name_es']}: Necesita {topic['target_quiz_size']} pero tiene {topic['question_count']} preguntas")
                else:
                    print(f"✅ {topic['name_es']}: OK ({topic['question_count']} >= {topic['target_quiz_size']})")
            
            return topics_data
            
        except Exception as e:
            print(f"Error checking topics: {e}")

if __name__ == "__main__":
    check_topic_questions() 