import itertools
def is_two_palindrome(txt):
    """

    Note that the many +1 and -1 are to get the right results
    with even and odd numbers.
    even //2 = exactly half
    odd // 2 = half (and a bit)
    so:
    even+1 //2 = still half
    odd+1 //2 = one over
"""
    return (txt[:len(txt)//2] == txt[len(txt)//2-1::-1] and
            txt[(len(txt)+1)//2:] == txt[:(len(txt)+1)//2-1:-1])

def uni_sort(ls1, ls2):
    """
"""
    return sorted([obj for indx, obj in enumerate(ls1+ls2)
            if indx == (ls1+ls2).index(obj)])


def dot_product(ls1, ls2):
    return sum([ls1[indx]*ls2[indx]
                for indx in range(min(len(ls1),len(ls2)))])


def list_intersection(ls1, ls2):
    return sorted(list(set(ls1)&set(ls2)))

def list_difference(ls1, ls2):
    return sorted(list(set(ls1)^set(ls2)))

##def list_intersection(ls1, ls2):
##    return sorted([obj for indx, obj in enumerate(ls1) if obj in ls2 and
##             indx == (ls1+ls2).index(obj)])
##
##def list_difference(ls1, ls2):
##    return sorted([obj for obj in ls1 + ls2 if (obj in ls1 and obj not in ls2)
##                   or (obj in ls2 and obj not in ls1)])
import random, string
def random_string(n):
    """
"""
    return "".join([random.choice(string.ascii_lowercase) for number
                    in range(n)])


def word_mapper(txt):
    """
"""
##one-liner is easy, but double doing dome of the job
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
    print(gen, "gen")
    if gen>1:
        print(gen, gimme_a_genexp(f,start,gen-1))
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
import itertools

def acc(x0,f):
    return accumulate([1, 1], f)
