from dotenv import load_dotenv, dotenv_values

load_dotenv()
config = dotenv_values(".env")

CREATE DATABASE IF NOT EXISTS quiz_db;
USE quiz_db;

CREATE TABLE IF NOT EXISTS games (
    id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    question_TEXT TEXT NOT NULL,
    option_a VARCHAR(255) NOT NULL,
    option_b VARCHAR(255) NOT NULL,
    option_c VARCHAR(255) NOT NULL,
    option_d VARCHAR(255) NOT NULL,
    correct_index INT NOT NULL CHECK ( correct_index BETWEEN 0 AND 3),
    FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
);

# stored procedures