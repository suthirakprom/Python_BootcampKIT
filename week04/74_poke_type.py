import requests
import json

def poke_type(pokemon):  
    arr = []
    poke_url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
    r = requests.get(poke_url)
    poke_json = r.json()['pokemon']
    for i in poke_json: 
        for j,k in i.items():
            if j == 'type':
                if k == pokemon:
                    arr.append((i['id'], i['name']))
    print(arr)
poke_type(['Water'])