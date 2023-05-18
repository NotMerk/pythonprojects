# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1": {
        "question": "What is the capital of Malaysia?",
        "answer": "Kuala Lumpur"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question4": {
        "question": "What is the capital of Philippines?",
        "answer": "Manila"
    },
    "question5": {
        "question": "What is the capital of Japan?",
        "answer": "Tokyo"
    },
    "question6": {
        "question": "What is the capital of Indonesia?",
        "answer": "Jakarta"
    },
    "question7": {
        "question": "What is the capital of Korea?",
        "answer": "Seoul"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer > ")

    if answer.lower() == value['answer'].lower():
        print("Correct!")
        score = score + 1
        print("Score > " + str(score))
        print("")
        print("")

    else:
        print("Wrong!")
        print("Correct Answer > " + value['answer'])
        print("Score > " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score / 7 * 100)) + "%")