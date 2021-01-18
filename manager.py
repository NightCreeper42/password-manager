from passwordLib import *
print("1) Generate a password")
print("2) Edit generation settings")
print("3) Remove a password")
print("4) Retrieve a password")
inp = int(input())
passw = newPass()
breakMain = False
letsQuit = False
while True:
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
        
        while True:
            passname = input("Password to remove: ")
            print(namesList)
            if passname in namesList:
                print("dummy")

                    
#TODO delete the correct index from all of the csv files