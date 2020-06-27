import datetime

def append_file(filename):
    user_input = ""
   
    while user_input != 'EXIT':
        user_input = input("$: ")
        f = open(filename, "a")
        if user_input == "EXIT":
            break
        time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        f.write(f"[{time}] {user_input} ")
        print(time)
        

    f.close

append_file("filename")