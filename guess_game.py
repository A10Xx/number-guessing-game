# guess_game.py

import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("🔽 Too low!")
            elif guess > number_to_guess:
                print("🔼 Too high!")
            else:
                print(f"✅ Correct! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    play_game()
