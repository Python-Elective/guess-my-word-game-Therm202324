
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    #Pseodo code:
    # for every letter in secret_word()
    #   If not the same from the list, then show False
      
    # All letter guessed correctly, so return True
  
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
### Testcases
print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
print(is_word_guessed('pineapple', []))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    pass
    #Pseodo Code:
      # Initialize an empty string to store the result
      # Iterate over each letter in secret_word
      #    If the letter is in letters_guessed, append it to guessed_word
      #        If the letter is not guessed, append an underscore
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_"

    return guessed_word
#Testcases
print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...   
    pass
    # Pseodo Code:
        # Create a string containing all lowercase letters
        # Iterate over each letter in letters_guessed
        # Remove the guessed letter from all_letters
    all_letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in letters_guessed:
        all_letters = all_letters.replace(letter, '')
    return all_letters

#Testcases 
print( get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) )
  
def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many 
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    pass
# Pseodo Code:
    # Set the maximum number of guesses
    # Initialize guessed letters list
    # Print the initial message
    # Display the remaining number of guesses
    # Display the available letters
    # Ask the user for a guess
    # Check if the guess is a valid letter
    # Check if the letter has already been guessed
    # Add the guess to the list of guessed letters
     # Check if the guess is in the secret word
      # Check if the word is guessed
       # If the player runs out of guesses
       # Example usage
# Replace 'example' with the actual secret word you want the player to guess
    max_guesses = 8
    letters_guessed = []
    print("Welcome to the word_guessed Game!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("-------------")
    while max_guesses > 0:
        print("You have", max_guesses, "guesses left.")
        available_letters = get_available_letters(letters_guessed)
        print("Available letters:", available_letters)
        guess = input("Please guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in letters_guessed:
            print("Incorrect! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
            continue
        letters_guessed.append(guess)

       
        if guess in secret_word:
            print("Correct:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Incorrect! That letter is not part of the word:", get_guessed_word(secret_word, letters_guessed))
            max_guesses -= 1
        print("-------------")
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations! You Win!:", secret_word)
            break
    if max_guesses == 0:
        print("Sorry, you ran out of guesses. The word was:", secret_word)
game_loop('example')


def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()