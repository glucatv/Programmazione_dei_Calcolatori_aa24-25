# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:13:38 2024

@author: gluca
"""

# In[Ordinare date]

a = ['09-12-2024', '10-12-2022', '18-10-2023']

#print(sorted(a))


# il parametro key di sorted è utilizzato per attribuire il valore
# agli elementi nei confronti
#
# la posizione di e1 e e2  viene stabilito in base a key(e1) < key(e2)

def f(e):
    '''

    Parameters
    ----------
    e :una stringa della forma 'dd-mm-yyyy'

    Returns
    -------
    una tupla della forma ('yyyy', 'mm', 'gg')

    '''
    
    return (e[6:], e[3:5], e[:2])
    # oppure return e.split('-')[::-1]

print(sorted(a, key=f))

# In[stesso problema risolto senza utilizzo parametro key]

a = ['09-12-2024', '10-12-2022', '18-10-2023']

# list comprehension
b = [ e.split('-')[::-1]   for e in a  ]

# equivalente a ...
# b = []
#
# for e in a:
#    b.append(e.split('-')[::-1])


b.sort()

print(b)

for i in range(len(b)):
    b[i] = '-'.join(b[i])
    
print(b)