import random

number = random.randint(1, 99)

guess = int(input("Enter a guess within the range 1 to 99: "))

while number != guess:
    if guess < number:
        print("Try again,your guess is too low")
        guess = int(input("Enter a new guess: "))
    elif guess > number:
        print("Try again,your guess is too high")
        guess = int(input("Enter a new guess: "))

print("Congrats! The number was: ", guess)
