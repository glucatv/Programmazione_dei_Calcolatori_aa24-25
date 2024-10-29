# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 09:21:48 2024

@author: gianluca
"""

# In[]

def disegna_punti_su_retta(a):
    def t1(e):
        return e[1]
    
    # n = len(a)
    
    lx = min(a, key=t1)[1]
    rx = max(a, key=t1)[1]
    
    m = rx-lx+1
    
    retta = ['*']*m  # Tempo e spazio O(m)
    
    for e, p in a: # Tempo O(n)
        retta[p-lx] = e
        
    print(''.join(retta)) # Tempo O(m)
    
    # Complessità
    # Temporale    O(n+m)
    # Spaziale     O(m)
        
    
a = [ ('A', -6), ('B', -2), ('E', -3), ('C', 0), ('D', -5) ]

disegna_punti_su_retta(a)

# In[Ordinamento]

# BubbleSort

a = [ 6, 1, 9, 0, -4, 5, 8, 10, 4 ]

n = len(a)

for _ in range(n-1):
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
        
# Complessità temporale O(n**2) sempre

# In[]


a = [ 6, 1, 9, 0, -4, 5, 8, 10, 4 ]

n = len(a)

for c in range(n-1):
    for i in range(n-1-c):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            
print(a)

# Complessità temporale O(n**2)

# In[]


a = [ 6, 1, 9, 0, -4, 5, 8, 10, 4 ]

n = len(a)

for c in range(n-1):
    # se non effettua scambi, la lista è ordinata
    terminato = True
    for i in range(n-1-c):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            terminato = False
    if terminato:
        # la lista è ordinata
        break
    
# Complessità temporale O(n**2) nel caso peggiore        
    
print(a)

# In[]

def t1(e):
        return e[1]
    
a = [ ('A', -6), ('B', -2), ('E', -3), ('C', 0), ('D', -5) ]


n = len(a)

for c in range(n-1):
    # se non effettua scambi, la lista è ordinata
    terminato = True
    for i in range(n-1-c):
        if t1(a[i]) > t1(a[i+1]):
            a[i], a[i+1] = a[i+1], a[i]
            terminato = False
    if terminato:
        # la lista è ordinata
        break
    
# In[]

def bubble_sort(a, key=None):
    def identity(e):
        return e

    n = len(a)
    
    if key == None:
        key = identity

    for c in range(n-1):
        # se non effettua scambi, la lista è ordinata
        terminato = True
        for i in range(n-1-c):
            if key(a[i]) > key(a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                terminato = False
        if terminato:
            # la lista è ordinata
            break
        
a = [ ('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5) ]

bubble_sort(a, key=t1)

print(a)


# In[]

def disegna_punti_su_retta(a):
    def t1(e):
        return e[1]
    
    n = len(a)
        
    b = a[:]
    bubble_sort(b, key=t1)  # Tempo O(n**2), spazio O(n)
    
    lx, rx = b[0][1], b[-1][1]
    
    # m = rx-lx+1
    
    i = 0 # indice in b del prossimo punto da stampare
    for p in range(lx, rx+1):
        if i < n and p == b[i][1]:
            print(b[i][0], end='')
            i += 1
        else:
            print('*', end='')   # O(m)
 
    
     # Complessità: tempo O(n**2 + m) nel caso peggiore,
     #              spazio O(n)
    
a = [ ('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5) ]
disegna_punti_su_retta(a)