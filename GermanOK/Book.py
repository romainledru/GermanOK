import random
from Save import Save


class Word:
    def __init__(self):
        """Initialisation: download the actual version of data.json
        """

        d = Save("")
        self.dico = d.download()

    def getDico(self):
        return self.dico

    def pickWord(self):
        print("A Word is picked")
        key = random.choice(list(self.dico))
        return key ,self.dico[key]

    def compareWord(self,key,word):
        word = word.lower()
        counter = 0
        for letter in range(len(word)):
            if self.dico[key][0][letter] == word[letter]:
                counter += 1
        if counter >= len(self.dico[key][0])-2:
            return True
        else:
            return False

    def updateWord(self,word,point):
        word = word.lower()
        if point:
            self.dico[word][1] += 1
        else:
            self.dico[word][2] += 1
        d = Save(self.getDico())
        d.upload()
    
    def deleteWord(self,word):
        word = word.lower()
        try:
            self.dico.pop(word)
        except KeyError:
            print("Word does not exist on database")
            pass
        d = Save(self.getDico())
        d.upload()

    def newWord(self,de,fr):
        de = de.lower()
        fr = fr.lower()
        print("New Word learned: {} for {}".format(de,fr))
        try:
            if self.dico[de]:
                print("Word Already Exist")
                pass
        except KeyError:
            print("Creating New Word")
            self.dico[de] = [fr,0,0]
        d = Save(self.getDico())
        d.upload()
