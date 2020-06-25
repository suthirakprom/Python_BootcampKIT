import os

def current_folder():
    # path = '.'

    lst_folder = []
    temp = temp1 = []
    
    lst_file = []
    lst = os.listdir()

    for i in lst:
        if i == ".git":
            continue
        if os.path.isdir(i):
            lst_folder.append(i)
        if not os.path.isdir(i):
            lst_file.append(i)


    #folder len
    len_folder = len(lst_folder)
    #file len 
    len_file = len(lst_file)

    for i in range(len_folder):
        temp.append('Folder')

    for i in range(len_file):
        temp1.append('File')


    zip_folder = list(zip(lst_folder, temp))


    zip_file = list(zip(lst_file,temp1))


    for i in lst_file:
        lst_folder.append(i)
    
    for i in zip_folder:
        lst_folder.append(i)
    
    for i in zip_file:
        zip_folder.append(i)

    print(zip_folder)
    
current_folder()