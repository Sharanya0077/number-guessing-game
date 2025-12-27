import random

print("Welcome to the Number Guessing Game!")

#genenate a random number between 1 and 100
number = random.randint(1,100)
attempts = 0
MAX_ATTEMPTS = 10

while True:
    guess = int(input("Enter your guess(1-100):"))
    attempts += 1

    if guess> number:
        print("Lower please!")
    elif guess < number:
        print("Higher please!")
    else:
        print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
        break

    if attempts >= MAX_ATTEMPTS:
        print(f"Sorry, You,ve used all 10 attempts. You Lose!")
        print(f"The correct number was {number}.")
        break   
