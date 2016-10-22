#############################################################
# FILE : NonRecursiveMystery.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex5 200132014
# DESCRIPTION:
#   An arithemtic function that:
#   gets a number and returns
#   the sum of its fractions, not self include, includes 1.
#############################################################


def mystery_computation(number):
    """An arithemtic function that:
    gets a number and
    returns the sum of its fractions, not self include, includes 1.
    """
    sm_modu = 0  # sum of modulos
    for i in range(1, number):
        if number % i == 0:
            sm_modu += i
    return sm_modu
