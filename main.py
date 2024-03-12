import translator as tr

t = tr.Translator()

def corntorlloInput(input):
    for carattere in input:
        valido = False
        if carattere>='a' and carattere<='z':
            valido = True
    if valido == False:
        print("Parola non valida!")
    return valido

while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

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
        if len(dati) == 2:
            if corntorlloInput(dati[0]) and corntorlloInput(dati[1]):
                t.dizionario.addWord(dati[0].lower(), dati[1].lower())
                print("Parola Aggiunta")
        elif len(dati) > 2:



            print("Parola Aggiunta")
        else:
            print("Inserire obbligatoriamente almeno due parole separate da uno spazio!")
        pass
    if int(txtIn) == 2:
        print('Ok, quale parola devo cercare?')
        txtInStr = input()
        if corntorlloInput(txtInStr):
            print(f"{txtInStr.lower()} significa {t.dizionario.translate(txtInStr.lower())}")
        pass
    if int(txtIn) == 3:
        pass
    if int(txtIn) == 4:
        print(t.dizionario)
    if int(txtIn) == 5:
        break

