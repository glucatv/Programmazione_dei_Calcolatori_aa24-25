# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:28:33 2024

@author: gianluca
"""

# In[Algoritmo di fusione o merge]

# ordina due sequenze ordinate in un'unica sequenza

a = [0, 5, 8, 10, 11, 11, 14]
b = [1, 2, 6, 6, 6, 9, 10]

i, j = 0, 0
c = []
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

while i < len(a):
    c.append(a[i])
    i+=1
    
while j < len(b):
    c.append(b[j])
    j += 1
    
# complessità temporale: O(n) dove n = len(a)+len(b)
# complessità spaziale: O(1), non ci sono strutture di appoggio



# In[]

def merge(a, lx, cx, rx):
    '''
        Input: a una lista di elementi
            lx, cx e rx indici in a t.c. lx <= cx <= rx
            con la proprietà che a[lx:cx] e a[cx:rx] sono ordinate
        Output: None
        
        Effetto collaterale a[lx:rx] è ordinata
    '''

    i, j = lx, cx
    c = []
    while i < cx and j < rx:
        if a[i] <= a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1
    
    while i < cx:
        c.append(a[i])
        i+=1
        
    while j < rx:
        c.append(a[j])
        j += 1
        
    i = lx
    for e in c:
        a[i] = e
        i += 1
        
    # complessità temporale: O(n) dove n è la lunghezza
    #    della sottosequenza da ordinare
    # complessità spaziale: O(n) per via della lista c
    
a = [10, 21, 0, 30, 34, 34, 38, 11, 13, 16, 17, 19, 0, 0, 10, 10]
merge(a, 3,7,12)
print(a)

# In[]

def merge_sort( a, lx = 0, rx = None ):
    '''
        Input: a una sequenza di elementi che possono essere
            confrontati
            lx < rx: indice sinistro e destro di a
        Output: None
        
        Effetto collaterale: ordinare in loco gli elementi di
            a[lx:rx]
    '''
    
    if rx == None:
        rx = len(a)
    

    if lx+1 >= rx:
        return None
    
    cx = int((lx+rx)/2)
    
    merge_sort(a, lx, cx)
    merge_sort(a, cx, rx)
    merge(a, lx, cx, rx)
    
    # complessità temporale: O(n log_2 n)
    # complessità spaziale: O(log_2 n) + O(n) = O(n)
    #
    # vedere dispense

a = [10, 21, 30, 34, 34, 38, 11, 13, 16, 17, 19, 0, 0, 10, 10]
merge_sort(a)
print(a)

