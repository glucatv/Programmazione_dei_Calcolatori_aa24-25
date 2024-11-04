# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:14:16 2024

@author: gianluca
"""

def ricerca_intervallo(a, k):
    '''
    Input: a, una lista di numeri ordinati in modo crescente, valori consecutivi
        in a rappresentano un intervallo chiuso a sinistra e aperto a destra;
        k, un numero
    Output: se k>=a[0] e k < a[-1], una coppia (a[i], a[i+1]) che rappresenta
        l'intervallo contenente k; se k < a[0] la funzione ritorna ('-inf', a[0]);
        se k >= a[-1] la funzione ritorna (a[-1], '+inf')
    '''
    lx, rx = 0, len(a)-1
    
    if k < a[0]:
        return ('-inf', a[0])
    
    if k >= a[-1]:
        return (a[-1], '+inf')
    
    while lx <= rx:
        cx = int( (lx+rx)/2 )
        if k == a[cx]:
            return ( a[cx], a[cx+1])
        elif k < a[cx]:
            rx = cx-1
        else:
            lx = cx+1
     
    if k < a[cx]:
        return ( a[cx-1], a[cx]) 
    elif k > a[cx]:
        return ( a[cx], a[cx+1] )
    

# complessità spaziale: O(1)
# complessità temporale: O(log_2 n)
    
a = [-2, 3, 9, 12, 13]
k = 4

print( ricerca_intervallo(a, k) )


