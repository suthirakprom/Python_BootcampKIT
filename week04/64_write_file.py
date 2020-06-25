import os

def write_file(filename, content):
    choice = ''
    lst = os.listdir()
    print(lst)

    #run when the file is duplicate
    for i in lst:
        if i == filename:
            while choice != 'N' or choice != 'Y':
                choice = input(f"Are you sure you want to replace {filename}? [Y/N]\n")
                if choice != 'N' and choice != 'Y':
                    print("Invalid Option")
                else:
                    break
            if choice == 'Y':
                f = open(filename, "w")
                f.write(content)
                f.close()
                return 1

            elif choice == 'N':
                return 0
    
    #check if the file is duplicate
    #if it is this code will not run
    if choice != 'N' and choice != 'Y': 
        for i in lst:
            if i != filename:
                f = open(filename, "w")
                f.write(content)            
                f.close() 
                return 1  


write_file("filename1", "ABC")