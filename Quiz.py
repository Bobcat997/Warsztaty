questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Who made PHP?: ": "C",
 "Is html a programming language?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1881", "B. 1991", "C. 2020", "D. 2007"],
          ["A. Elon Musk", "B. Mark Zuckerburg", "C. Rasmus Lerdorf", "D. Yukihiro Matsumoto"],
          ["A. False","B. of course", "C. True", "D. right"]]



def QUIZ():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for k in questions:
        print("-------------------------")
        print(k)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(k), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")

    if response.upper() == "YES":
        return True
    else:
        return False
# -------------------------

QUIZ()

while play_again():
    QUIZ()

print("See you next time!")

# -------------------------