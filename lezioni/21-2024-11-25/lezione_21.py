# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:06:43 2024

@author: gluca
"""

def anagramma(a, b):
    '''
       Parametri: a, b stringhe
       Return: True se e solo se a e b sono anagrammi
    '''
    da, db = {}, {} 
    
    for x in a:
        da[x] = da.get(x, 0) + 1 # O(1) in media
    for x in b:
        db[x] = db.get(x, 0) + 1
        
    for x in da:
        if da[x] != db.get(x, 0):  # O(1) in media
            return False
        # equivalente a...
        #if x not in db or da[x] != db[x]:
        #    return False
    
    for x in db:
        if da.get(x, 0) != db[x]:
            return False
        
    return True

a = 'AABCDAABD'
b = 'BABCADADA'
    
print(anagramma(a, b))   