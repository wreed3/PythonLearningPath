import random


user_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

choices = ["Rock", "Paper", "Scissors"]

computer_choice = random.choice(choices)

print(f"Your choice: {choices[user_choice]}")
print(f"Computer choice: {computer_choice}")
if choices[user_choice] == computer_choice:
    print("Draw!")
elif user_choice == 0 and computer_choice == "Paper":
    print("You lose!")
elif user_choice == 1 and computer_choice == "Scissors":
    print("You lose!")
elif user_choice == 2 and  computer_choice == "Rock":
    print("You lose!")
else:
    print("You Win!")

