"""
File: hangman.py
Name: Mike
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    guess = ''
    word = random_word()
    n = N_TURNS
    for i in range(len(word)):
        guess += '-'
    print("The word looks like: ", end="")
    print(guess)                    # This will show the length of the word.
    while True:
        if guess.isalpha():         # When all of the words are guessed right, it will go over the finishing process.
            print('You are correct!')
            print('You win!!')
            print('The word was:', str(word))
            break
        w = input_checker().upper()
        if word.find(w) != -1:      # If the word has the character of user's guess.
            for i in range(len(word)):
                if w == word[i]:    # Replace the position of the guess with the character that user guessed.
                    guess = guess[:i] + w + guess[i+1:]
            print('You are correct!')
            print('The word looks like', guess)
            print('You have', str(n), 'wrong guesses left.')
        else:             # If the user's input is not found in the guess will go over this process.
            n -= 1        # Minus 1 wrong guess chances.
            if n != 0:    # If user still have spare wrong guesses left.
                print('There is no', w+"'s", 'in the word.')
                print('You have', str(n), 'wrong guesses left.')
            else:         # If the user used up all the wrong guesses.
                print('There is no', w + "'s", 'in the word.')
                print('You are completely hung :(')
                print('The word was:', word)
                break


def input_checker():    # Determine if the input is a valid format or not.
    while True:
        input_ch = input('Your guess: ')
        if not input_ch.isalpha():
            print('Illegal format.')
        if len(input_ch) > 1:
            print('Illegal format.')
        if input_ch.isalpha():
            return input_ch


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
