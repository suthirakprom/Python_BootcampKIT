def milli_to_hours(second):
    hour = second // 3600000
    return hour

res = milli_to_hours(10800000)
print(res)