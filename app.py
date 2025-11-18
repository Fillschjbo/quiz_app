import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv, dotenv_values

load_dotenv()
config = dotenv_values(".env")

def connect():
    try:
        connection = mysql.connector.connect(
            host=config['DB_HOST'],
            user=config['DB_USER'],
            password=config['DB_PASSWORD'],
            database=config['DB_NAME']
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        exit(1)


def main_menu(connection):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.callproc('get_games')
        games = []
        for result in cursor.stored_results():
            games = result.fetchall()

        if not games:
            print("No games available.")
            return None

        print("\n" + "=" * 50)
        print("           QUIZ GAME - MAIN MENU")
        print("=" * 50)

        total_questions = 0
        for i, game in enumerate(games):
            count = len(game.get("questions", []))
            total_questions += count
            print(f"{i + 1}. Game {i + 1} ({count} questions)")

        print(f"M. All games mixed ({total_questions} questions)")
        print("-" * 50)

        while True:
            choice = input(f"Choose 1-{len(games)} or M for mixed: ").strip()
            if choice.upper() == "M":
                return -1
            try:
                num = int(choice)
                if 1 <= num <= len(games):
                    return num
                else:
                    print("Invalid number! Try again.")
            except ValueError:
                print("Please enter a valid number or 'M'.")

    finally:
        cursor.close()

def question_loop(connection, selected):
    cursor = connection.cursor(dictionary=True)
    score = 0
    wrong_answers = []
    letters = ["A", "B", "C", "D"]

    try:
        if selected != -1:
            cursor.callproc('GetQuestionsForGame', [selected])
            for results in cursor.stored_results():
                rows = results.fetchall()
        else:
            cursor.execute("""
               SELECT question_text, option_a, option_b, option_c, option_d, correct_index
               FROM questions
               ORDER BY RAND() LIMIT 20
            """)
            rows = cursor.fetchall()

        selected_game = []

        for row in rows:
            selected_game.append({
                "question": row["question_text"],
                "content": [row["option_a"], row["option_b"], row["option_c"], row["option_d"]],
                "correct": row["correct_index"]
            })
        total_questions = len(selected_game)

        for q in selected_game:
            print("\n" + q["question"])
            content = q["content"]

            for i, answer in enumerate(content):
                print(f"{letters[i]}. {answer}")

            while True:
                user_input = input("\nYour answer (A-D): ").strip().upper()
                if user_input in letters:
                    break
                print("Invalid input. Please enter only A, B, C, or D.")

            chosen_index = letters.index(user_input)
            correct_index = q["correct"]

            if chosen_index == correct_index:
                print("Correct!")
                score += 1
            else:
                print("Wrong!")
                wrong_answers.append({
                    "question": q["question"],
                    "chosen": user_input,
                    "correct": correct_index,
                    "all_content": content
                })

            print("\n" + "=" * 50)

        show_results(total_questions, score, wrong_answers)

    finally:
        cursor.close()


def show_results(total_questions, score, wrong_answers):
    incorrect = total_questions - score
    percentage = round((score / total_questions) * 100) if total_questions > 0 else 0

    print("\n" + "=" * 60)
    print("                     RESULT SUMMARY")
    print("=" * 60)
    print(f"Total questions   : {total_questions}")
    print(f"Correct answers   : {score}")
    print(f"Incorrect answers : {incorrect}")
    print(f"Score             : {percentage}%")
    print("=" * 60)

    if wrong_answers:
        print("\nREVIEW OF QUESTIONS YOU GOT WRONG:\n")
        letters = ["A", "B", "C", "D"]
        for i, wa in enumerate(wrong_answers, 1):
            chosen_idx = letters.index(wa["chosen"])
            chosen_text = wa["all_content"][chosen_idx]
            correct_idx = wa["correct"]
            correct_letter = letters[correct_idx]
            correct_text = wa["all_content"][correct_idx]

            print(f"{i}. {wa['question']}")
            print(f"   You answered   : {wa['chosen']} ({chosen_text})")
            print(f"   Correct answer : {correct_letter} ({correct_text})")
            print("-" * 50)
    else:
        print("\nPerfect! You got every question right!")

    print("\nThanks for playing!\n")





if __name__ == "__main__":
    connection = connect()

    try:
        selected = main_menu(connection)
        if selected is None:
            print("Goodbye!")
        else:
            mode = "Mixed mode selected!" if selected == -1 else f"You selected game #{selected}"
            print(mode)
            question_loop(connection, selected)
    finally:
        connection.close()
