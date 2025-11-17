import json
import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'charset': os.getenv('DB_CHARSET', 'utf8mb4'),
    'autocommit': True,
    'raise_on_warnings': True
}

def json_import(file_path = "questions.json"):
    missing = [key for key in ['DB_HOST', 'DB_USER', 'DB_PASSWORD', 'DB_NAME', 'DB_CHARSET'] if not os.getenv(key)]
    if missing:
        print("Missing environment variables: {}".format(missing))
        return

    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        with open(file_path, 'r', encoding='utf8mb4') as f:
            data = json.load(f)

        for game_indx, game in enumerate(data.get("games", []), start=1):
            title = game.get("title", f"Game {game_indx}")
            cursor.execute("INSERT INTO games (title) VALUES (%s)", (title,))
            game_id = cursor.lastrowid


if __name__ == "__main__":
    json_import()