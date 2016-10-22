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
import operator as op
from pprint import pprint

from bset import bset,pset,recount_board
from bset import prepare_board as replay_board

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

def diff_str(intro,exp,act):
    return "\n".join([intro+":",
                      "expected: "+str(exp),
                      "actual:   "+str(act)])

def check_empty_board(board,width,height,tname):
    if not isinstance(board, list):
        res_code(tname, "wrong", diff_str("Wrong type",list,type(board)))
        return False
    if len(board)!=height:
        res_code(tname, "wrong", diff_str("Wrong height",height,len(board)))
        return False
    exp_row = [None]*width
    id_set = {id(row) for row in board}
    if len(id_set)!=height:
        res_code(tname, "wrong", diff_str("Number of different row lists wrong",height,len(id_set)))
        return False    
    for i,row in enumerate(board):
        if row != exp_row:
            res_code(tname, "wrong", diff_str("Row "+str(i)+" wrong",exp_row,row))
            return False
    return True
        
def check_boards_equal(exp,act,tname):
    if len(exp)!=len(act):
        res_code(tname, "wrong", diff_str("Different board heights",len(exp),len(act)))
        return False
    id_set = {id(row) for row in act}
    if len(id_set)!=len(act):
        res_code(tname, "wrong", diff_str("Number of different row lists wrong",len(act),len(id_set)))
        return False    
    for i,(erow,arow) in enumerate(zip(exp,act)):
        if erow != arow:
            res_code(tname, "wrong", diff_str("Row "+str(i)+" different",erow,arow))
            return False
    return True

def check_board_consistency(board,row_ids,cell_ids,tname):
    d = {} #list,count
    for row in board:
        for cell in row:
            if cell:
                if cell[0] in d:
                    d[cell[0]][1]+=1
                    if cell[2] is not d[cell[0]][0]:
                        res_code(tname, "badboard", "Ship "+cell[0]+" has different list ids")
                        return False                    
                else:
                    d[cell[0]] = [cell[2],1]
    for k,v in d.items():
        if v[0][0] != v[1]:
            res_code(tname, "badboard", "Ship "+k+" has wrong count")
            return False                    
    if len({id(d[k][0]) for k in d}) != len(d):
           res_code(tname, "badboard", "Repeated length list ids on board")
           return False                    
    if row_ids != [id(row) for row in board]:
           res_code(tname, "badboard", "Row list ids changed during execution")
           return False                    
    for row,idlist, in zip(board,cell_ids):
        for cell,cid in zip(row,idlist):
            if(cell and cid and (id(cell) != cid)):
                res_code(tname, "badboard", "Cell tuples replaced during execution")
                return False
    return True 

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

def import_runner_function(modulename, fname, args=[], kwargs={},tname=''):
    input = kwargs.pop("_input",[])
    retval,res = import_runner(modulename, fname, args, kwargs)
    if retval:
        return (retval,res)
    return (None,list(map(res,input)))

def import_runner_chk_board(modulename, fname, args=[], kwargs={},tname=''):
    #print(modulename, fname, args, kwargs,tname)
    replay = kwargs.pop("_replay",[])
    recount = kwargs.pop("_recount",False)
    #print(replay)
    board = args[0] if args else kwargs["board"]
    row_ids = [id(row) for row in board]
    cell_ids = [[id(cell) if cell else None for cell in row] for row in board]
    board_cp = copy.deepcopy(board)
    if replay:
        replay_board(board_cp,replay)
        if recount:
            recount_board(board_cp)
    retval,res = import_runner(modulename, fname, args, kwargs, check_input=False)
    if retval:
        res_code(tname, retval, res)
        return ("skip",res)
    if not (check_boards_equal(board_cp,board,tname)):
        return ("skip", board)
    if not (check_board_consistency(board,row_ids,cell_ids,tname)):
        return ("skip", board)
    return (None,res)

def test_battleship(modulename="battleship",timeout=3):
    for name,testlist in bset.items():
        test_set(name,testlist,comparemethod="new_board")
    for name,testlist in pset.items():
        test_set(name,testlist,runner=import_runner_chk_board)
    #for name,testlist in fset.items():
    #    test_set(name,testlist,runner=import_runner_function)

def test_set(name, testlist, modulename="battleship",timeout=3,
             runner=import_runner, comparemethod=None):
    correct = 0
    #answers = []
    for i,(fname,args,kwargs,ans) in enumerate(testlist):
        tname = name + "_" + str(i)
        try:
            res, inner = mp_test(runner,[modulename,fname,args,kwargs],{"tname":tname}, timeout=timeout)
            #ans=retval
            #answers.append((fname,args,kwargs,ans))
            #continue
            if res:
                res_code(tname, res, retval)
                continue
            lres,retval = inner
            if lres=="skip":
                continue
            if lres:
                res_code(tname, lres, retval)
                continue
            if ans and comparemethod=="new_board":
                if check_empty_board(retval,ans[0],ans[1],tname):
                    correct+=1
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
        except FakeException as e:
            res_code(tname, "testingFailed", e)
            continue

    #print (name+'=',answers)
    res_code(name, str(correct))

if __name__=="__main__":
    if len(argv)>1:
        test_battleship(argv[1])
    else:
        test_battleship()
