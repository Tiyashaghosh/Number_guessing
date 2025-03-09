import random
# from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def check_answer(guessed_number,answer,turns):
    if guessed_number > answer:
        print("Too High.")
        return turns -1
    elif guessed_number < answer:
        print("Too Low.")
        return turns -1
    elif guessed_number == answer:
        print(f"You got it! The number was {answer}")

def choose_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS

def game():
    # print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = choose_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))

        turns = check_answer(guess,answer,turns)

        if turns == 0:
            print("You have run out of guesses. You lost.")
            return False
        elif answer != guess :
            print("Guess Again.")

game()