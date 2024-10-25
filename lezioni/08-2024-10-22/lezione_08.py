# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:22:39 2024

@author: gianluca
"""

a = [ ('A', 2,7), ('B',3, -1), ('C', 0, 1), ('D', -2,-2) ]
r = 2.9

# n = len(a)

# creare una lista che contiene i nomi dei punti in a a distanza al 
# più r da (O, 0,0)

b = []

for nome, x, y in a:
    if x**2+y**2 <= r**2:
        b.append(nome) # tempo costante "in media" O(1)
    
print(b)

# complessità temporale è O(n) in media?
#
# proprietà: nel caso peggiore n append() consecutivi
#    costano complessivamente O(n)
# 
# quindi l'algoritmo precedente ha complessità temporale O(n)
# nel caso peggiore

# In[]

def trova_posizioni(a, v):
    '''
    Input: a una lista, v un valore
    Return: una lista di interi contenente le posizioni di v in a
    '''
    
    # n = len(a)
    
    b = []
    
    i = 0
    while i < len(a): # O(1) 
        if a[i] == v: # O(1) perché indicizzazione ha costo costante
            b.append(i)
        i += 1
            
    return b

    # complessità temporale O(n) nel caso peggiore


a = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]
p = trova_posizioni(a, 6)
print(p)

# In[]

a = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]
n = len(a)

for i in range(n):
    print(a[i])

# In[versione con for]

def trova_posizioni(a, v):
    '''
    Input: a una lista, v un valore
    Return: una lista di interi contenente le posizioni di v in a
    '''
    
    # n = len(a)
    
    b = []
    
    for  i in range( len(a) ): # O(1) 
        if a[i] == v: # O(1) perché indicizzazione ha costo costante
            b.append(i)
            
    return b

a = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]
p = trova_posizioni(a, 6)
print(p)

# In[]

a = 'pr0grammaz10ne de1 c4lc0lator1'

# n = len(a)

# Stampa a ed sottolineare con * le vocali e con # le
# cifre decimali
#
# Esempio
#
# pr0grammaz10ne de1 c4lc0lator1
#   #  *  * ## *  *#  #  # * * #

b = ''
for x in a:
    if x in 'aeiouAEIOU': # O(1)
        b += '*'
    elif x >= '0' and x <= '9': # O(1)'
        b += '#'
    else:
        b += ' ' # O(i) dove i è la dimensione attuale di b
        
# numero di operazioni = 1+2+...+(n-1)+n in Theta(n**2)
# quindi la complessitò temporale è quadratica

print(a)
print(b)

# In[]

b = []
for x in a:
    if x in 'aeiouAEIOU': # O(1)
        b.append( '*' ) # O(1)
    elif x >= '0' and x <= '9': # O(1)'
        b.append( '#' ) # O(1)
    else:
        b.append( ' ' ) # O(1)
      
print(a)
print( ''.join(b) )   # O(n)

# In[]

a = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]

# n = len(a)

b = a # aliasing O(1)

print(a)

b[0] = 100

print(a)

c = a[:] # copia di a O(n)

a[1] = 200

print(a)
print(b)
print(c)

print( id(a) )
print( id(b) )
print( id(c) )

# In[Esercizio]

# def del_item(a, v):
#     '''
#     Input: a una lista; v un valore
#     Return: None
    
#     Elimina da a tutte le occorrenze di v
#     '''
    
#     for i in range(len(a)):
#         if a[i] == v:
#             del(a[i])
#
# Soluzione errata, range(len(a)) viene valutata soltanto la prima
# volta quindi la sequenza generata da range() dipenderà soltanto
# dal valore iniziale di len(a)   
 
def del_item(a, v):
    '''
    Input: a una lista; v un valore
    Return: None
    
    Elimina da a tutte le occorrenze di v
    '''

    i = 0

    while i < len(a):
        if a[i] == v:
            del(a[i])  # O(n)
        else:
            i += 1


           
a = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]
del_item(a, 1)
print(a)





