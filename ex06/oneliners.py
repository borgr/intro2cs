import itertools
import random
import string


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

    return (True if len(txt) == 1
            else (txt[:len(txt)//2] == txt[len(txt)//2-1::-1] and
                  txt[(len(txt)+1)//2:] == txt[:(len(txt)+1)//2-1:-1]))


def uni_sort(list1, list2):
    """ This function returns a sorted list of the objects
    that exist in either list1 or list2

    Args:
    ls1,list2 - two lists

    Return:
    A sorted list of the objects
    that exist in either list1 or list2.
"""
    return sorted([obj for indx, obj in enumerate(list1+list2)
                   if indx == (list1+list2).index(obj)])


def dot_product(list1, list2):
    """ Returns the dot product of thw two lists

    Args:
    list1, list2 - lists with integers

    Return:
    A list containing their dot product, shorter list
    considered as ending with 0
    (list1 - [1] list2 - [2,3,4] >>> list1 - [1,0,0])
"""
    return sum([list1[indx]*list2[indx]
                for indx in range(min(len(list1), len(list2)))])


def list_intersection(list1, list2):
    """ A function that returns the intersection of 2 lists.

    Args:
    list1,list2 - lists

    Return:
    A new lists consisting of list1 and list2 intersection.
"""
    return sorted(list(set(list1) & set(list2)))


def list_difference(list1, list2):
    """ A function that returns the difference of 2 lists.

    Args:
    list1,list2 - lists

    Return:
    A new lists consisting of list1 and list2 difference.
"""
    return sorted(list(set(list1) ^ set(list2)))


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
    a dictionary that tells how many times each number
    (not to be confused with digit)
    and each word (not char) are in the text.
"""
#one-liner is easy, but double doing some of the job
####    return ({key: "".join([char.lower()
####                           if char not in string.punctuation
####                           and char not in string.whitespace
####                           else " "
####                           for char in txt]).split().count(key)
####             for key in "".join([char.lower()
####                                 if char not in string.punctuation
####                                 and char not in string.whitespace
####                                 else " " for char in txt]).split()})
# this will be a faster solution, in more lines....

    x = "".join([char.lower() if char not in string.punctuation
                 and char not in string.whitespace
                 else " " for char in txt]).split()
    return ({key: x.count(key) for key in x})


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
        yield start
        start = f(start)


def gimme_a_genexp(f, start, repeat=-float("inf")):
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

    return ((gimme_a_genexp(f, start, itrat)
             for itrat in itertools.count()) if repeat == -float("inf")
            else f(gimme_a_genexp(f, start, repeat-1)) if repeat > 0
            else start)
