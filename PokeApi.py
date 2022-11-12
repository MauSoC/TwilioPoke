import requests as rq
import random 

def pokemon():
    num = random.randint(0,800)
    url_api=f"https://pokeapi.co/api/v2/pokemon/{num}/"
    res = rq.get(url_api)
    data = res.json()
    return data['name'],data['sprites']['front_default']