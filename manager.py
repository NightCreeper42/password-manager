from passwordLib import *
passw = newPass()
breakMain = False
letsQuit = False
while True:
    print("1) Generate a password")
    print("2) Edit generation settings")
    print("3) Remove a password")
    print("4) Retrieve a password")
    print("5) Quit")
    print("6) Clean all the files")
    inp = int(input())
    if inp == 1:
        while True:
            password = passw.generate()
            print(password)
            print("k to keep, a for another or q to quit")
            while True:
                inp = input()
                if inp == 'k':
                    breakMain = True
                    break
                if inp == 'a':
                    break
                if inp == 'q':
                    letsQuit = True
                    breakMain = True
                    break

            if breakMain == True:
                break

        if letsQuit == True:
            break

        passwEnc = passw.btecEncrypt(password)
        passname = input("Password label: ")
        passw.addToFile("passwords.csv",passwEnc)
        passw.addToFile("keys.csv",passw.key)
        passw.addToFile("passnames.csv",passname)
        print("Your password has been added to the file.")
    
    elif inp == 2:
        passw.settingsChange()
    
    elif inp == 3:
        names = open("passnames.csv","r")
        namesList = names.read()
        namesList = namesList.split('\n')
        names.close()
        print("available passwords:")
        print(*namesList)
        
        while True:
            passname = input("Password to remove: ")
            print(namesList)
            if passname in namesList:
                if passname == '':
                    print("Invalid password")
                    pass
                else:
                    index = namesList.index(passname)
                    files = ("passnames","passwords","keys")
                    for name in files:
                        file = open(name+".csv","r")
                        List = file.read()
                        List = List.split('\n')
                        List.pop(index)
                        rewrite = open(name+".csv","w")
                        for item in List:
                            rewrite.write(item+'\n')
                        file.close()
                        rewrite.close()
                    print("password removed")
                    break
            else:
                print("Invalid password")

    elif inp == 4:
        print("available passnames:")
        file = open("passnames.csv","r")
        passNames = file.read()
        file.close()
        passNames = passNames.split('\n')
        print(*passNames)

        passName = input("Passname: ")
        index = passNames.index(passName)
        file = open("passwords.csv","r")
        List = file.read().split('\n')
        password = List[index]
        file.close()

        key = input("Key: ")
        printPass = passw.btecDecrypt(password,key)
        print("password:",printPass)
        input("Press ENTER to continue")

    elif inp == 5:
        break

    elif inp == 6:
        passw.fileClean("passwords.csv")
        passw.fileClean("passnames.csv")
        passw.fileClean("keys.csv")
        print("Files successfully cleaned")
    
    print()