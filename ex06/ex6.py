import itertools
def is_two_palindrome(txt):
    """ This function checks if she got a two palindrome

    Args:
    txt - any string

    Return:
    True if txt is a two palindrome otherwise False.
"""
##    Note:
##    The many +1 and -1 are to get the right results
##    with even and odd numbers.
##    even //2 = exactly half
##    odd // 2 = half (and a bit)
##    so:
##    even+1 //2 = still half
##    odd+1 //2 = one over

    return (txt[:len(txt)//2] == txt[len(txt)//2-1::-1] and
            txt[(len(txt)+1)//2:] == txt[:(len(txt)+1)//2-1:-1])

def uni_sort(ls1, ls2):
    """ This function returns a sorted list of the objects
    that exist in either ls1 or ls2

    Args:
    ls1,ls2 - two lists

    Return:
    A sorted list of the objects
    that exist in either ls1 or ls2.
"""
    return sorted([obj for indx, obj in enumerate(ls1+ls2)
                   if indx == (ls1+ls2).index(obj)])


def dot_product(ls1, ls2):
    """ Returns the dot product of thw two lists

    Args:
    ls1, ls2 - lists with integers

    Return:
    A list containing their dot product, shorter list considered as ending with 0
    (ls1 - [1] ls2 - [2,3,4] >>> ls1 - [1,0,0])
"""
    return sum([ls1[indx]*ls2[indx]
                for indx in range(min(len(ls1),len(ls2)))])


def list_intersection(ls1, ls2):
    """ A function that returns the intersection of 2 lists.

    Args:
    ls1,ls2 - lists

    Return:
    A new lists consisting of ls1 and ls2 intersection.
"""
    return sorted(list(set(ls1)&set(ls2)))

def list_difference(ls1, ls2):
    """ A function that returns the difference of 2 lists.

    Args:
    ls1,ls2 - lists

    Return:
    A new lists consisting of ls1 and ls2 difference.
"""
    return sorted(list(set(ls1)^set(ls2)))

import random, string
def random_string(n):
    """ A function that generates n random lowercase ascii letters

    Args:
    n - a positive number

    Return:
    A string consisting of n random lowercase ascii letters
"""
    return "".join([random.choice(string.ascii_lowercase) for number
                    in range(n)])


def word_mapper(txt):
    """ A function that counts words and numbers

    Args:
    txt - any string

    Return:
    a dictionary that tells how many times each number (not to be confused with digit)
    and each word (not char) are in the text.
"""
##one-liner is easy, but double doing some of the job
    return ({key: "".join([char.lower()
                           if char not in string.punctuation
                           and char not in string.whitespace
                           else " "
                           for char in txt]).split().count(key)
             for key in "".join([char.lower()
                                 if char not in string.punctuation
                                 and char not in string.whitespace
                                 else " " for char in txt]).split()})
# this will be a faster solution, in more lines....

##x = "".join([char.lower() if char not in string.punctuation
##             and char not in string.whitespace
##             else " " for char in txt]).split()
##return ({key: x.count(key) for key in x})

def gimme_a_value(f, start):
    """ this function creates a generator for recursive use
    of the given function starting.
    or a generator for the solutions for
    an = f(f(f(...n times... (start)))) a1 = start

    Arguments:
    f - f as stated in the task, any function.
    start - x0 as stated in the task, any argument f should get.

    Return:
    a generator for an, as defined above.

    Note:
    if the function returns something it can not get as an argument,
    it will fail.
    """
    while True:
        start = f(start)
        yield start

def gimme_a_genexp(f, start, gen = -float("inf")):
    """ this function creates a generator for recursive use
    of the given function starting.
    or a generator for the solutions for
    an = f(f(f(...n times... (start)))) a1 = start

    Arguments:
    f - f as stated in the task, any function.
    start - x0 as stated in the task, any argument f should get.

    Return:
    a generator for an, as defined above.

    Note:
    if the function returns something it can not get as an argument,
    it will fail.
    """
    # this is themostefficient way    
##    return (eval(("f("*itrat) +str(start) + (")"*itrat)) for itrat in itertools.count() )
##    if gen == -float("inf"):
##        return (gimme_a_genexp(f, start, itrat) for itrat in range(1,5))
##    return f(gimme_a_genexp(f,start,gen-1)) if gen!=1 else start
    return ((gimme_a_genexp(f,start,itrat) for itrat in itertools.count(1)) if gen == -float("inf")
            else f(gimme_a_genexp(f,start,gen-1)) if gen!=1 else start)

        
##    return f(gimme_a_genexp(f,start,gen-1)) if gen!=1 else start                                  
##    return (lambda x: f(start)+gimme_a_genexp(f, x))(start-1) if start !=0 else 1
##    return [self[i] if i >= 1 else 2 for i in itertools.count()]
    #return itertools.count(-start + f(start), f(start))
##    return [x for indx in itertools.count() for func_num in range(indx)
##    return map(f, [reduce(f, cycle()
##                          lambda x: 
