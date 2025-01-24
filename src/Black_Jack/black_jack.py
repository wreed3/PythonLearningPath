import random


from black_jack_logo import black_jack_logo

cards = [11,2,3,4,5,6,7,8,10,10,10,10]

# User and computer pull a card one at a time. User goes first.
# If User pulls go higher than 21 before the computer pulls do, the computer wins and vice versa.
# You ask for a card or pass
# The game tells you what your pulls are everytime you pull and what the computer pulls are( in a list)
#At the end the system tells you who won and asks you if you want to play again

play_again = True
your_cards = []
computer_cards = []
game_over = False


def add_up_cards(card_array):
    sum_of_cards = 0
    for card_Num in card_array:
        sum_of_cards += card_Num
    return sum_of_cards

def random_choice(card_array):
    card_choice = random.choice(card_array)
    return card_choice

def pull_a_card(selection, card_array, game_end):
    while ('y' == choice == 'n') & game_end == False:
        if selection == 'y':
            user_pull = random_choice(card_array)
            your_cards.append(user_pull)
            user_score = add_up_cards(your_cards)
            print(f"Your cards are: {your_cards}, Your current score: {user_score}\n")
            if int(user_score) > 21:
                print(f"You went over. You Lose!")
                print(f"Computer Wins!")
                game_end = True
                break

            elif int(user_score) == 21:
                print(f"You Win!")
                game_end = True
                break

            system_pull = random.choice(cards)
            computer_cards.append(system_pull)
            system_score = add_up_cards(computer_cards)
            print(f"Computer's cards are: {computer_cards}, Computer's current score: {system_score}\n")

            if int(system_score) > 21:
                print(f"Computer went over!")
                print(f"You Win!")
                game_end = True
                break

            elif int(system_score) == 21:
                print(f"Computer Wins!")
                game_end = True
                break
        else:
            system_pull = random.choice(cards)
            computer_cards.append(system_pull)
            system_score = add_up_cards(computer_cards)
            print(f"Computer's cards are: {computer_cards}, Computer's current score: {system_score}\n")
            if int(user_score) > 21:
                print(f"You went over. You Lose!")
                print(f"Computer Wins!")
                game_end = True
                break
            elif int(system_score) > 21:
                print(f"Computer went over!")
                print(f"You Win!")
                game_end = True
                break
            elif int(user_score) == 21:
                print(f"You Win!")
                game_end = True
                break
            elif int(system_score) == 21:
                print(f"Computer Wins!")
                game_end = True
                break

        selection = input(f"type 'y' to get another card, type 'n' to pass:  ")





while play_again:
    print(black_jack_logo)
    your_score = 0
    computer_score = 0
    your_cards = []
    computer_cards = []
    pull_card = input(f"\nPull a card? 'y' or 'n':  ")
    while 'y' != pull_card != 'n':
        pull_card = input(f"Pull a card? 'y' or 'n':  ")
    if pull_card == 'y':
        your_pull = random_choice(cards)
        your_cards.append(your_pull)
        your_score = add_up_cards(your_cards)
        print(f"Your first card is: {your_cards}, Your current score: {your_score}\n")

        computer_pull = random.choice(cards)
        computer_cards.append(computer_pull)
        computer_score = add_up_cards(computer_cards)
        print(f"Computer's first card is: {computer_cards}, Computer's current score: {computer_score}\n")
    else:
        play_again = False
        break

    choice = input(f"type 'y' to get another card, type 'n' to pass:  ")

    while 'y' != choice != 'n':
        choice = input(f"type 'y' to get another card, type 'n' to pass:  ")


    pull_a_card(choice,cards,game_over)

    # computer_pull = random.choice(cards)
    # computer_cards.append(computer_pull)
    # computer_score = add_up_cards(computer_cards)
    # print(f"Computer's first card is: {computer_cards}, Computer's current score: {computer_score}\n")






    # #reponse
    # print(f'Your cards: [5,10], current score: 15 ')
    # #response
    # print(f"Computer's first card: 10")
    #
    # #input
    # print(f"type 'y' to get another card, type 'n' to pass:  ")
    #
    # #reponse
    # print(f'Your cards: [5,10,10], current score: 25 ')
    # print(f"Your final hand: [5,10,10], final score: 25 ")
    # print(f"Computer's final hand: [10,10], final score: 20 ")
    # print(f"You have the high score without going over. You Win!")
    # print(f"You went over. You Lose!")
    # print(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")

