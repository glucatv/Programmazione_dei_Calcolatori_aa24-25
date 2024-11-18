# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:23:20 2024

@author: gianluca
"""

nomi = ['A', 'B', 'A', 'C', 'B', 'D', 'A', 'C']
pos  = [ 3,   1,   2,   0,   1,  2,   4,   2]

# al tempo, i pos[i] è la nuova posizione di nomi[i]


# qual è l'ultima configurazione dei punti? Ovvero la posizione dei
# punti alla fine della serie temporale

# d[k] = p se il punto k si trova in posizione p

n = len(nomi)

d = {}

for i in range(n):
    d[nomi[i]] = pos[i]   # tempo medio O(1) 
    
    
# complessità temporale: O(n) medio

# In[funzione zip]

d = {}

for nome, p in zip(nomi, pos):
    d[nome] = p
    
# In[metodi di dict]

print(d.keys())
print(d.values())
print(d.items())

# In[]

nomi = ['A', 'B', 'A', 'C', 'B', 'D', 'A', 'C']
pos  = [ 3,   1,   2,   0,   2,  2,   4,   2]


d = {}

# d[nome] = [lista dei posizioni occupate da nome]

for nome, p in zip(nomi, pos):
    if nome in d:
        d[nome].append(p) 
    else:
        d[nome] = [p]
        
print(d)

# In[metodo get]

d = {'a':2, 'b':1}

print( d.get('a') )
print( d.get('c') )
print( d.get('c', 0) )

# In[]

nomi = ['A', 'B', 'A', 'C', 'B', 'D', 'A', 'C']
pos  = [ 3,   1,   2,   0,   2,  2,   4,   2]

# d[k] = somma delle posizioni in cui compare k

d = {}

for nome, p in zip(nomi, pos):
    if nome in d:
        d[nome] += p 
    else:
        d[nome] = p

print(d)


# In[con get]

d = {}

for nome, p in zip(nomi, pos):
    d[nome] = d.get(nome, 0) + p

print(d)


# In[]

d = {'A': 9, 'B': 3, 'C': 2, 'D': 2, 'E':9}

# d_inv[v] = [lista di chiavi di d che hanno per valore v] 

d_inv = {}

for k in d:
    v = d[k]
    if v in d_inv:
        d_inv[v].append(k)
    else:
        d_inv[v] = [k]
        
print(d_inv)


# In[con metodo items]

d = {'A': 9, 'B': 3, 'C': 2, 'D': 2, 'E':9}

d_inv = {}

for k, v in d.items():
    if v in d_inv:
        d_inv[v].append(k)
    else:
        d_inv[v] = [k]
        
# In[con metodo key e values]
d = {'A': 9, 'B': 3, 'C': 2, 'D': 2, 'E':9}

d_inv = {}

for k, v in zip(d.keys(), d.values()):
    if v in d_inv:
        d_inv[v].append(k)
    else:
        d_inv[v] = [k]
        
print(d_inv)

# In[]


def intersezione(a, b):
    #n, m = len(a), len(b)
    
    da, db = {}, {}
    
    for e in a: # O(n) tempo, O(n) spazio 
        da[e] = None  # non mi interessa il valore
        
    for e in b: # O(m) tempo, O(m) spazio
        db[e] = None  # O(1) tempo nel coso medio
    
    c = []
    
    if len(da) < len(db):
        d0, d1 = da, db
    else:
        d0, d1 = db, da
    
    for e in d0:  # per min(n,m) volte
        if e in d1:  # O(1) tempo nel caso medio
            c.append(e)
            
    
    # complessità temporale: O(n+m+n)
    # complessità spaziale: O(n+m)
    
    return c


a = [9, 2, 1, 8, 4] 
b = [1, 7, 0, 8, 2, 10 ,8, 12, 6, 1, 6, 1, 0, 4, 5, 7, 0, 1, 5, 4, 9] 

c = intersezione(a, b)
print(c)

# In[]

def intesezione(d0, d1):
    '''
    Input: d0 d1 dizionari
    Output: d dizionario le cui chiavi sono quelle sia in d0
        che in d1
    '''
    d = {}
    
    # n, m = len(d0), len(d1)
    
    if len(d0) < len(d1):
        d0, d1 = d0, d1
    else:
        d0, d1 = d1, d0
        
    
    for e in d0:  # per min(n,m) volte
        if e in d1:  # O(1) tempo nel caso medio
            d.append(e)
    
    # complessità temporale O(min(len(d0), len(d1)))
    
    return d


d0 = {'a': None, 'b': None, 'c':None, 'd':None}
d1 = {'a': None, 'b': None}

print(intersezione(d0,d1))
