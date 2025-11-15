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

    letters = ["A", "B", "C", "D"]

    for q in questions:
        print("\n" + q["question"])

        for i, answer in enumerate(q["content"]):
            print(f"{letters[i]}. {answer}")

        while True:
            user_input = input("\nYour answer (A-D): ").strip().upper()

            if user_input in letters:
                break
            else:
                print("gInvalid input. Please enter only A, B, C, or D.")

        chosen_index = letters.index(user_input)

        if chosen_index == q["correct"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            wrong_answers.append({
                "question": q["question"],
                "chosen": user_input,
                "correct": letters[q["correct"]],
                "correct_text": q["content"][q["correct"]]
            })

question_loop(questions)
#
# def result_summary()