import translator as tr

t = tr.Translator()


def corntorlloInput(input):
    for carattere in input:
        if not ('a' <= carattere <= 'z'):
            print("Input non valido!")
            return False
    return True


def corntorlloInput2(input):
    for carattere in input:
        if carattere == '?':
            pass
        elif not ('a' <= carattere <= 'z'):
            print("Input non valido!")
            return False
    return True


primoAccesso = True


while(True):

    t.printMenu()

    if primoAccesso:
        t.loadDictionary("dictionary.txt")
        primoAccesso = False

    txtIn = input()

    # Add input control here!
    if txtIn.isdigit() == False:
        print("Comando errato! Inserire un numero")
        txtIn = 99
    elif int(txtIn) > 5 or int(txtIn) < 1:
        print("Comando errato! Inserire un numero compreso tra 1 o 5")
        pass

    if int(txtIn) == 1:
        print('Ok, quale parola devo aggiungere?')
        txtInStr = input()
        dati = txtInStr.split(' ')

        valido = True

        if len(dati) >= 2:
            for dato in dati:
                if corntorlloInput(dato):
                    valido = True
                else:
                    valido = False
                    break

            if valido:
                t.handleAdd(dati)
                print(dati)
        else:
            print("Inserire obbligatoriamente almeno due parole separate da uno spazio!")
        pass
    if int(txtIn) == 2:
        print('Ok, quale parola devo cercare?')
        txtInStr = input()
        if corntorlloInput(txtInStr):
            print(t.handleTranslate(txtInStr.lower()))
        pass
    if int(txtIn) == 3:
        print('Ok, quale parola devo cercare?')
        txtInStr = input()
        conta = 0
        for carattere in txtInStr:
            if carattere == '?':
                conta += 1
        if conta == 1:
            if corntorlloInput2(txtInStr):
                trovati = t.handleWildCard(txtInStr)
                if len(trovati[0]) == 1:
                    print(trovati[0])
                else:
                    for trovato in trovati:
                        print(f'{trovato[0]}:')
                        print(trovato[1:])
        else:
            print('La wildcard deve contenere obbligatoriamente solo un "?"')
        pass
    if int(txtIn) == 4:
        print(t.dizionario)
    if int(txtIn) == 5:
        break

