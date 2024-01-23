#scrivere un programma in c che prenda in input due stringhe e stampi il numero di anagrammi possibili


def anagrammi(s1,s2):
    if len(s1) != len(s2):
        return 0
    else:
        for i in range(len(s1)):
            if s1[i] not in s2:
                return 0
        return 1
    
s1=input("inserisci la prima stringa: ")
s2=input("inserisci la seconda stringa: ")

if anagrammi(s1,s2):
    print("sono anagrammi")
else:
    print("non sono anagrammi")

#scrivere un programma in c che prenda in input una stringa e stampi il numero di anagrammi possibili