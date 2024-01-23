# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:20:40 2023

@author: Lorenzo
"""

def conta_occorrenze(x, y):
    
    m= len(y)

    occ=0

    #i=0

   # while i<=n-m:
    j=0
    while j<m and y[j]==x[j]:
        j+=1
    if j==m:
        occ+=1
       # i+=1
    
    return occ

print(conta_occorrenze("massaggio", "mass"))
                                             

#DIMOSTRO COME IL PROGRAMMA POSSA FUNZIONARE ANCHE SENZA IL CONTATORE i