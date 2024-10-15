# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:22:29 2024

@author: gianluca
"""

print( ord('a'), ord('b') )
print( ord('A'), ord('B') )
print( ord('0'), ord('1') )

print( chr(100) )

# In[]

# da maiuscolo a minuscolo

c = 'D'

if c >= 'A' and c <= 'Z': # c è maiuscolo
    delta = ord(c)-ord('A')
    c_min = chr( ord('a')+delta )
    print(c_min)
    
# In[]

def sqrt( x ):
    g, c = x/2, 0 # variabili locali
    
    eps, c_max = 0.00000000001, 1000
    
    while abs( g - x/g ) >  eps and c < c_max:
        c = c+1
        g = ( g + x/g )/2

    return g # senza il risultato è None
    
ris = sqrt(20)
print(ris)

# In[]

def sqrt( x, eps, c_max ):
    g, c = x/2, 0 # variabili locali
    
    while abs( g - x/g ) >  eps and c < c_max:
        c = c+1
        g = ( g + x/g )/2

    return g # senza il risultato è None
    
ris = sqrt(20, 0.00001, 10)

ris = sqrt(20, c_max = 100, eps = 0.123)
print(ris)

# In[]

def sqrt( x, eps=0.01, c_max=100 ):
    g, c = x/2, 0 # variabili locali
    
    while abs( g - x/g ) >  eps and c < c_max:
        c = c+1
        g = ( g + x/g )/2

    return g # senza il risultato è None
    
print( sqrt(20, 0.00001, 10000) )
print( sqrt(20) )
print( sqrt(20, 0.1) )
print( sqrt(20, c_max=2) )
print( sqrt(c_max = 2, x = 20) )

# In[Problema]

def palindromo( a ):
    n = len(a)    
    i = 0
    
    while i < n/2 and a[i] == a[n-1-i]:
        i += 1
        
    if a[i] != a[n-1-i]:
        return False
    else:
        return True
    
# In[]

def palindromo( a ):
    n = len(a)    
    i = 0
    
    while i < n/2 and a[i] == a[n-1-i]:
        i += 1
        
    if a[i] != a[n-1-i]:
        return False
    
    return True
    

print( palindromo( '012Kayak210' ) )

# In[]

a = '0123456789'

print(a[-2])
print(a[1:7])  # slicing
print(a[:7])
print(a[1:])
print(a[:])
print(a[1:7:2]) # slicing con step
print(a[::-1])

# In[]

def palindromo_ingenua( a ):
    return a == a[::-1]


