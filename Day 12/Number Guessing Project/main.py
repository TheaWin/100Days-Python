import random
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def difficulty_level():
    level_question = True
    while level_question:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == "easy":
            # level_question = False
            return EASY_LEVEL_TURNS
        elif level == "hard":
            # level_question = False
            return HARD_LEVEL_TURNS
        else:
            print("Please choose either 'easy' or 'hard'")

def check_answer(player_guess, correct_number, turns):
    """Checks answer against guess, returns the remaining number of turns."""
    if player_guess > correct_number:
        print("Too high.")
        return turns -1
    elif player_guess < correct_number:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it!. The answer was {correct_number}")

def game():
    print(art.logo)
    print(f"Welcome to the Number Guessing Game!\n"
          f"I'm thinking of a number between 1 and 100.")

    answer = random.randint(1,100)
    print(f"answer is {answer}")

    turns = difficulty_level()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()

