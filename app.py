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
# def question_loop():
#
# def result_summary():