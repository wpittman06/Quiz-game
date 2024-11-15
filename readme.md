This was a quiz game project to have practical python skill application. 

Tools:
 - Python
 - Youtube

I used Dictionaries to create my quiz base.
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


Randomization of Questions:

I used random.sample(questions, len(questions)) to randomize the order of questions.
Randomization of Options:

I used random.sample(question["options"], len(question["options"])) to randomize the order of answer options.

random.sample(sequence, k):

This function returns a new list with k unique elements chosen from the input sequence, in a random order.
By setting k to the length of the list, we effectively shuffle the entire list.
next():

This function is used to find the correct option in the shuffled list of options using a generator expression (opt.startswith(question["answer"])).

Continued developement
    I would like to instead of manually creating the quiz, either A connect to a quiz API or B make a database with "X" number of questions and the quiz can filter through a database of questions.