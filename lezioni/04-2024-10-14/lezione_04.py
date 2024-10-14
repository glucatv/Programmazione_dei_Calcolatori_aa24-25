# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 07:47:26 2024

@author: gianluca
"""

# In[Esercizio 1]

a = 'programmazione dei calcolatori'

spaces = 0

i = 0

while i < len(a):   
    # calcolare il numero di spazi in 'a' a partire dalla
    # posizione 'i'
    
    spaces_from_i = 0
    #j = i
    while i+spaces_from_i < len(a) and a[i+spaces_from_i] == ' ':
        spaces_from_i += 1
        #j += 1  # risparmio di una variabile
    
    spaces += spaces_from_i
    i += spaces_from_i + 1
    
print(spaces)

# In[Esercizio 2]

a = 'programmazione dei calcolatori'

vocali = 0

i = 0

while i < len(a):   
    # calcolare il numero di spazi in 'a' a partire dalla
    # posizione 'i'
    
    vocali_da_i = 0
    #j = i
    while i+vocali_da_i < len(a) and a[i+vocali_da_i] in 'aeiou':
        vocali_da_i += 1
        #j += 1  # risparmio di una variabile
    
    vocali += vocali_da_i
    i += vocali_da_i + 1
    
print(vocali)

# In[IF]

#   if condizione:
#       blocco

a = 'programmazione dei calcolatori'

vocali = 0

i = 0

while i < len(a):   
    if a[i] in 'aeiou':
        vocali += 1    
    i += 1
    
print(vocali)

# In[]


# =============================================================================
# if cond0:
#     blocco0
# elif cond1:
#     blocco1:
# elif cond2:
#     blocco3
# else:
#     blocco_default
#     
# if cond:
#     blocco0
# else:
#     blocco1
#     
# if cond0:
#     blocco0
# elif cond1:
#     blocco1:
# 
# =============================================================================

# In[]

a = 'programmazione dei calcolatori'

vocali = 0
for x in a:
    if x in 'aeiou':
        vocali += 1
print(vocali)

# In[Esercizio]

a = 'pr0grammaz10ne de1 c4lc0lator1'

# Stampa a ed sottolineare con * le vocali e con # le
# cifre decimali
#
# Esempio
#
# pr0grammaz10ne de1 c4lc0lator1
#   #  *  * ## *  *#  #  # * * #

b = ''
for x in a:
    if x in 'aeiouAEIOU':
        b += '*'
    elif x >= '0' and x <= '9': # oppure x in '0123456789'
        b += '#'
    else:
        b += ' '

print(a)
print(b)

# In[]

print( ord('a'), ord('b') )
print( ord('A'), ord('B') )
print( ord('0'), ord('1') )

print( chr(100) )

