from easy import easy
from medium import medium
from hard import hard
from threading import Timer
from time import sleep
import pyfiglet
import pygame
import time
import os


def welcomeMessage():
    # To hide pygame intro
    os.system('clear')
    result = pyfiglet.figlet_format("Master Mind!") 
    print(result)
    print(
    'Welcome to MasterMind!\n\n\nThe rules are: '
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
    

def playing(number):
    num = int(number[0])
    print(num)
    guesses=[]
    count = 1
    
    print('Time to guess a four digit number.You have 10 attempts: ')
    while len(guesses)<1:
        print('Your guesses: '+ str(guesses))
       
        guess=int(input('Guess number: '))
        guesses.append(guess)
        if guess == num:
            os.system('clear')
            print(pyfiglet.figlet_format("WINNER!"))
            print('\n')
            print(str(num)+ ' is the correct answer! You have won!')
            sound('soundEffects/yay.wav')
            return
        else:
            os.system('clear')
            count-= 1
            print('You have '+ str(count) +" guess(es) left.")
    print(guesses)
    # os.system('clear')
    print("Sorry, you are out of guesses. Goodbye.")
    sleep(1)
    # MP3

    # print(pyfiglet.figlet_format("LOSER!"))
    # sound('soundEffects/womp.wav')
    return

def sound(n):
    pygame.mixer.init()
    sound1 = pygame.mixer.Sound(n)
    
    sound1.play()
    pygame.time.wait(int(sound1.get_length() * 1000))
    return



# #EXTRA
# def hints():
#     return

    

welcomeMessage()