import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
ANSWER = random.randint(1, 100)

def number_guessing():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    available_times = 0
    if difficulty == "easy":
        available_times = 10
    else:
        available_times = 5
    print(f"You have {available_times} attempts remaining to guess the number.")

    game_over = False
    while not game_over:
        guess_num = int(input("Make a guess: "))
        if guess_num > ANSWER:
            print("Too high.\nGuess again.")
            available_times -= 1
            print(f"You have {available_times} attempts remaining to guess the number.")
        elif guess_num < ANSWER:
            print("Too low.\nGuess again.")
            available_times -= 1
            print(f"You have {available_times} attempts remaining to guess the number.")
        else:
            print(f"You got it! The answer was {ANSWER}")
            game_over = True
        if available_times == 0:
            game_over = True
            print("You've run out of guesses. Refresh the page to run again.")

number_guessing()