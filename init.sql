DROP DATABASE IF EXISTS quiz_db;

CREATE DATABASE quiz_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
USE quiz_db;

CREATE USER IF NOT EXISTS 'quiz_user'@'%' IDENTIFIED BY 'SecurePass123!';
GRANT ALL PRIVILEGES ON quiz_db.* TO 'quiz_user'@'%';
FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS games (
    id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    question_text TEXT NOT NULL,
    option_a VARCHAR(255) NOT NULL,
    option_b VARCHAR(255) NOT NULL,
    option_c VARCHAR(255) NOT NULL,
    option_d VARCHAR(255) NOT NULL,
    correct_index INT NOT NULL CHECK ( correct_index BETWEEN 0 AND 3),
    FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
);

# stored procedures

DELIMITER //
CREATE PROCEDURE get_games()
    BEGIN
        SELECT games.id, COUNT(questions.id) AS question_count
        FROM games
        LEFT JOIN questions ON games.id = questions.game_id
        GROUP BY games.id
        ORDER BY games.id;
    END //

CREATE PROCEDURE GetQuestionsForGame(IN gameId INT)
    BEGIN
        SELECT question_text, option_a, option_b, option_c, option_d, correct_index
        FROM questions
        WHERE game_id = gameId;
    END //
DELIMITER ;