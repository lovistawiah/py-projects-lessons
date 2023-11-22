import random
RANDOM_NUMBER = random.randint(1, 100)


def guess_message(high_or_low):
    return f"Too {high_or_low}.\nGuess again\n"


def guess(attempts: int, random_number: int):
    result = True
    high_or_low = ""
    while result:
        print(f"You have {attempts} attempts to guess the number")
        if attempts >0:
            ask_guess_number = int(input("Make a guess: "))
            if ask_guess_number > random_number:
                high_or_low = "high"
                print(guess_message(high_or_low))
            elif ask_guess_number < random_number:
                high_or_low = "low"
                print(guess_message( high_or_low))
            else:
                print("Your guess is correct")
                result = False
            attempts -= 1
        else:
            result = False
            print(f"You lost, the number was {random_number}.")


def ask_difficulty():
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty 'easy' or 'hard' ").lower()
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    return attempts

attempt_number = ask_difficulty()
guess(attempt_number,RANDOM_NUMBER)
