import requests

def get_fbid(url):
    find_fbid = "https://findmyfbid.com/"
    URL = {'url': url}
    try: 
        r = requests.post(url = find_fbid, params = URL)
        return r.json().get("id")
    except Exception:
        return 0