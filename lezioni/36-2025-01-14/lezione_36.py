# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:26:41 2025

@author: gluca
"""

# In[]


a = "Questa, è la. striNga: più  noiosa dell'anno e questa no"

def lista_parole(a):
    
    b = []
    
    acc = { 'è': 'e', 'é':'e', 'ò':'o', 'ù':'u', 'à':'a', 'ì':'i'}
    
    for x in a:
        if x.isalpha():
            x = x.lower()
            if x in acc:
                x = acc[x]
            elif  x < 'a' or x > 'z':
                continue    
            b.append(x.lower()) 
            # b += x.lower() # costo lineare nella dim di b
        else:
            #b += ' ' coto lineare
            b.append(' ')
            
    return ''.join(b).split()



def firma(x):
    # ritorna la stringa delle lettere nella parola x ordinate in modo 
    # crescente
    return ''.join(sorted(x))

# In[]




nome_file = 'promessi_sposi.txt'

f = open(nome_file)


# costruire il dizionario delle firme
d ={} # d[k] = insime di parole con firma k

for line in f:
    # estrarre le parole da line
    for p in lista_parole(line):
        k = firma(p)
        if k in d:
            d[k].add(p)
        else:
            d[k] = set([p])
    

            
f.close()

# In[]

d_clean = {}

c = 0
for k in d:
    if len(d[k]) > 1:
        d_clean[k] = d[k]
        
        