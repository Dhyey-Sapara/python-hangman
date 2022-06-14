import random
from words import words
import string

def get_valid_name(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_name(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    # Getting user input
    while len(word_letters ) > 0 and lives >0:
        # Letters used
        #  ' '.join(['a','b','cd']) => 'a b cd'
        print('You have ',lives,'left and Letters you have used is: ' + ' '.join(used_letters))

        # What current word is W-RD
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word is: ',' '.join(word_list))

        user_char = input('Guess the character: ').upper()
        if user_char in alphabet - used_letters:
            used_letters.add(user_char)
            if user_char in word_letters:
                word_letters.remove(user_char)
            else:
                lives -= 1
                print('Letter not in word')

        elif user_char in used_letters:
            print('Ypu have already guessed that alphabet')

        else:
            print('Invalid Character')
    #here the len(word_letters) == 0 or lives == 0
    if lives == 0:
        print('You died. The word was ',word)
    else:
        print('You have guessed the word',word)

hangman()