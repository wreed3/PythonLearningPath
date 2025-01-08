import random
from hangman_words import hangman_words
from hangman_art import hangman_art
from hangman_logo import hangman_logo

def user_guess():
    return input("Please guess a letter: ")

restart = True
while restart:

    print(f'{hangman_logo}'              
          f'By: Will Reed')
    random.shuffle(hangman_words)

    random_word_selection = hangman_words[0]
    blanks = []
    print(f'{hangman_art[6]}\n')
    lives = 6

    # def build_blanks_array_and_placeholder(random_word):
    for i in random_word_selection:
        blanks.append("_")
    print('\n'+" ".join(blanks) + '\n')
    print(f'You have {lives} lives\n')

    game_over = False
    while not game_over:

        guess = user_guess().lower()

        while not guess.isalpha():
            guess = input("Please enter a letter?: ").lower()
        display = ""
        for index, letter in enumerate(random_word_selection):
            if letter == guess:
                blanks[index] = letter
        print('\n' + " ".join(blanks) + '\n')
        if guess not in random_word_selection:
            lives -= 1
            print(f'\nThe letter "{guess}" is not in the word.\n')
            print(f'You have {lives} lives left\n') if lives != 1 else print(f'You have {lives} life left\n')
        if "_" not in blanks:
            game_over = True
            print("You win!".upper())
        if lives == 0:
            game_over = True
            print("You lose!".upper())
            print(f'The word was {random_word_selection}')
        if game_over:
            replay = input(f"\nDo you want to play again? Y or N: ").lower()
            while 'y' != replay != 'n':
                replay = input(f"\nDo you want to play again? Y or N: ").lower()
            if replay == 'y':
                restart = True
            else:
                restart = False
        print(hangman_art[lives])
print("Game Over ")

