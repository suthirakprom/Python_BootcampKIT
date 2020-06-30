import os
import datetime

class FileLib: 
    def inspect(self):
        pass
    def current_path(self):
        return os.path.dirname(os.path.abspath(__file__))
    def read(self, filename): 
        try:
            f = open(filename, "r")
            print(f.read())
            f.close()
        except:
            print("Invalid FILENAME")
    def write(self, filename, content):
        choice = ''
        lst = os.listdir()
        print(lst)
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
    
        if choice != 'N' and choice != 'Y': 
            for i in lst:
                if i != filename:
                    f = open(filename, "w")
                    f.write(content)            
                    f.close() 
                    return 1  

    def append(self,filename, content):
        f = open(filename, "a")
        f.write(content)         
        f.close

    def remove(self, filename): 
        choice = ''
        while choice != 'N' and choice != 'Y':
            choice = input(f"Are you sure you want to delete {filename}? [Y/N]\n")
            if choice == 'Y':
                try:
                    try:
                        os.remove(filename)
                    except:
                        os.rmdir(filename)
                    return 1
                except:
                    print("That file or folder does not exist.")
            elif choice == 'N':
                return 0
            else:
                print("Invalid Option")

    def create_folder(self, folder_list):
        try:
            choice = ''
            existing_dir = os.listdir()
            for j in range(len(folder_list)):
                if os.path.isdir(folder_list[j]): 
                    while choice != 'N' or choice != 'Y':
                        choice = input(f"Do you want to replace {folder_list[j]}? [Y/N]\n")
                        if choice != 'N' and choice != 'Y':
                            print("Invalid Option")
                        else:
                            break                   
                    if choice == 'Y':
                        os.rmdir(folder_list[j])
                        os.mkdir(folder_list[j])
                    elif choice == 'N':                      
                        continue                         
                else: 
                    os.mkdir(folder_list[j])
            return 1
        except:
            return 0   