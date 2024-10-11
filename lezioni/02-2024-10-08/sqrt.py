# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 06:26:12 2024

@author: gianluca
"""

x = 20 # variabile che contiene l'input
g = 5

while abs( g*g - x ) > 0.00001 :
    g = ( g + x/g )/2

print( g )  # stampa dell'output


# In[Seconda versione]

# inizializzazione di x e g
x = 20 # variabile che contiene l'input
g = 150

print( type(g) )

while abs( g - x/g ) > 0.00001: # seconda versione del test
    print(g)
    g = ( g + x/g )/2
    print( type(g) )

print( g )  # stampa dell'output

# In[input]

a = input('Digita un numero: ')
a = float(a) # int(a)
print(a, type(a))




