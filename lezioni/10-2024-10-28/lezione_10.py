# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 09:12:29 2024

@author: gianluca
"""

# In[Confronto tra sequenze (tuple, liste, stringhe)]

print ( (1, 3, 1) < (1, 2, 2) )

# print ( ('A', 3, 1) < (1, 2, 2) ) # TypeError

print ( (1, 3, 0) < (1, 3, 1, 2) )

print ( (1, 3, 1) < (1, 3, 1, 2) ) # tupla prefissa

# In[]

a = [ ('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5) ]

# non utilizzare memoria aggiuntiva, non modificare input

# determinare lx e rx (estremi dell'intervallo)

lx = a[0][1]

for e, p in a: # for _, p in a:
    if p < lx:
        lx = p
        

# In[]

def Max(a, key=None):
    '''
    Input: a una lista, key una func
    Output: e in a tale che key(e) = max(key(x) per x in a)
        se key è None massimizza e
    '''
    
    def identity(e):
        return e
    
    
    if key == None:
        key = identity
        
    v_max = key( a[0] )
    r_max = a[0]

    for e in a:
        if key(e) > v_max:
            v_max, r_max = key(e), e
            
    return r_max


def t1(e):
    return e[1]
    
a = [ ('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5) ]

print(Max(a))
print(Max(a, key=t1))

# In[]

# il parametro key delle funzioni incorporate min() e max()
# è lo stesso  della funzione Max()

print(max(a, key=t1)) 


# In[]

def disegna_punti_su_retta(a):
    def t1(e):
        return e[1]
    
    # n = len(a)
    
    lx = min(a, key=t1)[1]
    rx = max(a, key=t1)[1]
    
    for p in range(lx-1, rx+1+1):
        c = '*'
        for e, v in a:
            if p == v:
                c = e
        print(c, end='') # O(1) perché c è un carattere
        
    print('\nfine')

a = [ ('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5) ]

disegna_punti_su_retta(a)

# Complessità temporale: sia m = rx-lx (dimensione dell'output)
#
# costo = O(n*m) almeno quadratico in n
#
# Complessità spaziale: O(1)

# In[]

# Si può ridurre la complessità temporale, eventualmente
# a scapito di quella spaziale?

