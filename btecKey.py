import random
class newKey:
    def __init__(self):
        self.key = ''
        global alphabet,specials
        specials = ('!','"','£','$','€','%','^','&','*','(',')','[',']','@')
        alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

    def generate(self):
        #keyLen = len(alphabet)+len(specials)
        self.merge = list(alphabet)
        for x in specials:
            self.merge.append(x)
        for x in range(10):
            self.merge.append(str(x))
        random.shuffle(self.merge)
        for x in self.merge:
            self.key = self.key + str(x)

        return self.key

    def getKeyList(self):
        """returns list for letters then specials"""
        replaceAlpha = []
        replaceSpecial = []
        self.key = list(self.key)

        for x in range(len(alphabet)):
            replaceAlpha.append(self.key[x-1])
        for x in range(len(specials)):
            replaceSpecial.append(self.key[x-1])

        return replaceAlpha, replaceSpecial
