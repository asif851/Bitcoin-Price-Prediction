import random

print("Welcome to the Number Guessing Game!")
number_to_guess = random.randint(1, 10)
attempts = 0
    
while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1
            
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
