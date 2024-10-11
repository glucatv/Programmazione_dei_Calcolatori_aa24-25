# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 06:26:12 2024

@author: gianluca
"""

a = input('Digita un numero: ')
x = float(a) # int(a)

# inizializzazione di g
g = x/2

while abs( g - x/g ) > 0.000001:
    g = ( g + x/g )/2

print( g )  # stampa dell'output


# In[]


x = 2 
g, c = x/2, 0 #  assegnamento multiplo

eps, c_max = 0.0000000000000001, 1000

while abs( g - x/g ) >  eps and c < c_max:
    c = c+1
    g = ( g + x/g )/2

print( g, c )  # stampa dell'output

# In[]

a = 'questa è una stringa'
print(a, type(a))

stringa_vuota = ''

print('lunghezza di a = ', len(a) )
print('lunghezza di stringa_vuota = ', len(stringa_vuota) )

# In[]

a = 'python'
c = 0

while a != input('scrivi python '):
    c = c +1

# altri operatori di confronto: <, <= ....
# vale per loro l'ordinamento lessicografico (estensione
# dell'ordinamento alfabetico)

# In[]

a = 'programmazione'
b = 'Python'

c = a + ' ' + b # concatenazione
print(c)

d = a*2 # ripetizione il numero deve essere int

print(d)

# In[]

i = 0

while i < len(a):
    print( a[i] )
    i += 1 # equivalente a i = i+1






