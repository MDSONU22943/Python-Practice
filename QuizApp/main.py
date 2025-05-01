def ask_question(question, options, correct_option):
    print(question)
    for key, value in options.items():
        print(f"{key}: {value}")
    answer = input("Please select an option: ").upper()
    return answer == correct_option


def run_quiz():
    score = 0
    questions = [
        {
            "question": "What is the capital of France?",
            "options": {
                "A": "Berlin",
                "B": "Madrid",
                "C": "Paris",
                "D": "Rome"
            },
            "correct_option": "C"
        },
        {
            "question": "What is 2 + 2?",
            "options": {
                "A": "3",
                "B": "4",
                "C": "5",
                "D": "6"
            },
            "correct_option": "B"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": {
                "A": "Earth",
                "B": "Mars",
                "C": "Jupiter",
                "D": "Saturn"
            },
            "correct_option": "C"
        },
        {
            "question": "Which data type is immutable in Python?",
            "options": {
                "A": "List",
                "B": "Tuple",
                "C": "Set",
                "D": "Dictionary"
            },
            "correct_option": "B"
        },
        {
            "question": "What keyword is used to define a function in Python?",
            "options": {
                "A": "func",
                "B": "define",
                "C": "def",
                "D": "function"
            },
            "correct_option": "C"
        }
    ]
    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_option"]):
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is: {score}/{len(questions)}")

run_quiz()
# This code defines a simple quiz application that asks the user a series of questions and keeps track of their score.  