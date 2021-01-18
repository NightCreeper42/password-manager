import random,btecKey
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
        self.alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
        self.password = ''
        settingsFile.close()

        global myKey
        myKey = btecKey.newKey()

        global alphaSpec
        alphaSpec = []
        for char in self.alphabet:
            alphaSpec.append(char)
        for char in self.specials:
            alphaSpec.append(char)
        for char in range(10):
            alphaSpec.append(str(char))
        
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
                char = random.choice(self.alphabet)
                
            password = password + char
        
        return password
    
    def settingsChange(self):
        """change how the password is generated"""
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
        
    def btecEncrypt(self,password):
        self.key = myKey.generate()
        print("Your password's key:\n",self.key+"\nKeep it safe!")

        self.encrypted = ""
        for char in password:
            self.encrypted = self.encrypted + alphaSpec[list(self.key).index(char)]
        return self.encrypted

    def btecDecrypt(self,password,key):
        self.decrypted = ""
        for char in password:
            self.decrypted = self.decrypted + list(key)[alphaSpec.index(char)]
        return self.decrypted

    def addToFile(self,filename,password):
        file = open(filename,"a")
        file.write(password+'\n')
        file.close()

    def getFromFile(self,filename,passname):
        file = open(filename,"r")
        #fileRows = []
        for row in file.read():
            row = row.split(',')
            if row[0] == passname:
                break
        return row[1]

    def removeFromFile(self,filename,passname):
        file = open(filename,"r+")
        fileRows = []
        print(fileRows)
        
