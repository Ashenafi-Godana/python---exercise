import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f"Guess a number from 1 to {x}: "))
        if guess < random_number:
            print("Too low")
        elif guess > random_number:
            print("Too high")
    print("Yay, congrats you guessed the correct number")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(
            'Is {guess} too low(l) or too high(h) or correct (c): ')
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
    print("Yay, correct. You guessed the correct number.")


computer_guess(10)
