#medium
import requests

def randomApi():
    r = requests.get('https://www.random.org/integers/?num=5&min=0&max=7&col=1&base=10&format=plain&rnd=new')
    number=r.text.replace('\n',"")
    return number

def medium():
    random= randomApi()
    attempts = 5
    strLength ='five'
    t = 10
    return [random, t, strLength, attempts]

