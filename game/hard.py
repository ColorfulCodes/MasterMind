# 5 second timer
# 7 digit number
import requests

def randomApi():
    r = requests.get('https://www.random.org/integers/?num=7&min=0&max=7&col=1&base=10&format=plain&rnd=new')
    number=r.text.replace('\n',"")
    return number

def hard():
    random= randomApi()
    return random