def read_file(file_name):
    try:
        f = open(file_name, "r")
        print(f.read())
        f.close()
    except:
        print("Invalid FILENAME")

read_file("hello.txt")
