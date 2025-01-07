#print('programma', 3.14, ['uno', 'due', 3], 6)

#print(min(2, 3, 4, 5, 10, 0))


def concatena(*args):
    a = ''
    for x in args:
        a += x
    return a
        
print(concatena('uno', 'due', 'tre', 'quattro'))


# qual è la complessità temporale di concatena?
# [si assuma len(a) = n]

# siano a0,...,ak le stringhe in args di lunghezza n0,..,nk
# il costo delle concatenazioni nel for:
#
# n0
# n0+n1
# n0+n1+n2
# ....
# n0+n1+....+nk
# il costo totale è O(n**2)


# In[]

def concatena(*args):
    return ''.join(args)

print(concatena('uno', 'due', 'tre', 'quattro'))

#costo temporale O(n) dove n è la lunghezza dell'output

# In[]

b = ['uno', 'due', 'tre', 'quattro']

print(b)

print(' '.join(b))

for x in b:
    print(x, end=' ')
print()

print(*b)  # unpacking

#print('uno', 'due', 'tre', 'quattro')

# In[]

p = [(3, 1), (10, -3), (2, 6), (8, -6)]

# In[moduli]

import math

print( math.cos(3.14/2) )

# In[]

import math as m

print(m.sin(0))

# In[]

from math import tan

print(tan(3.14/4))

# In[matplotlib]

import matplotlib.pyplot as plt

plt.plot([0, 3, 9, 4], [1, -3, 2, 10])


# In[]

p = [(3, 1), (10, -3), (2, 6), (8, -6)]

x = [ x0 for x0, _ in p ]
y = [ x1 for _, x1 in p ]

plt.plot(x, y)

# In[]

a = [0, 1, 2, 3]
b = ['zero', 'uno', 'due', 'tre']
c = ['0', '1', '2', '3']

print(list(zip(a,b,c)))




# In[]

# zip(*p) è zip( (3,1), (10, -3), (2, 6), (8,-6) ) 

for x in zip(*p):
    print(x)
    
# In[]

print(list(zip(*p)))

x, y = list(zip(*p))

plt.plot(x, y)

# In[]

f = open('testo.txt')

for line in f:
    print(line, end='')

f.close()

# In[]

f = open('nuovo_file.txt', 'w')

f.write('prima stringa')

f.close()

f = open('nuovo_file.txt', 'a')

f.write('\nseconda stringa')

f.close()
