def controllaParole(parola, wildcard):
    if len(parola) != len(wildcard):
        return False
    for i in range(len(wildcard)):
        if wildcard[i] == '?':
            pass
        elif parola[i] != wildcard[i]:
            return False
    return True

class Dictionary:
    def __init__(self):
        self.dizionario = {}

    def addWord(self, parolaAliena, parolaItaliana):
        try:
            self.dizionario[parolaAliena].append(parolaItaliana)
        except KeyError:
            self.dizionario[parolaAliena] = [parolaItaliana]

    def translate(self, parolaAliena):
        try:
            return self.dizionario[parolaAliena]
        except KeyError:
            return ["Parola non Trovata"]
    def translateWordWildCard(self, wildcard):
        traduzioni = []
        for daTradurre in self.dizionario.keys():
            if controllaParole(daTradurre,wildcard):
                traduzioniParola = []
                traduzioniParola.append(daTradurre)
                [traduzioniParola.append(i) for i in self.dizionario[daTradurre]]
                traduzioni.append(traduzioniParola)
        if len(traduzioni) == 0:
            return [["Parola non Trovata"]]
        else:
            return traduzioni

    def __repr__(self):
        elenco = ''
        for chiave in self.dizionario:
            if elenco != '':
                elenco += '\n'
            elenco += chiave
            for valore in self.dizionario[chiave]:
                elenco += " " + valore

        return elenco

