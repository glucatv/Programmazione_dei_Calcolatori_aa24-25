# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:34:28 2024

@author: gianluca
"""

def merge_sort( a, lx = 0, rx = None ):
    '''
        Input: a una sequenza di elementi che possono essere
            confrontati
            lx < rx: indice sinistro e destro di a
        Output: None
        
        Effetto collaterale: ordinare in loco gli elementi di
            a[lx:rx]
    '''
    
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
    
    if rx == None:
        rx = len(a)
    

    if lx+1 >= rx:
        return None
    
    cx = int((lx+rx)/2)
    
    merge_sort(a, lx, cx)
    merge_sort(a, cx, rx)
    merge(a, lx, cx, rx)
  
    
# In[]
    
a = ['programmazione', 'dei', 'calcolatori', '2024/25']
merge_sort(a)
print(a)


# In[lambda function]

v = (lambda x: x**2)(2)

f = lambda x:x

# In[]

def merge_sort( a, key = lambda x:x, lx = 0, rx = None ):
    '''
        Input: a una sequenza di elementi che possono essere
            confrontati
            lx < rx: indice sinistro e destro di a
        Output: None
        
        Effetto collaterale: ordinare in loco gli elementi di
            a[lx:rx]
    '''
    
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
            if key(a[i]) <= key(a[j]):
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
    
    if rx == None:
        rx = len(a)
    

    if lx+1 >= rx:
        return None
    
    cx = int((lx+rx)/2)
    
    merge_sort(a, key, lx, cx)
    merge_sort(a, key, cx, rx)
    merge(a, lx, cx, rx)

a = ['programmazione', 'dei', 'calcolatori', '2024/25']
merge_sort(a)
print(a)

# In[]

a = [10.4, 3.14, 'programmazione', 0, 'dei', 'calcolatori', 8, '2024/25']

def f(x):
    if type(x) in (int, float):
        return 0
    else:
        return 1

#merge_sort(a, key=f)

# oppure

merge_sort(a, key = lambda x: 0 if type(x) in (float, int) else 1)

print(a)

# In[]

def f(x):
    if type(x) in (int, float):
        return (0, x)
    elif type(x) == str:
        return (1, x)

a = [10.4, 3.14, 'programmazione', 0, 'dei', 'calcolatori', 8, '2024/25']

merge_sort(a, key = f)

print(a)

# In[sorted]

a = (10, 9, 11, 0, 4)
print(sorted(a)) # ritorna una lista

print(sorted('python'))

a = [10.4, 3.14, 'programmazione', 0, 'dei', 'calcolatori', 8, '2024/25']
   
print(sorted(a, key=str))

# In[metodo sort del tipo list]

a = [10, 9, 11, 0, 4]

a.sort()

print(a)
    
a = [10.4, 3.14, 'programmazione', 0, 'dei', 'calcolatori', 8, '2024/25']

a.sort(key=str)

print(a)

a = [10.4, 3.14, 'programmazione', 0, 'dei', 'calcolatori', 8, '2024/25']

a.sort(key=str)

