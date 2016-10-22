#!/usr/bin/env python3

from autotest import sp_test,mp_test,res_code,long_sequence_compare
from sys import argv
from os import chdir
import sys
from importlib import import_module
from numbers import Number
from math import isnan
from collections import Sequence
import copy

from rtset import rtset,eset,fset

class FakeException(Exception):
    pass

def allclose(act, exp, rtol=1.e-5, atol=1.e-5, history=None):
    if id(act)==id(exp):
        return True
    if isinstance(exp,int):
        return exp==act
    elif isinstance(exp,Number):
        if exp==act or isnan(exp) and isnan(act):
            return True
        return abs(act-exp) <= atol + rtol * abs(exp) #based on numpy allclose
    elif isinstance(exp,(list,tuple)): #python recursive '==' doesn't work any better than this
        if type(exp) != type(act) or len(exp) != len(act):
            return False
        for l_act,l_exp in zip(act,exp):
            if not allclose(l_act,l_exp):
                return False
        return True
    else:
        return exp==act

def import_runner(modulename, fname, args=[], kwargs={}):
    module = import_module(modulename)
    func = getattr(module, fname)
    args2 = copy.deepcopy(args)
    kwargs2 = copy.deepcopy(kwargs)
    res = func(*args, **kwargs)
    if not (args==args2 and kwargs==kwargs2): #good enough for now
        return ("modified", res)
    return (None,res)

def import_runner_function(modulename, fname, args=[], kwargs={}):
    input = kwargs.pop("_input",[])
    retval,res = import_runner(modulename, fname, args, kwargs)
    if retval:
        return None
    return (None,list(map(res,input)))

def test_ex4(modulename="ex4",timeout=3, rtol=1.e-5, atol=1.e-5):
    for name,testlist in rtset.items():
        test_set(name,testlist)
    for name,testlist in eset.items():
        test_set(name,testlist,geteps=True)
    for name,testlist in fset.items():
        test_set(name,testlist,runner=import_runner_function)

def test_set(name, testlist, modulename="ex4",timeout=3, rtol=1.e-5, atol=1.e-5,
             geteps=False, runner=import_runner):
    correct = 0
    #answers = []
    for i,(fname,args,kwargs,ans) in enumerate(testlist):
        tname = name + "_" + str(i)
        try:
            res, (lres,retval) = mp_test(runner,[modulename,fname,args,kwargs], timeout=timeout)
            #ans=retval
            #answers.append((fname,args,kwargs,ans))
            #continue
            if res:
                res_code(tname, res, retval)
                continue
            if lres:
                res_code(tname, lres, retval)
                continue
            #if retval==ans: # correct result    #with no floats
            if geteps:
                atol += kwargs["epsilon"] if "epsilon" in kwargs else 1E-5
            if allclose(ans, retval, rtol=rtol, atol=atol): # correct result   #deep float compare?
                correct+=1
                continue
            else:
                if isinstance(ans, Sequence):
                    long_sequence_compare(tname, ans, retval, contextpreview=3)
                else:
                    res_code(tname, "wrong", "\n".join(
                        ["Wrong result:",
                         "expected: "+str(ans),
                         "actual:   "+str(retval)]))
                continue
        except Exception as e:
            res_code(tname, "testingFailed", e)
            continue

    #print (name+'=',answers)
    res_code(name, str(correct))

if __name__=="__main__":
    if len(argv)>1:
        test_ex4(argv[1])
    else:
        test_ex4()
