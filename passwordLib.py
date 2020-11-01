import random
class newPass:
    def __init__(self):
        self.SETTINGS = {}
        global settingsList
        settingsList = ("passLenMin","passLenMax","charChangeChance","specialMax","numMax")
        settingsFile = open("genSETTINGS.txt","r")

        index = 0
        fileLines = settingsFile.read().split('\n')
        for line in fileLines:
            line = line.split(':')
            self.SETTINGS[settingsList[index]] = int(line[1])
            index += 1

        self.specials = ['!','"','£','$','€','%','^','&','*','(',')','[',']','@']
        self.alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        self.password = ''
        settingsFile.close()

        """remove a character from the special characters list"""
        del self.specials[self.specials.index(char)]
    
    def generate(self):
        """generate your new fancy password"""
        password = ""
        strLen = random.randint(self.SETTINGS["passLenMin"],self.SETTINGS["passLenMax"])
        for x in range(strLen):
            charChange = random.randint(0,self.SETTINGS["charChangeChance"])
            if charChange >= 0 and charChange <= self.SETTINGS["specialMax"]:
                char = random.choice(self.specials)
            if charChange >= self.SETTINGS["specialMax"]+1 and charChange <= self.SETTINGS["numMax"]:
                char = str(random.randint(0,9))
            if charChange >= self.SETTINGS["numMax"]+1 and charChange <= self.SETTINGS["charChangeChance"]:
                upChance = random.randint(0,1)
                char = random.choice(self.alphabet)
                if upChance == 1:
                    char = char.upper()
                
            password = password + char
        
        return password
    
    def settingsChange(self):
        while True:
            print()
            print("1) Change the minimum length")
            print("2) Change the maximum length")
            print("3) Change the maximum chance range of each character")
            print("4) Change the minimum chance of getting a special character")
            print("5) Change the maximum chance of getting a number")
            inp = int(input())-1
            setting = settingsList[inp]

            print("Current state:", self.SETTINGS[setting])
            changeTo = int(input("Change to: "))
            self.SETTINGS[setting] = changeTo
            print("Setting has been changed")

            settingsFile = open("genSETTINGS.txt","w")
            index = 0
            for line in self.SETTINGS:
                appStr = settingsList[index] + ":" + str(self.SETTINGS[line])
                if index != len(self.SETTINGS)-1:
                    appStr = appStr + "\n"

                settingsFile.write(appStr)
                index += 1
            settingsFile.close()
            print("put c to continue or q to quit")
            while True:
                inp = input()
                if inp == "c":
                    breakMain = False
                    break
                elif inp == "q":
                    breakMain = True
                    break
            
            if breakMain == True:
                break

class btecEncryption:
    def __init__(self,password):
        alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
