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
            if nuovaTraduzione in traduzioni:
                 print(f'{nuovaTraduzione} Già presente')
            else:
                self.dizionario.addWord(entry[0], nuovaTraduzione)
                risultato.append(nuovaTraduzione)
                print(f"{nuovaTraduzione} Aggiunta")
        return risultato

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        traduzioni = []
        for parolaDaTradurre in self.dizionario.dizionario.keys():
            if query == parolaDaTradurre:
                [traduzioni.append(i) for i in self.dizionario.translate(parolaDaTradurre)]
        if len(traduzioni) == 0:
            return ['Parola non Trovata']
        return traduzioni

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        return self.dizionario.translateWordWildCard(query)


def test():
    t = Translator()
    t.printMenu()
    print(t.loadDictionary('dictionary.txt'))
    print(t.dizionario.translate("taivas"))
    t.dizionario.addWord("taivas", "mare")
    print(t.handleAdd(["taivas", "cielo", "nuvola", "carro"]))
    print(t.handleTranslate("taivas"))
    t.handleAdd(["tailas", "carne", "pane", "pesce"])
    print(t.handleWildCard("tai?as"))
    print(t.dizionario.translate('siahbn'))
    print(t.handleTranslate('bhbh'))

if __name__ == "__main__":
    test()