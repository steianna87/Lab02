import dataclasses

from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.dizionario = Dictionary()

    def printMenu(self):
        print("------------------------------")
        print("  Translator Alien-Italian")
        print("------------------------------")
        # 1. Aggiungi nuova parola
        print("1. Aggiungi nuova parola")
        # 2. Cerca una traduzione
        print("2. Cerca una traduzione")
        # 3. Cerca con wildcard
        print("3. Cerca con wildcard")
        # 4. Exit
        print("4. Stampa tutto il Dizionario")
        print("5. Exit")
        print("------------------------------")
        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict,'r', encoding='utf-8') as file:
            for righe in file:
                dati = righe.rstrip().split(' ')
                self.dizionario.addWord(dati[0], dati[1])

        return self.dizionario

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        traduzioni = self.handleTranslate(entry[0])
        nuoveTraduzioni = entry[1:]
        risultato = [entry[0]]
        for nuovaTraduzione in nuoveTraduzioni:
            for traduzione in traduzioni:
                if traduzione == nuovaTraduzione:
                    print(f'{nuovaTraduzione} già presente')
                else:
                    self.dizionario.addWord(entry[0], nuovaTraduzione)
                    risultato.append(nuovaTraduzione)
                    print(f"{nuovaTraduzione} aggiunta")
        return risultato

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        traduzioni = []
        for valore in self.dizionario.dizionario.values():
            if query == valore:
                traduzioni.append(valore)
        return traduzioni

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass

def test():
    t = Translator()
    t.printMenu()
    print(t.loadDictionary('dictionary.txt'))
    print(t.dizionario.translate("taivas"))

if __name__ == "__main__":
    test()