import json

questions=[]

try:
    with open ("questions.json", "r") as file:
        data = json.load(file)
        questions = data
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Decode error")

# def main_menu():
#

questions = data["games"][0]["questions"]

def question_loop(questions):
    score = 0
    wrong_answers = []

    for q in questions:
        print("\n" + q["question"])
        for i, answer in enumerate(q["content"], start=1):
                print(f"{i}. {answer}")

        user_input = input("\nType your answer (1-4): ")

        if user_input.lower() in ("q", "quit"):
            print("Quitting early...")
            break

        if user_input.isdigit() and int(user_input) - 1 == q["correct"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

question_loop(questions)
#
# def result_summary()