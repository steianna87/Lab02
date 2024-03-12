class Dictionary:
    def __init__(self):
        self.dizionario = {}

    def addWord(self, parolaAliena, parolaItaliana):
        self.dizionario[parolaAliena] = parolaItaliana

    def translate(self, parolaAliena):
        return self.dizionario[parolaAliena]

    def translateWordWildCard(self):
        pass

    def __repr__(self):
        elenco = ''
        for chiave in self.dizionario:
            if elenco != '':
                elenco += '\n'
            elenco += chiave + " " + self.translate(chiave)

        return elenco

