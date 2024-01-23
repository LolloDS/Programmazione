#Date due parole scrivere una funzione che mi dice se le due parole sono anagrammi

def anagrami(parola1, parola2):

    d1 = {}
    d2 = {}

    for lettera in parola1:
        d1[lettera] = d1.get(lettera, 0) + 1

    for lettera in parola2:
        d2[lettera] = d2.get(lettera, 0) + 1
        
    return d1 == d2

print (anagrami('ciao', 'oiac'))
print (anagrami('ciao', 'oiaca'))