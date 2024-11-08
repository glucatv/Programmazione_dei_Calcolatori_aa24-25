# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:55:05 2024

@author: gianluca
"""

def deep_copy(a):
    
    b = []
    for e in a:
        if type(e) != list:
            b.append(e)
        else:
            b.append(deep_copy(e))
    return b

a = [ 'python', [0, 3.14, '2.71'], 100, ['programmazione', 'python'] ]
b = deep_copy(a)

# complessità temporale:
#
# la dimensione dell'input è data dal numero degli elementi scalari in a
# ed in tutte le sottoliste annidate
#
# T(n) lineare in n
#
# complessità spaziale
#
# 
# a = [0,[1, [2, [3,[4,[5,[6]]]]]]] n annidamenti
#
# caso peggiore O(n)

# In[]

# Data una lista di numeri ordinati in modo non decrescente ed un numero k
# Trovare la posizione dell'occorrenza più a destra di k in a: nell'esempio
# l'algoritmo ritorna 5. Se k non è in a, ritorna -1

def ricerca_dx(a, k):
    n = len(a)
    lx, rx = 0, len(a)-1
    
    while lx <= rx:
        cx = int( (lx+rx)/2 )
        if k < a[cx]:
            rx = cx-1
        elif k == a[cx] and ( cx == n-1 or a[cx+1] > k ):
            return cx
        else:
            lx = cx+1
    
    return -1

a = [1, 5, 5, 7, 7, 7, 9, 9,  10, 13, 13, 14, 17]
k = -10

print( ricerca_dx(a, k) )

# In[]

