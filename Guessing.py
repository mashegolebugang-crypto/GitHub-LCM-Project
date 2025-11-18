import random

target = random.randint(0, 10)
print("guess a number between 0 and 10")

try:
    guess = int(input("enter your guess:"))
    if guess == target:
        print("numbers match! you guessed correctly!")
    elif guess > target:
        print("your guess is too high.")
    else:
        print("your guess is too low.")
    print("correct number was:", target)
except ValueError:
    print("error:please enter a valid number!")
    