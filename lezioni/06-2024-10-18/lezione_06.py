# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:26:40 2024

@author: gianluca
"""




a0 = ' programmazione dei calcolatori con laboratorio     '
a1 = ' linguaggi di programmazione:c; python,java'

def lettera(c):
    return c >= 'a' and c <= 'z'

def conta_parole( a ):
    '''
    Input: a una stringa
    Return: numero di parole nella stringa.
    
    Una parola è una sequenza massimale di caratteri alfabetici
    minuscoli
    '''
    
    #### ^^^ Docstring ^^^
    
    
    # n = len(a)
    
    parole = 0
    in_parola = False
    
    for c in a:
        if lettera(c):  # numero costante di operazioni c0
            if not in_parola: # numero costante di ops c1
                parole += 1 # numero costante di ops c2
                in_parola = True # numero costante di ops c3
        else:
            if in_parola: # numero costante di ops c4
                in_parola = False # numero costante di ops c3
        # costo del blocco:
        #
        #    c0+c1+c2+c3 oppure c0+c1 oppure c0+c4+c5
        #    oppure  c0+c4
        #
        # in ogni caso è costante (diciamo c)
    
    return parole

    # Il costo della funzione è n*c + d dove d è una costante
    # e rappresenta il costo delle inizializzazione e del return
    # 
    # Al crescere di n, la costante d diventa sempre più ininfluente,
    # quindi va tolta. In generale rimangono soltanto i termini di ordine
    # superiore.
    #
    # Il costo c*n risente dalla costante c che a sua volta può dipendere da
    # fattori incontrollabili (implementazione a basso livello delle operazioni
    # elementari), quindi anche le costanti moltiplicative vengono eliminate
    #
    # Rimane l'ordine di grandezza della funzione...


print( conta_parole(a1) )

