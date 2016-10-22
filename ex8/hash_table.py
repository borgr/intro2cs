import random

def is_prime( m ):
    """ probabilistic test for m's compositeness """
    for i in range(0 ,100):
        a = random . randint (1 ,m -1) # a random integer in [1..m-1]
        if pow (a ,m -1 , m ) != 1:
            return False
    else:
        return True
    
def next_prime ( start ):
    """ returns the a prime number > start """
    for i in range( start ,2* start ):
        if is_prime (i ):
            return i

def contained(key, list_of_items):
    """ checks if item is a member in list_of_items
    returns location in list (if found), or None"""
    try:
        return list_of_items.index(key)
    except ValueError:
        return None
    
class hash_table:
    def __init__(self, mod, func = hash):
        self._keytable = [[] for i in range(mod)]
        self._valtable = [[] for i in range(mod)]
        self._func = func
        self._mod = mod

    def insert(self, key, val):
        i,k = self.find(key)

        if k is None :
            self._keytable[i].append(key)
            self._valtable[i].append(val)
        else:
            self._keytable[i][k]=key
            self._valtable[i][k]=val
        return None

    def find(self, key):
        i = self._func(key) % self._mod
        k = contained (key, self._keytable[i])
        return i,k
 
    def get(self, key):
        i,k = self.find(key)
        if k is None:
            return None
        else:
            return self._valtable[i][k]
 
    def get_load(self):
        return [len(elem) for elem in self._keytable]
