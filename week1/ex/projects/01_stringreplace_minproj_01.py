choice = True
while choice:
    paragraph = input("Please input a paragraph:\n")
    searchStr = input("Please input a String search:\n")
    splitParagraph = paragraph.split()
    # count the number of searchStr that contained in the paragraph
    count = paragraph.count(searchStr)
    # the amount of words need to be replaced
    countReplacedWord = splitParagraph.count(searchStr)
    # print to the console
    print(f"There are {count} occurrences.")
    choice2 = True
    # second while loop
    while choice2:
        choose = input("Do you want to replace the text [Y/N]?\n")
        if choose == 'Y' or choose == 'N' or choose == 'y' or choose == 'n':     
            if choose == 'Y' or choose == 'y':
                replace = input("Please input replacement string:\n")
                # after_replace = paragraph.replace(searchStr, replace)
                # print(after_replace)
                print(f"{countReplacedWord} words has been replaced from the paragraph")
                splitParagraph = paragraph.split()
                for i in splitParagraph:
                    if i == searchStr:
                        i = replace
                    else: 
                        i = i
                    # print the paragraph with replaced words
                    print(i, end=' ')

                choice = False
            elif choose == 'N' or choose == 'n': 
                recheck = input("Oh! you don't like to replace, Do you want to check again?[Y/N]\n")
                # if yes
                if recheck == 'Y' or recheck == 'y':
                    choice = True
                # if no
                if recheck == 'N' or recheck == 'n':
                    choice = False
            # out of the second while loop
            choice2 = False
        else: 
            print("Please give a proper input")
            # get back the the second while loop
            choice2 = True
            


        