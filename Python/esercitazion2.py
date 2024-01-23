def num_occorrenze(parola):

    d={}

    for lettera in parola:
        d[lettera] = d.get(lettera, 0) + 1

    return d

print (num_occorrenze('ciao'))
