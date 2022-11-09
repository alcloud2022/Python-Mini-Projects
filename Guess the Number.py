import random

#Guess number function
def guess(numb):
    random_number = random.randint(1, numb) #chooses a random number 
    guess = 0 #guess is set to 0 so it never ends up being the guessed number
    while guess != random_number:
        guess = int(input(f'Guess a number bewteen 1 and {numb}: '))
        print(guess)
        if guess < random_number:
            print("Sorry that number is too low")
            
        elif guess > random_number:
            print("Sorry that number is too high")
                
        
    print(f"That number is spot on, thember was indeed {random_number}")    
#guess(10)


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:    
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
            
    print(f'the computer guessed your number, {guess}, correctly!')        
    
computer_guess(5)