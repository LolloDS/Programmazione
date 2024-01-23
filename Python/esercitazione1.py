# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:24:12 2023

@author: Lorenzo
"""
# In[Esercizio 1]

x = input("Inserisci stringa 1\n")
y = input("Inserisci stringa 2\n")
a = ""

for c in x:
    if c in y:
        a += c

print("Le lettere in comune sono:\n" + a)


# In[Esercizio 3]

x = input("Inserisci stringa 1\n")
y = input("Inserisci stringa 2\n")
Flag = True

for c in x:
    if not c in y:
        Flag = False
        
for c in y:
    if not c in x:
        Flag = False
        
if(Flag):
    print("La seconda scritta è anagramma della prima")
else:
    print("La seconda scritta non è anagramma della prima")
    
# In[Esercizio 3 ALTERNATIVO]

x = input("Inserisci stringa 1\n")
y = input("Inserisci stringa 2\n")
Flag = True

if(len(x)==len(y)):
    for c in range(len(x)):
        if(x[c] not in y) or (y[c] not in x):
            Flag = False
else:
    Flag = False

if(Flag):
    print("La seconda scritta è anagramma della prima")
else:
    print("La seconda scritta non è anagramma della prima")
    
# In[Esercizio 3 ALTERNATIVO 2]

x = input("Inserisci stringa 1\n")
y = input("Inserisci stringa 2\n")
Flag = True

if(len(x)==len(y)):
    for c in x:
        if c not in y or c not in x:
            Flag = False
else:
    Flag = False

if(Flag):
    print("La seconda scritta è anagramma della prima")
else:
    print("La seconda scritta non è anagramma della prima")    