import requests

def get_html(url):
    get_html = requests.get(url)
    convert_to_text = get_html.text
    print(convert_to_text)

get_html("https://www.google.com/")