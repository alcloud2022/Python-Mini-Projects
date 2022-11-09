import random
#import words from words python file (list form)
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed 
    user_letter = input('Guess a letter: ').upper()
    lives = 7
    
    
    while len(word_letters) > 0 and lives > 0:
        #letters used are printed forming a list
        print('You haved used: ',' '.join(used_letters) )
        print('You have', lives, 'left')
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))
        
        user_letter = input('Guess a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1 #takes away a life for an incorrect guess
                print('Letter is not in word')    
                
        elif user_letter in used_letters:
            print("You have already used this letter")
            
        else:
            print("Invalid character please try again")
    
    if lives == 0:
        print('You did not guess the word correctly')  
        print('The word was',word,'!')  
    else:
        print('You guessed the word correctly')   
    
hangman()