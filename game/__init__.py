import requests
import os

def randomApi():
    r = requests.get('https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new')
    number=r.text.replace('\n',"")
    return number

def welcomeMessage():
    print('Welcome to MasterMind!\n The rules are:'
    'The computer will choose four random numbers in astring.\n'
    'You will have 10 guesses to choose the right number sequence.\n'
    'For each try, you have 10 seconds to guess before time is up.')
    print('Ready? Press Y to begin')
    start=input()
    if start=="y" or start=="Y" or start=="yes":
        os.system("clear")
        playing()
    elif start=="n" or start=="N" or start=="no":
        print('Alright, Goodbye now')
        return
    else:
        raise ValueError('Invalid Entry')
        return

# def numOfGuesses():
#     guesses=[]
#     count=len(guesses)
#     return

# def isCorrect():
#     correct='Woot Woot you got it!'
#     incorrect='Sorry wrong guess. Try again.'
#     return

def playing():
    num = randomApi()
    guesses=[]
    count = 3
    print('Time to guess a four digit number.You have 10 attempts: ')
    while len(guesses)<3:
        print('Your guesses: '+ str(guesses))
        guess=input()
        guesses.append(int(guess))
        if guess == num:
            # isCorrect()
            print(num+ ' is the correct answer! You have won!')
            return
        else:
            os.system('clear')
            count-= 1
            print('You have '+ str(count) +" guess(es) left.")
    print(guesses)
    print("Sorry, you are out of guesses. Goodbye.")
    return

# #EXTRA
# def hints():
#     return

# def difficulty(choice):
#     if choice == easy:
#         return
#     elif choice == medium:
#         return
#     elif choice == hard:
#         return
#     else:
#         raise Error('Not an option.')
    

welcomeMessage()