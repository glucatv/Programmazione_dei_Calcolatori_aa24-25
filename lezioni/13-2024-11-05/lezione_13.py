# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:19:17 2024

@author: gianluca
"""

# In[Esercizio per casa]

# Data una lista di numeri ordinati in modo non decrescente ed un numero k

a = [1, 5, 5, 7, 7, 7, 9, 9,  10, 13, 13, 14, 17]
k = 7

# Trovare la posizione dell'occorrenza più a destra di k in a: nell'esempio
# l'algoritmo ritorna 5. Se k non è in a, ritorna -1


# In[]

a = [1, 5, 5, 7, 7, 7, 9, 9,  10, 13, 13, 14, 17]
c = a
b = a[:]

print( id(a) == id(b) )
print( id(a) == id(c) )

# In[]

a = [ 'python', [0, 3.14, '2.71'], 100, ['programmazione', 'python'] ]
b = a[:]

a[1][0] = 'uno'
a[0] = 2014

print(b)

# In[Come clonare ai livelli successivi?]

a = [ 'python', [0, 3.14, '2.71'], 100, ['programmazione', 'python'] ]
b = []

for x in a:
    if type(x) == list:
        b.append(x[:])
    else:
        b.append(x)
    
a[1][0] = 'uno'
a[0] = 2014

print(b)

# In[Una prima funzione ricorsiva]

def r_max( a ):
    if len(a) == 1:
        return a[0]
    else:
        m = r_max(a[1:])
        if m > a[0]:
            return m
        else:
            return a[0]

a = [5, 1, 2, 7, 8, 2, 1]    
print(r_max(a))

# Complessità temporale: n = len(a) 
#
# Sia T(n) il numero di operazioni eseguita da r_max() su input di dim
# n
#
# se T(1) = O(1)
#
# altrimenti, siano c e d due costanti
#
# T(n) = c + d(n-1) + T(n-1) 

# = c + d(n-1) + c + d(n-2) + T(n-2) =
# 2c + d(n-1) + d(n-2) + c + d(n-3) + T(n-3) = 3c + d(n-1 + n-2 + n-3) +
# T(n-4) = ....
#
# = kc + d( (n-1)+(n-2)+...+(n-k) ) + T(n-k) = ... =
# = (n-1)c + d( (n-1) + (n-2) + ...+ (1) ) + T(1) =
# (n-1)c + dn(n-1)/2 + O(1) è in O(n**2)

# Complessità spaziale è O(n**2) per via degli slicing

# In[]

def r_max( a, i = 0 ):
    if i == len(a)-1:
        return a[i]
    else:
        m = r_max(a, i+1)
        if m > a[i]:
            return m
        else:
            return a[i]

a = [5, 1, 2, 7, 8, 2, 1]    
print(r_max(a))


# Complessità temporale
# T(n) = c + T(n-1) = (n-1)c  + O(1) in O(n)

# Complessità spaziale

# O(n) per via degli n frame aperti dalle chiamate ricorsive

# In[]

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
