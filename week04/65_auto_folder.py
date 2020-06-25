import os

def auto_folder(list_folder):

    try:
        choice = ''
        
        #get a list of existing directory in our path 
        existing_dir = os.listdir()

        #check existing folder one by one
        for j in range(len(list_folder)):
            if os.path.isdir(list_folder[j]): 
                while choice != 'N' or choice != 'Y':
                    choice = input(f"Do you want to replace {list_folder[j]}? [Y/N]\n")
                    if choice != 'N' and choice != 'Y':
                        print("Invalid Option")
                    else:
                        break
                
                if choice == 'Y':
                    os.rmdir(list_folder[j])
                    os.mkdir(list_folder[j])
                    
                elif choice == 'N':                      
                    continue  
                    
            else: 
                os.mkdir(list_folder[j])
        return 1
    except:
        return 0   


auto_folder(["Folder1","Folder2"])
