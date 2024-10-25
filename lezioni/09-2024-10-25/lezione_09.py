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


           
L = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]
del_item(L, 1)
print(L)


# Complessità temporale: O(n**2)

# In[]
def f(x):
    a = x+[0]*g(x)
    return len(a)
    
def g(x):
    n = len(x)
    return n

L = [0,1,2]
n = f(L)
print(n)

# In[]

# def del_item(a, v):
#     '''
#     Input: a una lista; v un valore
#     Return: None
    
#     Elimina da a tutte le occorrenze di v
#     '''

#     b = []
    
#     for x in a:
#         if x != v:
#             b.append(x)

#     return b

# # # NON CORRETTA PERCHé NON RISPETTA LE SPECIFICHE
           
# L = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]
# L = del_item(L, 1)
# print(L)

# In[]

# def del_item(a, v):

#     b = []
    
#     for x in a:
#         if x != v:
#             b.append(x)

#     a = b
    
# # NON CORRETTA PERCHé MODIFICA VARIABILI LOCALI

# L = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]
# del_item(L, 1)
# print(L)

# In[]

def del_item(a, v):

    b = []
    
    for x in a:
        if x != v:
            b.append(x)
            
    i = 0
    while i < len(b):
        a[i] = b[i]
        i += 1
        
    # i è la posizione del primo elemento da eliminare da a
    while i < len(a):
        del(a[i])
        
L = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]
del_item(L, 1)
print(L)

# soluzione corretta ma ancora non efficiente, l'ultimo while
# ha costo quadratico nel caso peggiore

# In[]

def del_item(a, v):

    b = []
    
    for x in a:
        if x != v:
            b.append(x)
            
    i = 0
    while i < len(b):
        a[i] = b[i]
        i += 1
        
    # i è la posizione del primo elemento da eliminare da a
    while i < len(a):
        del(a[-1])
        
L = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]
del_item(L, 1)
print(L)

# complessità temporale O(n)

# In[]


