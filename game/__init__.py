from easy import easy
from medium import medium
from hard import hard
import os


def welcomeMessage():
    print('Welcome to MasterMind!\n The rules are:'
    'The computer will choose four random numbers in astring.\n'
    'You will have 10 guesses to choose the right number sequence.\n'
    'For each try, you have 10 seconds to guess before time is up.')
    start = input('Ready? Press Y to begin: ')
    if start=="y" or start=="Y" or start=="yes":
        given = input("Do you want to play easy, medium or hard level? ")
        os.system("clear")
        difficulty(given)
        
    elif start=="n" or start=="N" or start=="no":
        print('Alright, Goodbye now')
        return
    else:
        raise ValueError('Invalid Entry. Try again')
        return

def difficulty(choice):
    if choice == 'easy':
        value= easy()
        playing(value)

    if choice == 'medium':
        value= medium()
        playing(value)

    if choice == 'hard':
        value= hard()
        playing(value)
    

def playing(num):
    guesses=[]
    count = 10
    print('Time to guess a four digit number.You have 10 attempts: ')
    while len(guesses)<10:
        print('Your guesses: '+ str(guesses))
        guess=input()
        guesses.append(int(guess))
        if guess == num:
            print(num+ ' is the correct answer! You have won!')
            return
        else:
            os.system('clear')
            count-= 1
            print('You have '+ str(count) +" guess(es) left.")
    print(guesses)
    print("Sorry, you are out of guesses. Goodbye.")
    # Add mp3 here

    return



# #EXTRA
# def hints():
#     return

    

welcomeMessage()