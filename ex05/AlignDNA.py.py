#############################################################
# FILE : AlignDNA.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex4 200132014
# DESCRIPTION:DNA****
# 
#############################################################

def get_alignment_score(a, b, match = 1, mismatch = -1, gap = -2):
    """ The function compares two DNA strands
    Args:
    a,b - equal length DNA strands consisting of actg strings
    three parameters for the pointing system for
    match, mismatch and gap between the strands.

    Returns the comparing value
"""
    sm = 0 #sum
    for i in range(len(a)):
        if a[i] != b[i]:
            sm += mismatch
        else:
            if a[i] == b[i] and b[i] == "-":
                sm += gap
            else:
                sm += match
    return sm

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
####def rec_alignment(a, b, match, mismatch, gap, spaces):
####    if spaces == 0:
####        return get_aligment_score(a, b, match, mismatch, gap)
####    if match > mismatch:
####        if a[o] == b[0]:
####            return match + rec_alignment(a[1:], b[1:], match, mismatch, gap)
####        return gap + rec_alignment(a, b[1:], match, mismatch, gap-1)
####    if a[o] == b[0]:
####            return gap + rec_alignment(a, b[1:], match, mismatch, gap-1)
####        return mismatch + rec_alignment(a[1:], b[1:], match, mismatch, gap)
####
####def  get_best_alignment_score(a, b, match = 1, mismatch = -1, gap = -2):
####    if len(a) > len(b):
####        a,b=b,a
####    return rec_alignment(a, b, match, mismatch, gap, len(b)-len(a))
####def  get_best_alignment_score(a, b, match = 1, mismatch = -1, gap = -2):
####    if len(a) == 0:
####        return gap * len(b), a+"-"*len(b), b
####    if len(b) == 0:
####        return gap * len(a), a, b+"-"*len(a)
####    bheaded =  b[:-1] #b without a head, got the pun?
####    aheaded = a[:-1]
####    best = max(match, mismatch,gap)
####    if best == match and a[-1] == b[-1]:
####        result = get_best_alignment_score(aheaded, bheaded, match, mismatch, gap)
####        return result[0]+match, result[1]+a[-1], result[2]+b[-1]
####    elif best == mismatch:
####        result = get_best_alignment_score(aheaded, bheaded, match, mismatch, gap)
####        return result[0]+mismatch, result[1]+a[-1], result[2]+b[-1]
####    elif best == gap:
####        return gap * len(a)+len(b), "-"*len(b) + a, b + "-"*len(a)
####        
####    a_gap = get_best_alignment_score(a, bheaded, match, mismatch, gap)
####    a_gap = (a_gap[0] + gap, a_gap[1]+"-", a_gap[2]+b[-1])
####    b_gap = get_best_alignment_score(aheaded, b, match, mismatch, gap)
####    b_gap = (b_gap[0] + gap, b_gap[1]+a[-1], b_gap[2]+"-")
####    no_gap = get_best_alignment_score(aheaded, bheaded, match, mismatch, gap)
####    if a[-1] == b[-1]:
####        no_gap = (match + no_gap[0], no_gap[1]+a[-1], no_gap[2]+b[-1])
####    else:
####        no_gap = (mismatch + no_gap[0], no_gap[1]+a[-1], no_gap[2]+b[-1])
####    max_val = max(no_gap[0], a_gap[0], b_gap[0])
####    if max_val == no_gap[0]:
####        return no_gap
####    elif max_val == a_gap[0]:
####        return a_gap
####    return b_gap
####
####def rec_alignment(a, b, match, mismatch, gap):
####    if len(a) == 0:
####        return gap * len(b), a+"-"*len(b), b
####    if len(b) == 0:
####        return gap * len(a), a, b+"-"*len(a)
####    bheaded =  b[:-1] #b without a head, got the pun?
####    aheaded = a[:-1]
####    best = max(match, mismatch,gap)        
####    a_gap = rec_alignment(a, bheaded, match, mismatch, gap)
####    a_gap = (a_gap[0] + gap, a_gap[1]+"-", a_gap[2]+b[-1])
####    b_gap = rec_alignment(aheaded, b, match, mismatch, gap)
####    b_gap = (b_gap[0] + gap, b_gap[1]+a[-1], b_gap[2]+"-")
####    no_gap = rec_alignment(aheaded, bheaded, match, mismatch, gap)
####    if a[-1] == b[-1]:
####        no_gap = (match + no_gap[0], no_gap[1]+a[-1], no_gap[2]+b[-1])
####    else:
####        no_gap = (mismatch + no_gap[0], no_gap[1]+a[-1], no_gap[2]+b[-1])
####    max_val = max(no_gap[0], a_gap[0], b_gap[0])
####    if max_val == no_gap[0]:
####        return no_gap
####    elif max_val == a_gap[0]:
####        return a_gap
####    return b_gap
####
####import time
####a="agtggttg"
####b="cgtgcgtgt"
####match = 100
####mismatch =10
####gap=1
####start = time.time()
####x = get_best_alignment_score(a, b, match , mismatch, gap)
####end = time.time()
####print (end - start,"time. x=", x)
####
####start = time.time()
####x = rec_alignment(a, b, match, mismatch, gap)
####end = time.time()
####print (end - start,"time. x=", x)
