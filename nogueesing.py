import random

def guess_number():
  #A simple number guessing game with manual input handling and a 3-attempt limit
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0
    max_attempts = 3

    print("🎯 Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100. You have 3 attempts!")

    while attempts < max_attempts:
        try:
            import sys
            if sys.stdin.isatty():
                guess = int(input("Enter your guess: "))
            else:
                print("⚠️ Input is not interactive. Please run this script in a terminal.")
                break
            
            attempts += 1

            if guess < number_to_guess:
                print("🔼 Too low! Try again.")
            elif guess > number_to_guess:
                print("🔽 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                return  # Exit the function when guessed correctly
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.")
    
    print(f"❌ Out of attempts! The correct number was {number_to_guess}.")

if __name__ == "__main__":
    guess_number()
