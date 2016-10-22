#############################################################
# FILE : AlignDNA.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex4 200132014
# DESCRIPTION:DNA****
# 
#############################################################

def get_aligment_score(a, b, match = 1, mismatch = -1, gap = -2):
    """ The function compares two DNA strands
    Args:
    a,b - equal length DNA strands consisting of actg strings
    three parameters for the pointing system for
    match, mismatch and gap between the strands.

    Returns the comparing value
    """
    sm=0
    for i in range(len(a)):
        if a[i] != b[i]:
            sm += mismatch
        else:
            if a[i] == b[i] and b[i] == "-":
                sm += gap
            else:
                sm += match
    return sm
##def rec_alignment(a, b, match, mismatch, gap, spaces):
##    if spaces == 0:
##        return get_aligment_score(a, b, match, mismatch, gap)
##    if match > mismatch:
##        if a[o] == b[0]:
##            return match + rec_alignment(a[1:], b[1:], match, mismatch, gap)
##        return gap + rec_alignment(a, b[1:], match, mismatch, gap-1)
##    if a[o] == b[0]:
##            return gap + rec_alignment(a, b[1:], match, mismatch, gap-1)
##        return mismatch + rec_alignment(a[1:], b[1:], match, mismatch, gap)
##
##def  get_best_alignment_score(a, b, match = 1, mismatch = -1, gap = -2):
##    if len(a) > len(b):
##        a,b=b,a
##    return rec_alignment(a, b, match, mismatch, gap, len(b)-len(a))
##def get_best_alignment_score(a, b, match = 1, mismatch = -1, gap = -2):
##    best = max(match, mismatch, gap)
##    if gap*2 >= best:
##        return gap * (len(a)+len(b)), "-"*len(b) + a, b + "-"*len(a)
##    else:
##        return  rec_alignment(best, a, b, match, mismatch, gap)
##        #write what to do with best mismatch and gap
##
##def rec_alignment(a, b, match, mismatch, gap, best): #it never puts mismatch!! should check
##    if len(a) == 0:
##        return gap * len(b), a+"-"*len(b), b
##    if len(b) == 0:
##        return gap * len(a), a, b+"-"*len(a)
##    bheaded =  b[:-1] #b without a head, got the pun?
##    aheaded = a[:-1]
##    if a[-1] == b[-1]:
##        result = rec_alignment(aheaded, bheaded,
##                               match, mismatch, gap, best)
##        print( """a = {0} b = {1}, aheaded {2}, bheaded {3}
##no gap answer {4} """.format(a,b,aheaded,bheaded,result))
##        return result[0]+best, result[1]+a[-1], result[2]+b[-1]
##    
##
##    a_gap = rec_alignment(a, bheaded, match, mismatch, gap, best)
##    a_gap = (a_gap[0] + gap, a_gap[1]+"-", a_gap[2]+b[-1])
##    print( """a = {0} b = {1}, aheaded {2}, bheaded {3}
##a_gap answer {4} """.format(a,b,aheaded,bheaded,a_gap))
##    print()
##    b_gap = rec_alignment(aheaded, b, match, mismatch, gap, best)
##    b_gap = (b_gap[0] + gap, b_gap[1]+a[-1], b_gap[2]+"-")
##    print( """a = {0} b = {1}, aheaded {2}, bheaded {3}
##b_gap answer {4} """.format(a,b,aheaded,bheaded,b_gap))
##    print()
##    if a_gap[0] > b_gap[0]:
##        return a_gap
##    return b_gap
##
##def rec_alignment(best, a, b, match = 1, mismatch = -1, gap = -2):
##    if len(a) == 0:
##        return gap * len(b), a+"-"*len(b), b
##    if len(b) == 0:
##        return gap * len(a), a, b+"-"*len(a)
##    bheaded =  b[:-1] #b without a head, got the pun?
##    aheaded = a[:-1]
##    
##    #If you have the best case right now,
##    #choose it and check the rest of the string.
##    if best == match and a[-1] == b[-1]:
##        result = rec_alignment(best, aheaded, bheaded, match, mismatch, gap)
##        return result[0]+match, result[1]+a[-1], result[2]+b[-1]
##    elif best == mismatch and a[-1] != b[-1]:
##        result = rec_alignment(best, aheaded, bheaded, match, mismatch, gap)
##        return result[0]+mismatch, result[1]+a[-1], result[2]+b[-1]
##        #write what to do with best worst case, what can I know
##    
##    #check where is best to put -    
##    a_gap = rec_alignment(best, a, bheaded, match, mismatch, gap)
##    a_gap = (a_gap[0] + gap, a_gap[1]+"-", a_gap[2]+b[-1])
##    b_gap = rec_alignment(best, aheaded, b, match, mismatch, gap)
##    b_gap = (b_gap[0] + gap, b_gap[1]+a[-1], b_gap[2]+"-")
##
##    #check if without "-" it is better
##    no_gap = rec_alignment(best, aheaded, bheaded, match, mismatch, gap)
##    if a[-1] == b[-1]:
##        no_gap = (match + no_gap[0], no_gap[1]+a[-1], no_gap[2]+b[-1])
##    else:
##        no_gap = (mismatch + no_gap[0], no_gap[1]+a[-1], no_gap[2]+b[-1])
##    max_val = max(no_gap[0], a_gap[0], b_gap[0])
##    if max_val == no_gap[0]:
##        return no_gap
##    elif max_val == a_gap[0]:
##        return a_gap
##    return b_gap

def rec_alignment(best, a, b, match = 1, mismatch = -1, gap = -2):
    if len(a) == 0:
        return gap * len(b), a+"-"*len(b), b
    if len(b) == 0:
        return gap * len(a), a, b+"-"*len(a)
    bheaded =  b[:-1] #b without a head, got the pun?
    aheaded = a[:-1]
    
    #If you have the best case right now,
    #choose it and check the rest of the string.
    if best == match and a[-1] == b[-1]:
        result = rec_alignment(best, aheaded, bheaded, match, mismatch, gap)
        return result[0]+match, result[1]+a[-1], result[2]+b[-1]
    elif best == mismatch and a[-1] != b[-1]:
        result = rec_alignment(best, aheaded, bheaded, match, mismatch, gap)
        return result[0]+mismatch, result[1]+a[-1], result[2]+b[-1]
        #write what to do with best worst case, what can I know
    
    #check where is best to put -    
    a_gap = rec_alignment(best, a, bheaded, match, mismatch, gap)
    a_gap = (a_gap[0] + gap, a_gap[1]+"-", a_gap[2]+b[-1])
    b_gap = rec_alignment(best, aheaded, b, match, mismatch, gap)
    b_gap = (b_gap[0] + gap, b_gap[1]+a[-1], b_gap[2]+"-")

    #check if without "-" it is better
    no_gap = rec_alignment(best, aheaded, bheaded, match, mismatch, gap)
    if a[-1] == b[-1]:
        no_gap = (match + no_gap[0], no_gap[1]+a[-1], no_gap[2]+b[-1])
    else:
        no_gap = (mismatch + no_gap[0], no_gap[1]+a[-1], no_gap[2]+b[-1])
    max_val = max(no_gap[0], a_gap[0], b_gap[0])
    if max_val == no_gap[0]:
        return no_gap
    elif max_val == a_gap[0]:
        return a_gap
    return b_gap

def memorize(f):
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
    def g(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return g

def get_best_alignment_score(a, b, match = 1, mismatch = -1, gap = -2):
    best = max(match, mismatch, gap)
    global rec_alignment
    rec_alignment = memorize(rec_alignment)
    if gap*2 >= best:
        return gap * (len(a)+len(b)), "-"*len(b) + a, b + "-"*len(a)
    else:
        return  rec_alignment(best, a, b, match, mismatch, gap)

def new (a, b, match = 1, mismatch = -1, gap = -2):
    best = max(match, mismatch, gap)
    if gap*2 >= best:
        return gap * (len(a)+len(b)), "-"*len(b) + a, b + "-"*len(a)        
    else:
        return  rec_alignment(best, a, b, match, mismatch, gap)
    
def new_in(best, a, b, match = 1, mismatch = -1, gap = -2): 

    if len(a) == 0:
        return gap * len(b), a+"-"*len(b), b
    if len(b) == 0:
        return gap * len(a), a, b+"-"*len(a)
    bheaded =  b[:-1] #b without a head, got the pun?
    aheaded = a[:-1]
    not_best = match + mismatch - best
    
    #If you have the best case right now,
    #choose it and check the rest of the string.
    if best == match and a[-1] == b[-1]:
        result = rec_alignment(best, aheaded, bheaded, match, mismatch, gap)
        return result[0]+match, result[1]+a[-1], result[2]+b[-1]
    elif best == mismatch and a[-1] != b[-1]:
        result = rec_alignment(best, aheaded, bheaded, match, mismatch, gap)
        return result[0]+mismatch, result[1]+a[-1], result[2]+b[-1]
        #write what to do with best worst case, what can I know
    
    #check what happens if there is "-" at the end of strand a    
    a_gap = rec_alignment(best, a, bheaded, match, mismatch, gap)
    a_gap = (a_gap[0] + gap, a_gap[1]+"-", a_gap[2]+b[-1])

    
    shorter = (min(len(a), len(bheaded)))
    longer = len(a) + len(bheaded) - shorter
    worst_a_gap = (not_best)*shorter + (longer-shorter)*gap
    best_a_gap = best*shorter + (longer-shorter)*gap

    #check if the result is best possible
    if a_gap == best_gap:
        if len(a) > len(b): # cgtc- cg--a  or  cgtcc- cg-c-t
            result =[a_gap[0] - gap, a, ""]
            letter_b = 0
            letter_a = 0
            while letter_a < len(b):
                if (a[letter_a] == b[letter_b] and match == best or
                    a[letter_a] != b[letter_b] and mismatch == best):
                    result[1] += a[letter_a]
                    letter_a += 1
                    letter_b += 1
                else:
                    a_gap[2] += "-"
                    letter_b += 1
                if letter_b == len(b)-1:
                    if a[letter_a] != b[letter_b]:#make sure it is right and working
                        if gap*2 > not_best:#maybe it can be before the while?
                            return a_gap
                        else:
                            result[0] = result[0] + not_best - gap
                            result[1] += a[letter_a]
                    if a[letter_a] == b[letter_b]#what to do than? what to do if it finishes before the end of b and it is all right
                return result
        elif len(a) == len(b): # finish it: cga- c-at
            pass
        else: #make sure I am right
            return a_gap
    #check if the result is the worst possible (the best of bad)
    if a_gap == worst_a_gap:
        pass # what can I know from that?
    b_gap = rec_alignment(best, aheaded, b, match, mismatch, gap)
    b_gap = (b_gap[0] + gap, b_gap[1]+a[-1], b_gap[2]+"-")

    #If with a gap in a and in b is the worst case,
    #don't bother doing another recursion.
    if worst_a_gap == a_gap[0] and worst_b_gap == b_gap[0]:
        if len(a) > len(b):
            return a_gap
        elif len(a) < len(b):
            return b_gap
        else:
            return a_gap[0]- gap, b_gap[1], a_gap[2]
        
    #check if without "-" it is better
    if (not_best > gap*2):
        no_gap = rec_alignment(best, aheaded, bheaded, match, mismatch, gap)
        no_gap = (not_best + no_gap[0], no_gap[1] + a[-1], no_gap[2] + b[-1])
    else:
        no_gap = (-float("inf"), "", "")
    max_val = max(no_gap[0], a_gap[0], b_gap[0])
    if max_val == no_gap[0]:
        return no_gap
    elif max_val == a_gap[0]:
        return a_gap
    return b_gap

def memoize(f):

    cache = {}
    def g(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return g
import inspect
def timed(f):
    def g(*args):
        first = False
##        try:
##            nonlocal start 
##        except NameError:
        if "start" not in inspect.currentframe().f_code.co_freevars:
            start = time.time()
            first = True
        x = f(*args)
        if first:
            return time.time() - start, x
        return x
    return g
def func(x,y):
    if y > 0:
        return 1
    return func(x,y-1)
import random
import time
a=""
b=""
letters= ["a","g","c","t"]
for i in range(155):
    a += letters[random.randint(0, 3)]
    b += letters[random.randint(0, 3)]
    

##a="gcgcgtatgaaa"
##b="cacgtgattgag"
match = random.randint(-2, 2)
mismatch = random.randint(-2, 2)
gap = random.randint(-2, 2)
print ("a {0} b {1} match {2} mismatch {3} gap {4}".format(
    a,b,match,mismatch,gap))
##start = time.time()
##x = get_best_alignment_score(a, b, match , mismatch, gap)
##end = time.time()
##print (end - start,"time. x=", x)

##start = time.time()
##x = get_best_alignment_score(a, b, match, mismatch, gap)
##end = time.time()
##print (end - start,"time. x=", x)

##start = time.time()
##rec_alignment = memoize(rec_alignment)
get_best_alignment_score = timed(get_best_alignment_score)
new = timed(memoize(new))
x = get_best_alignment_score(a, b, match, mismatch, gap)
y = new(a, b, match, mismatch, gap)
print( "x {0} y{1}".format(x,y))
if y[0] < x[0]:
    print("success, it is faster")
if x[1][0] != y[1][0]:
    print ("oh oh they are not the same")
##end = time.time()

