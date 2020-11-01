from passwordLib import *
print("1) Generate a password")
print("2) Edit generation settings")
print("3) Remove a password")
inp = int(input())
passw = newPass()
while True:
    if inp == 1:
        password = passw.generate()
        print("New password:", password)
        print("a for another or c to continue")
        while True:
            another = input()
            if another == "a":
                breakMain = False
                break
            if another == "c":
                print("k to keep the password or q to quit")
                while True:
                    keep = input()
                    if keep == "k":
                        print("dummy")
