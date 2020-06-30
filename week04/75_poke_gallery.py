import requests
import os

def poke_gallery():
    with open("pokemon.html", 'w') as poke_html:
        poke_html.write("<!DOCTYPE html>\n")
        poke_html.write('<html lang="en">\n')
        poke_html.write('<head>\n')
        poke_html.write('<meta charset="UTF-8">\n')
        poke_html.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        poke_html.write('<title>Document</title>\n')
        poke_html.write('</head>\n')
        poke_html.write('<body>\n')

    
    poke_url_gallery = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
    r = requests.get(poke_url_gallery)
    poke_json = r.json()['pokemon']
    for i in poke_json:
        for j,k in i.items():
            if j == 'img':
                with open("pokemon.html", 'a') as poke_html:
                    poke_html.write(f'<img src="{k}" height="100px" width="100px">\n')
                    # print(k)
    with open("pokemon.html", 'a') as poke_html:
        poke_html.write('</body>\n')
        poke_html.write('</html>\n')

poke_gallery()