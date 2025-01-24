import random

from GuessingGame.guess_the_number_logo import guess_the_number_logo

# print(guess_the_number_logo)
numbers = []

for i in range(1, 101):
    numbers.append(i)


num = int(random.choice(numbers))

print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.\n")
attempts = ""
difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
while 'easy' != difficulty != 'hard':
    difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
if difficulty == 'hard':
    attempts = 5
while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if not guess.is_integer():
        guess = int(input("Make a guess: "))
    if  guess > num :
        attempts -= 1
        print("Too high")
        if attempts >= 1:
            print("Guess again.")
    elif guess < num:
        attempts -= 1
        print("Too low")
        if attempts >= 1:
            print("Guess again.")
    elif guess == num:
        print(f"You got it! The answer was {guess}!")
        break

    else:
        print("try again")



