# Problem Set 2, hangman.py
# Name: pavdemesh
# Collaborators: None
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
from typing import List

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading words list from file...")
    # inFile: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # words: list of strings
    words: list[str] = line.split()
    print("  ", len(words), "words loaded.")
    return words


def choose_word(wlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(sec_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in sec_word:
        if char not in letters_guessed:
            return False
    return True


def get_guessed_word(sec_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    res = ''
    for char in sec_word:
        if char in letters_guessed:
            res += char
        else:
            res += '_ '
    return res


# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_guessed_word(secret_word, letters_guessed))


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    res = ''
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            res += char
    return res


def unique_length(sec_word):
    unique_set = set()
    for char in sec_word:
        unique_set.add(char)
    return len(unique_set)


def hangman(sec_word):
    """
    sec_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    num_guesses = 6
    num_unique_char_sec_word = unique_length(sec_word)
    num_warnings = 3

    guessed = []

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(sec_word)} letters long")
    print(f"You have {num_warnings} warnings left.")
    print("-------------")

    while num_guesses > 0:

        print(f"You have {num_guesses} guesses left.")
        print(f"Available letters: {get_available_letters(guessed)}")

        guess = input("Please guess a letter:").lower()

        if guess not in string.ascii_lowercase:
            num_warnings -= 1
            tmp_word = get_guessed_word(sec_word, guessed)
            if num_warnings >= 0:
                print(f"Oops! That is not a valid letter. You have {num_warnings} warnings left: {tmp_word}")
                print("-------------")
                continue
            elif num_warnings < 0:
                print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {tmp_word}")
                num_guesses -= 1
                print("-------------")
                continue

        elif guess in guessed:
            num_warnings -= 1
            tmp_word = get_guessed_word(sec_word, guessed)

            if num_warnings >= 0:
                print(f"Oops! You've already guessed that letter. You have {num_warnings} warnings left: {tmp_word}")
                print("-------------")
                continue

            elif num_warnings < 0:
                print(f"""Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {tmp_word}""")
                num_guesses -= 1
                print("-------------")
                continue

        elif guess in sec_word:
            guessed.append(guess)
            print(f"Good guess: {get_guessed_word(sec_word, guessed)}")

        else:
            guessed.append(guess)
            print(f"Oops! That letter is not in my word: {get_guessed_word(sec_word, guessed)}")
            if guess in 'aeoiu':
                num_guesses -= 2
            else:
                num_guesses -= 1

        print("-------------")

        if is_word_guessed(sec_word, guessed):
            print("Congratulations, you won!")
            score = num_guesses * num_unique_char_sec_word
            print(f"Your total score for this game is: {score}")
            return 1

    print(f"Sorry, you ran out of guesses.The word was {sec_word}")
    return -1

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(sec_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    # secret_word = 'else'
    hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
