import random
class newKey:
    def __init__(self):
        self.key = ''
        global alphabet,specials,getChars
        specials = ('!','"','£','$','€','%','^','&','*','(',')','[',']','@')
        alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

    def generate(self):
        keyLen = len(alphabet)+len(specials)
        merge = list(alphabet)
        for x in specials:
            merge.append(x)
        random.shuffle(merge)
        for x in merge:
            self.key = self.key + x

        return self.key

