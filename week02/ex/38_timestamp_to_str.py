from datetime import datetime

def timestamp_to_str(timestamp):
    try:
        n = int(timestamp)
        x = datetime.fromtimestamp(n)
        print(x)
    except:
        print("Your timestamp is not valid.")

timestamp_to_str(1623646780)
timestamp_to_str("1623646780")
timestamp_to_str("abc")
