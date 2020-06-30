import requests
import json

def get_fbid(url_face):
    lst = []
    find_fbid = "https://findmyfbid.com/"
    URL = {'url': url_face}
    get_status_code = requests.get(url_face).status_code

    r = requests.post(url = find_fbid, params = URL)
    res = r.json()
    print(res)
    # if res == []:
    #     return get_status_code
    # else:
    lst.append(get_status_code)
    print(lst)

get_fbid("https://www.facebook.com/JohnDoe")
