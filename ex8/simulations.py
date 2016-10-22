#!/usr/bin/env python3

import sys
import random
from hash_table import next_prime,hash_table
from hash_functions import hash_functions
import time
import timeit
import string
import hashlib

def id_generator(chars=string.ascii_uppercase + string.digits, len_range=10, len_min=10):   
    """ generates random strings """
    while True:
        size = random.randrange(len_range)+len_min
        yield ''.join(random.choice(chars) for x in range(size))

def get_load_stats ( table ):
    """
    Returns the maximal, average, variacnce and normalized
    variance of the number of collisions in the hash table.
    """
    load = table.get_load()
    total = sum(load)
    max_load = max(load)
    mean_load = total/len(load)
    variance_load = sum((mean_load - value) ** 2 for value in load) / len(load)
    normalized_variance_load = sum((mean_load - value) ** 2 for value in load) / len(load)/total/total
    
    return max_load, mean_load, variance_load, normalized_variance_load

def simulation(id_list, times = 10 , mod = 10**3, func = hash):
    """ Performs hashing t times for M slots using func as the hash function.
    Returns the load tuple (see get_load_stats) and the time  in seconds
    for insertion of all the id_list to the table.
    """
    loads =[]
    timer = []
    for i in range(times):
        table = hash_table(mod, func = func) # restart hash table
        t0= time.perf_counter()
        for id in id_list:
            table.insert(id,id)
        t1= time.perf_counter()
        timer.append(t1 - t0)
        loads.append(get_load_stats(table)) # add load to loads
    return loads, timer

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Run Simulations")
    parser.add_argument('--repeats', '-r', type=int, default=1)
    parser.add_argument('--minhashsize', '-m', type=int, default=10**3)
    parser.add_argument('--idlistsize', '-n', type=int, default=500)
    parser.add_argument('--toprime', '-p', action='store_true')
    parser.add_argument('--function', '-f', type=int, default=-1)
    parser.add_argument('--sourcefile', '-s', type=str, default=None)
    parser.add_argument('--csvoutput', '-c', action='store_true')
    args = parser.parse_args()

    " user arguments"
    if args.sourcefile is None:
        gen = id_generator()
        id_list = [None]*args.idlistsize
        for i in range(len(id_list)):
            id_list[i]=next(gen)
    elif args.sourcefile == '-':
        id_list = [line for line in sys.stdin]
    else:
        with open(args.sourcefile) as f:
            id_list = [line for line in f]

    " start simulation"
    repeats = args.repeats
    mod = args.minhashsize
    if args.toprime:
        mod = next_prime(mod)
    func = hash_functions[0](args.minhashsize) #hash_functions[args.function](args.minhashsize) if 0<=args.function<len(hash_functions) else hash
    res,timer = simulation(id_list, times=repeats, mod=mod, func=func)

    max_collisions = sum([x[0] for x in res])/repeats
    mean_collisions = sum([x[1] for x in res])/repeats
    var_collisions = sum([x[2] for x in res])/repeats
    nvar_collisions = sum([x[3] for x in res])/repeats


    if args.csvoutput:
        print(len(id_list),mod,args.function,min(timer),max_collisions,mean_collisions,var_collisions,nvar_collisions,sep=',')
    else:
        print ("No. of elements:",len(id_list))
        print("Hash table size:",mod)
        print("Hash function number:",args.function)
        print("Minimum time: %f seconds" %(min(timer)))
        print("Maximum load:",max_collisions)
        print("Average load:",mean_collisions)
        print("Variance of load:",var_collisions)
        print("Normalized variance of load:",nvar_collisions)

if __name__=='__main__':
    main()
