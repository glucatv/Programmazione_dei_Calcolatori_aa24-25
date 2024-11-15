# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:24:45 2024

@author: gluca
"""


# In[]

def disegna_punti_su_retta(a):
    def t1(e):
        return e[1]
    
    n = len(a)
        
    b = sorted(a, key=t1)  # Tempo O(n log_2 n), spazio O(n)
    
    lx, rx = b[0][1], b[-1][1]
    
    # m = rx-lx+1   dimensione dell'output
    
    i = 0 # indice in b del prossimo punto da stampare
    for p in range(lx, rx+1):
        if i < n and p == b[i][1]:
            print(b[i][0], end='')
            i += 1
        else:
            print('*', end='')   # O(m)
 
    
     # Complessità: tempo O(n log_2 n + m) nel caso peggiore,
     #        spazio O(n)
     
# In[] 

a = [ ('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5) ]

disegna_punti_su_retta(a)

# In[Intersezione]

a = [9, 2, 1, 8, 4] # insieme
b = [1, 7, 0, 8, 2] # insieme

# assumiamo len(a) == len(b) di valore n

# un algoritmo che trovi a intersezione b
# ovvero c = [1, 2, 8]

# alg 1

c = []

for e in a:
    if e in b: # O(n) nel caso peggiore e nel caso medio (verdere dopo)
        c.append(e)
        
print(c)


# complessità temporale O(n**2) nel caso peggiore  e medio
# complessità spaziale O(1)

# costo ricerca su lista b nel caso medio
#
# e è b[0]    1 confronto
# e è b[1]    2 confronti
# e è b[2]    3 confronti
# ...
# e è b[n-1]  n controni
# e non è in b n+1 confronti

# costo medio (1+2+3+...+(n-1)+n+(n+1))/(n+1) = ((n+2)n)/(2(n+1)) = n/2 circa

# In[]

# assumiamo len(a) == len(b) di valore n

# alg 2

a.sort()
b.sort()

i, j = 0, 0
c = []

while i < len(a) and j < len(b):
    if a[i] == b[j]:
        c.append(a[i])
        i+=1
        j+=1
    elif a[i] < b[j]:
        i+=1
    else:
        j+=1
print(c)


# complessità temporale O(n log_2 n + n)
# complessità spaziale O(n) per via del metodi sort()

# In[Dizionari]

# mapping tra chiavi e valori (k, v)

# d contiene (k0, v0), (k1, v1),....

# proprietà: le chiavi sono univoche ki != kj se i!=j

# operazioni: dato un dizionario
#
# ricerca: k è una chiave del dizionario?
#
# lettura: data una chiave k voglio conoscere il valore associato a k
#
# aggiornamento: k, v 
#
#   se k è una chiave ne viene aggiornato il valore a v
#   altrimenti (k,v) viene aggiunta al dizionario
#
# cancellazione: k
#
#   se k è una chiave, elimina la coppia (k, v)
#   altrimenti ERRORE

d = {}   # dizionario vuoto

d = {5:'cinque', 'uno':1.0, 'due':(1,2)}

print(d, len(d))

print(5 in d)
print('5' in d)

print( d['uno'] )
# print( d[1] )  IndexError perché 1 not in d

d['uno'] = 'UNO'  # aggiornato il valore associato a 'uno'

print(d)

d[10] = '2x5'  # nuova coppia chiave-valore

print(d)

del(d['uno'])

print(d)

# del(d['12'])  IndexError perché '12' not in d

print(d)

# creazione del dizionario vuor, ricerca, aggiornamento, lettura e
# cancellazione hanno costo temporale che spaziale O(1) in media

# In[]

a = [9, 2, 1, 8, 4] # insieme
b = [1, 7, 0, 8, 2] # insieme

# assumiamo len(a) == len(b) di valore n

da, db = {}, {}

for e in a: # O(n) tempo, O(n) spazio
    da[e] = None  # non mi interessa il valore
    
for e in b: # O(n) tempo, O(n) spazio
    db[e] = None  # O(1) tempo nel coso medio

c = []

for e in da:  # itera sulle chiavi del dizionario
    if e in db:  # O(1) tempo nel caso medio
        c.append(e)
        
print(c)

# complessità:
# - temporale: O(n) nel caso medio
# - spaziale: O(n) sempre

# In[]

def disegna_punti_su_retta(a):
    def t1(e):
        return e[1]
    
    # n = len(a)
    
    lx = min(a, key=t1)[1]
    rx = max(a, key=t1)[1]
    
    
    # m = rx+1-lx dimensione dell'output
    
    d = {}
    
    for nome, coordinata in a: # O(n)
        d[coordinata] = nome
    
    
    for p in range(lx-1, rx+1+1):  # O(m)
        if p in d:   # O(1)
            print(d[p], end='')
        else:
            print('*', end='')
            
    print('\nfine')

    # complessità
    # - temporale: O(n + m) in media
    # - spaziale: O(n)



a = [ ('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5) ]

disegna_punti_su_retta(a)