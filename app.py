import json
import random

questions = []
try:
    with open("questions.json", "r") as file:
        data = json.load(file)
        if "games" in data and isinstance(data["games"], list):
            questions = data["games"]
        else:
            print("No games found in JSON")
            exit(1)
except FileNotFoundError:
    print("File 'questions.json' not found!")
    exit(1)
except json.JSONDecodeError:
    print("Invalid JSON format!")
    exit(1)


def main_menu(games):
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


def question_loop(selected):
    score = 0
    wrong_answers = []
    letters = ["A", "B", "C", "D"]

    if selected != -1:
        selected_game = data["games"][selected - 1]["questions"]
    else:
        all_questions = []
        for game in data["games"]:
            all_questions.extend(game["questions"])
        random.shuffle(all_questions)
        selected_game = all_questions[:20]

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


if __name__ == "__main__":
    if not questions:
        print("No games to play. Exiting.")
    else:
        selected = main_menu(questions)
        if selected is None:
            print("Goodbye!")
        else:
            mode = "Mixed mode selected!" if selected == -1 else f"You selected game #{selected}"
            print(mode)
            question_loop(selected)
