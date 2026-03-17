import json
import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME', 'quiz_db'),
    'charset': 'utf8mb4',
    'autocommit': True,
    'raise_on_warnings': True
}

def import_json(file_path="questions.json"):
    required = ['DB_USER', 'DB_PASSWORD']
    missing = [k for k in required if not os.getenv(k)]
    if missing:
        print(f"ERROR: Missing environment variables: {', '.join(missing)}")
        print("   → Create a .env file in the project root with:")
        print("     DB_USER=quiz_user")
        print("     DB_PASSWORD=SecurePass123!")
        return

    try:
        print("Connecting to MySQL...")
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        print("Connected!")

        with open(file_path, 'r') as f:
            data = json.load(f)

        total_questions = 0
        for game_idx, game in enumerate(data.get("games", []), start=1):
            cursor.execute("INSERT INTO games (id) VALUES (DEFAULT)")
            game_id = cursor.lastrowid

            for q in game.get("questions", []):
                options = q["content"] + [""] * 4
                options = options[:4]

                correct_idx = q["correct"]
                if correct_idx >= 4:
                    print(f"Warning: question has correct_index {correct_idx} → clamping to 0")
                    correct_idx = 0

                cursor.execute("""
                    INSERT INTO questions 
                    (game_id, question_TEXT, option_a, option_b, option_c, option_d, correct_index)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (game_id, q["question"], *options, correct_idx))

                total_questions += 1

        conn.commit()
        print(f"SUCCESS! Imported {len(data.get('games', []))} games and {total_questions} questions.")

    except Error as e:
        print(f"MySQL Error: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    import_json()