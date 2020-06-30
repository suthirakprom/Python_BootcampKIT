import requests
import os

def poke_gallery():
    with open("pokemon.html", 'w') as poke_html:
        poke_html.writerow("<!DOCTYPE html>")
        poke_html.writerow('<html lang="en">')
        poke_html.writerow('<head>')
        poke_html.writerow('<meta charset="UTF-8">')
        poke_html.writerow('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
        poke_html.writerow('<title>Document</title>')
        poke_html.writerow('</head>')
        poke_html.writerow('<body>')

    
    poke_url_gallery = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
    r = requests.get(poke_url_gallery)
    poke_json = r.json()['pokemon']
    for i in poke_json:
        for j,k in i.items():
            if j == 'img':
                with open("pokemon.html", 'a') as poke_html:
                    poke_html.writerow(f"<img src={k} height='100px' width='100px'>")

        with open("pokemon.html", 'a') as poke_html:
            poke_html.writerow('</body>')
            poke_html.writerow('</html>')

poke_gallery()
