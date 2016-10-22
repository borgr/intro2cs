#############################################################
# FILE : AlignDNA.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex5 200132014
# DESCRIPTION: DNA comparison functions
#############################################################
empty = "-" # the sign of and empty place in the DNA strand

def get_alignment_score(dna, dnb, match=1, mismatch=-1, gap=-2):
    """ The function compares two DNA strands
    Args:
    dna, dnb - equal length DNA strands consisting of actg strings
    three parameters for the pointing system for
    match, mismatch and gap between the strands.

    Returns the comparing value
"""
    sm = 0  # sum
    for indx in range(len(dna)):
        if dna[indx] == empty or dnb[indx] == empty:
            sm += gap
        elif dna[indx] != dnb[indx]:
            sm += mismatch
        else:
            if dna[indx] == dnb[indx] and dnb[indx] == empty:
                sm += gap
            else:
                sm += match
    return sm

# These operands are about the min length for recursion overstack error
# to occur for both operands too long or for just one.
# the function does not rely onspecific ones, so they canbe changed
# if it is wished.

long = 100
one_long = 80
jumps = 20


def memorize(function):
    """ This function memorizes the answers given function results
    thus ending with noneed to re run the code each time.

    Arg:
    function to be memorizes while running

    Return:
    The new function made, that know to memorize itself.

    Note:
    the function will only work if assigned to the name given
    when the regular function was defined.
    (func = memorize(func) <<< good
    f = memorize(func) <<< will not get expected result)    
"""

    cache = {}
    #the convention is f and g. so function and gunction...
    def gunction(*args):
        """ a function that gets arguments,
        adds the function result to the cache
        and returns the function's result"""
        if args not in cache:
            cache[args] = function(*args)
        return cache[args]
    return gunction
    
    
def inner(best, dna, dnb, match, mismatch, gap):
    """ this function finds the best alignment of 2 dna strands

    Args:
    best - the best of match mismatch and gap,
    dna, dnb - two dna strands, each a string
    match, mismatch, gap - the value each comparison worth accordingly.

    Returns:
    a tuple with the best value and the new strings
    (with gaps when needed)
    """
    end = -1  # an argument for the end of the list or tuple
    frst = 0  # an argument for the first object in a list or tuple
    scnd = 1  # an argument for the second object in a list or tuple
    #stop case, when dna(a) or dnb(b) are empty
    if not len(dna):
        return gap * len(dnb), dna + empty*len(dnb), dnb
    if not len(dnb):
        return gap * len(dna), dna, dnb + empty*len(dna)
    bheaded = dnb[:end]  # b without a head, got the pun?
    aheaded = dna[:end]
    not_best = match + mismatch - best
    
    #If you have the best case right now,
    #choose it and check the rest of the string.
    if best == match and dna[end] == dnb[end]:
        result = inner(best, aheaded, bheaded, match, mismatch, gap)
        return (result[frst]+match, result[scnd]+dna[end],
                result[end]+dnb[end])
    elif best == mismatch and dna[end] != dnb[end]:
        result = inner(best, aheaded, bheaded, match, mismatch, gap)
        return result[frst]+mismatch, result[scnd]+dna[end], result[end]+dnb[end]
        #write what to do with best worst case, what can I know
    
    # check what happens if there is "-" at the end of strand a    
    a_gap = inner(best, dna, bheaded, match, mismatch, gap)
    a_gap = (a_gap[frst] + gap, a_gap[scnd]+empty, a_gap[end]+dnb[end])
    
    shorter = (min(len(dna), len(bheaded)))
    longer = len(dna) + len(bheaded) - shorter
    worst_a_gap = (not_best)*shorter + (longer-shorter)*gap

    #check if if there is "-" at the end of strand b
    b_gap = inner(best, aheaded, dnb, match, mismatch, gap)
    b_gap = (b_gap[frst] + gap, b_gap[scnd]+dna[end], b_gap[end]+empty)
    shorter = (min(len(aheaded), len(dnb)))
    longer = len(bheaded) + len(dnb) - shorter
    worst_b_gap = (not_best)*shorter + (longer-shorter)*gap

    #If worst case scenario is being held with both 
    #a and b having a gap, don't bother doing another recursion.
    if worst_a_gap == a_gap[frst] and worst_b_gap == b_gap[frst]:
        if len(dna) < len(dnb):
            return a_gap
        elif len(dna) > len(dnb):
            return b_gap
        else:
            return a_gap[frst] - gap, b_gap[scnd], a_gap[end]
        
    #check if without "-" might be better
    if (not_best > gap*2): #it is 2 because each gap empties a space
        no_gap = inner(best, aheaded, bheaded, match, mismatch, gap)
        no_gap = (not_best + no_gap[frst],
                  no_gap[scnd] + dna[end], no_gap[end] + dnb[end])
    else:
        no_gap = (-float("inf"), "", "")
    max_val = max(no_gap[frst], a_gap[frst], b_gap[frst])
    if max_val == no_gap[frst]:
        return no_gap
    elif max_val == a_gap[frst]:
        return a_gap
    return b_gap
        
inner = memorize(inner)


def get_best_alignment_score(dna, dnb, match=1, mismatch=-1, gap=-2):
    """ The function compares two dna strands

    Args:
    dna,dnb - two dna strands consistings of strings without gaps
    match, mismatch, gap - integer values for
    comparison of the apropriate cases.
    
"""
    global long
    global one_long
    global jump
    best = max(match, mismatch, gap)
    if gap*2 >= best:
        return (gap * (len(dna)+len(dnb)),
                empty*len(dnb) + dna, dnb + empty*len(dna))

    #if recursion error is forseen save options to lighten the recursion
    #it runs the tree in parts from the end, avoiding any overflow.
    else:
        if ((len(dna) > long or len(dnb) > long) or
             len(dna)+len(dnb) > one_long):
            runs = max(len(dna), len(dnb))
            tmp_b = ""
            while long < runs:
                tmp_a = dna[:long]
                inner(best, tmp_a, tmp_b, match, mismatch, gap)
                tmp_b = dnb[:long]
                inner(best, tmp_a, tmp_b, match, mismatch, gap)
                long += jumps

        return inner(best, dna, dnb, match, mismatch, gap)
