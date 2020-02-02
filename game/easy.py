#Easy Mode
import requests

def randomApi():
    r = requests.get('https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new')
    number=r.text.replace('\n',"")
    return number

def easy():
    random= randomApi()
    attempts = 10
    strLength ='four'
    t = 0
    return [random, t, strLength, attempts]