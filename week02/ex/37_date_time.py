import datetime

def date_time():
    value = datetime.datetime.now()
    n = value.replace(microsecond=0)
    return n

res = date_time()
print(res)