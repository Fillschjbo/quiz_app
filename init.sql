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