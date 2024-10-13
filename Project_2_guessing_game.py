import random

print("Welcome to the Guessing Game App \n")

computer_choice = random.randint(1,101)
user_choice = 0

while computer_choice != user_choice:
    user_choice = int(input("Guess a number between 1-100 \n"))
    if user_choice > computer_choice:
        print("Too high")
    elif user_choice < computer_choice:
        print("Too low")
print("Congratulations! You won")
