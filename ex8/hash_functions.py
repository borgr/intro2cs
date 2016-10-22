import random
import hashlib
from operator import mul
import collections

def h0(m):
    def h(key):
        return 0
    return h

def h1(m):
    def h(key):
        return ord(key[0]) % m
    return h

def h2(m):
    def h(key):
        x = 0
        for i in range(len(key)):
            ascii_code = ord(key[i])
            x = x + ascii_code
        return x % m
    return h
    
    
def h3(m):
    def h(key):
        x = 0
        for i in range(len(key)):
            ascii_code = ord(key[i])
            x = 128 * x + ascii_code
        return x % m
    return h

def h4(m):
    def h(key):
        return random.randrange(m)
    return h 
    
def h5(m):
    def h(key):
        if isinstance(key, int):
            return key % m
        elif isinstance(key, str):
            return h(str_to_int(key))
        elif isinstance(key, collections.Hashable):
            return h(key.__str__())
        else:
            return None
    return h
    
def str_to_int(text):
    if isinstance(text, str):
        value = 0
        for i in range(len(text)):
            value = ((value << 4) ^ ord(text[i]))
        return value
    else:
        return None
    
def h6(m):
    def h(key):
        if (len(key)==0):
            return 0
        value = ord(key[0]) << 7
        for char in key:
            value = mul(1000003, value) ^ ord(char)
            value = value ^ len(key)
        return value % m
    return h
 
def h7(m):
    def h(key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16) % m
    return h
    
def h8(m):
    def h(key):
        return int(hashlib.sha1(key.encode()).hexdigest(), 16) % m
    return h

def h9(m):
    def h(key):
        return hash(key) % m
    return h

hash_functions = [h0,h1,h2,h3,h4,h5,h6,h7,h8,h9]
