import json

questions = []

try:
    with open ("questions.json", "r") as file:
        data = json.load(file)
        if "games" in data and isinstance(data["games"], list):
            questions = data["games"]
        else:
            print("No games found")
            exit(1)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Decode error")

def main_menu(games):
    if not games:
        print("No games found")
        return None

    else:
        print("\n" + "=" * 50)
        print("           QUIZ GAME - MAIN MENU")
        print("=" * 50)

        total_questions = 0
        for i, game in enumerate(games):
            count = len(game.get("questions", []))
            total_questions += count
            print(f"Game {i + 1}, ({count} questions)")

        print(f"M. All games mixed ({total_questions} questions)")
        print("-" * 50)

        choice = input(f"Choose 1-{len(games)} or M for mixed: ").strip()
        if choice.upper() == "M":
            return -1
        else:
            try:
                num = int(choice)
                if 1 <= num <= len(games):
                    return num
                else:
                    print("Invalid number! Try again.")
            except ValueError:
                print("Please enter a valid number or 'M'.")




# def question_loop():
#
# def result_summary():

if __name__ == "__main__":
    if not questions:
        print("No games to play. Exiting.")
    else:
        selected = main_menu(questions)

        if selected is None:
            print("Goodbye!")
        elif selected == -1:
            print("Mixed mode selected!")
            question_loop(selected)
        else:
            print(f"You selected game #{selected}")
            question_loop(selected)
