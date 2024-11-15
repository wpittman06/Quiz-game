import random

# List of quiz questions
questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "What is the primary language spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 5", "D. 7"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    }
]

# Function to run the quiz
def run_quiz(questions):
    # Randomize the order of questions
    randomized_questions = random.sample(questions, len(questions))
    score = 0

    for question in randomized_questions:
        print("\n" + question["prompt"])

        # Randomize the order of answer options
        randomized_options = random.sample(question["options"], len(question["options"]))
        
        # Display randomized options
        for option in randomized_options:
            print(option)

        # Get the user's answer
        answer = input("Enter your answer (A, B, C, D): ").upper()

        # Determine the correct answer based on the randomized options
        correct_option = next(opt for opt in randomized_options if opt.startswith(question["answer"]))

        # Check the answer
        if answer == correct_option[0]:
            print("Yay! You are correct!\n")
            score += 1
        else:
            print(f"That is incorrect. The correct answer was {correct_option}.\n")

    # Display the final score
    print(f"You got {score} out of {len(questions)} questions correct.")

# Run the quiz
run_quiz(questions)
