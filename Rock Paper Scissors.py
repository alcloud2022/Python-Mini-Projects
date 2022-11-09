#import random for computer selection
import random

#This function will allow the player to choose an option
#The computer will be assigned and option at random
def play():
    user = input("What is your choice? 'r' for rock 'p' for paper 's' for scissors\n") #asks user to select rock, paper or scissors
    computer = random.choice(['r', 'p', 's']) #computer will be assigned rock, paper or scissors at random
    """If statements check to see whether user has won 
    based on whether the is_win function is True"""
    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'You Won'
    return 'You lost'
"""Function checks all possibilities whereby the user would win and returns
   True if any of the conditions are met"""   
def is_win(player, cpu):
    if (player == 'r' and cpu == 'p') or (player == 's' and cpu == 'p') \
    or (player == 'p' and cpu == 'r'):
        return True
    
print(play())
            