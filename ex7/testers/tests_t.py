#!/usr/bin/env python3

from autotest import sp_test,mp_test,mp_test2,res_code,long_sequence_compare
import autotest as at
from sys import argv
from os import chdir
import sys
from importlib import import_module
from numbers import Number
from math import isnan
from collections import Sequence
import copy
import operator as op
from pprint import pprint
from types import GeneratorType
from itertools import islice
import re

from tset import tset,jset

class FakeException(Exception):
    pass

def diff_str(intro,exp,act):
    return "\n".join([intro+":",
                      "expected: "+str(exp),
                      "actual:   "+str(act)])

def import_runner(modulename, fname, args=[], kwargs={}, check_input=True,tname=''):
    module = import_module(modulename)
    func = getattr(module, fname)
    if check_input:
        args2 = copy.deepcopy(args)
        kwargs2 = copy.deepcopy(kwargs)
    res = func(*args, **kwargs)
    if check_input:
        if not (args==args2 and kwargs==kwargs2): #good enough for now
            return ("modified", res)
    return (None,res)

def import_runner_class(modulename, fname, args=[], kwargs={},tname=''):
    outtest = kwargs.pop("_outputtest",None)
    outargs = kwargs.pop("_outputargs",[])
    retval,res = import_runner(modulename, fname, args, kwargs)
    if retval:
        return(retval,res)
    if outtest:
        res = getattr(res, outtest)(*outargs)
    return (None,res)

def import_runner_map(modulename, fname, args=[], kwargs={},tname=''):
    outtest = kwargs.pop("_outputtest",None)
    outargs = kwargs.pop("_outputargs",[])
    reslist = [import_runner(modulename, fname, argset, kwargs) for argset in args]
    results = []
    for retval,res in reslist:
        if retval:
            return(retval,res)
        results.append(getattr(res, outtest)(*outargs) if outtest else res)
    return (None,results)

def test_tweet(modulename="tweet",timeout=3):
    for name,testlist in tset.items():
        test_set(name,testlist,modulename,timeout,runner=import_runner_class)
    for name,testlist in jset.items():
        test_set(name,testlist,modulename,timeout,runner=import_runner_map)
    #for name,testlist in lset.items():
    #    test_set(name,testlist,modulename,timeout=10)
    #for name,testlist in gset.items():
    #    test_set(name,testlist,modulename,timeout,runner=import_runner_generator)
    #for name,testlist in rset.items():
    #
    #test_set(name,testlist,modulename,timeout,runner=import_runner_rand)

def test_set(name, testlist, modulename="tweet",timeout=3,
             runner=import_runner, comparemethod=None):
    correct = 0
    #answers = []
    for i,(fname,args,kwargs,ans) in enumerate(testlist):
        tname = name + "_" + str(i)
        try:
            res, retval = mp_test2(runner,[modulename,fname,args,kwargs],{"tname":tname}, timeout=timeout)
            #ans=retval
            #answers.append((fname,args,kwargs,ans))
            #continue
            if res=="skip":
                continue
            if res:
                res_code(tname, res, retval)
                continue
            if retval==ans: # correct result    #with no floats
                correct+=1
                continue
            else:
                #if isinstance(ans, Sequence):
                #    long_sequence_compare(tname, ans, retval, contextpreview=3)
                #else:
                res_code(tname, "wrong",diff_str("Wrong result",ans,retval))
                continue
        except at.Error as e:
            res_code(tname, e.code, e.message)
        except Exception as e:
            res_code(tname, "testingFailed", e)
            continue

    #print (name+'=',answers)
    res_code(name, str(correct))

if __name__=="__main__":
    if len(argv)>1:
        #test_mystery(argv[1])
        test_tweet()
    else:
        test_tweet()
