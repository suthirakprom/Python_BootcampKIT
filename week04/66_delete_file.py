import os

def delete_file(filename):
    choice = ''
    while choice != 'N' and choice != 'Y':
        choice = input(f"Are you sure you want to delete {filename}? [Y/N]\n")
        if choice == 'Y':
            # if user enter a folder it will go straight into expect
            try:
                try:
                    # remove file
                    os.remove(filename)
                except:
                    # remove folder
                    os.rmdir(filename)
                return 1
            except:
                print("That file or folder does not exist.")
        elif choice == 'N':
            return 0
        else:
            print("Invalid Option")


delete_file("Folder 2")