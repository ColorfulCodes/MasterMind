import requests

def randomApi():
    r = requests.get('https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new')
    return ''.join(r.text)

def welcomeMessage():
    return

def numOfGuesses():
    guesses=[]
    count=len(guesses)
    return

def isCorrect():
    correct='Woot Woot you got it!'
    incorrect='Sorry wrong guess. Try again.'
    return

def playing():
    return

#EXTRA
def hints():
    return

def difficulty(choice):
    if choice == easy:
        return
    elif choice == medium:
        return
    elif choice == hard:
        return
    else:
        raise Error('Not an option.')
    

print(randomApi())
print(len(randomApi()))