import random
class newKey:
    def __init__(self):
        self.key = ''
        global alphabet,specials,getChars
        specials = ('!','"','£','$','€','%','^','&','*','(',')','[',']','@')
        alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        numbers = ('1','2','3','4','5','6','7','8','9','0')

    def generate(self):
        keyLen = len(alphabet)+len(specials)
        self.merge = list(alphabet)
        for x in specials:
            self.merge.append(x)
        random.shuffle(self.merge)
        for x in self.merge:
            self.key = self.key + x

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
