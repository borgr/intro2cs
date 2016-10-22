#############################################################
# FILE : ex4.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex4 200132014
# DESCRIPTION: functions for post retirement
# 
#############################################################


def variable_pension(salary, save, growth_rates):
    """ calculate retirement fund assuming variable_pension

    A function that calculates the value of a retirement fund in each year
    based on the worker salary, savings,  and a list of growthRates values.
    Number of working years is as the length of growthRats

    Args:
    - salary: the amount of money you earn each year, a non negative float.
    - save: the percent of your salary to save in the investment account
    each working year -  a non negative float between 0 and 100
    - growth_rates: the annual percent increase/decrease in your investment
    account - a float larger than or equal to -100

    return: a list whose values are the size of your retirement account at
    the end of each year.

    In case of bad input: values are out of range
    returns None

    You can assume that the types of the input arguments are correct. """
    perc = 0.01  # percent
    if len(growth_rates) > 0 and growth_rates[0] < -100:
        return
    if salary >= 0 and save >= 0 and save < 101 and len(growth_rates) >= 1:
        rtrn = [salary*save*perc]
        for ind in range(len(growth_rates)-1):
            if growth_rates[ind+1] < -100:
                return
            rtrn.append(rtrn[ind]*(1 + growth_rates[ind+1]*perc) +
                        salary*save*perc)
    elif len(growth_rates) == 0:
        rtrn = []
    else:
        return
    return rtrn

def live_like_a_king(salary, save, pre_retire_growth_rates,
                     post_retire_growth_rates, epsilon):
   
    """ Find the maximal expenses you may expend during your lifetime  

    A function that calculates what is the maximal annual expenses you may
    expend each year and not enter into debts
    You may Calculate it using binary search or using arithmetics
    Specify in your README in which method you've implemnted the function

    Args:  
    -salary: the amount of money you make each year-a non negative float.
    -save: the percent of your salary to save in the investment account
    each working year -  a non negative float between 0 and 100
    -pre_retire_growth_rates: a list of annual growth percentages in your
    investment account - a list of floats larger than or equal to -100.
    -post_retire_growth_rates: a list of annual growth percentages
    on investments while you are retired. a list of floats larger
    than or equal to -100. In case of empty list return None
    - epsilon: an upper bound on the money must remain in the account
    on the last year of retirement. A float larger than 0

    Returns the maximal expenses value you found (such that the amount of
    money left in your account will be positive but smaller than epsilon)

    In case of bad input: values are out of range returns None

    You can assume that the types of the input arguments are correct."""
    perc = 0.01  # percent
    
    #check input
    if not post_retire_growth_rates or epsilon <= 0:
        return
    product = variable_pension(salary, save, pre_retire_growth_rates)
    if product is None:
        return
    if len(product) == 0:
        return 0
    else:
        product = product[-1]
    denominator = 0
    for ind in post_retire_growth_rates:
        if ind < -100:
            return

    #calculate
    for ind in post_retire_growth_rates:
        product = product*(1 + ind*perc)
        denominator = denominator*(1 + ind*perc) + 1
        
    return product/denominator

def bubble_sort_2nd_value(tuple_list):
    """sort a list of tuples using bubble sort algorithm

    Args:
    tuples_list - a list of tuples, where each tuple is composed of a string
    value and a float value - ('house_1',103.4)

    Return: a NEW list that is sorted by the 2nd value of the tuple,
    the numerical one. The sorting direction should be from the lowest to the
    largest. sort should be stable (if values are equal, use original order)

    You can assume that the input is correct."""
    ordered = tuple_list.copy()
    for outr in range(len(ordered)):
        for inr in range(len(ordered)-outr-1):
            if(ordered[inr][1] > ordered[inr+1][1]):
                ordered[inr+1], ordered[inr] = ordered[inr], ordered[inr+1]
    return ordered

def choosing_retirement_home(savings, growth_rates, retirement_houses):
    """Find the most expensive retirement house one can afford.

    Find the most expensive, but affordable, retiremnt house.
    Implemnt the function using binary search

    Args:
    -savings: the initial amount of money in your savings account.
    -growth_rates: a list of annual growth percentages in your
    investment account - a list of floats larger than or equal to -100.
    -retirement_houses: a list of tuples of retirement_houses, where
    the first value is a string - the name of the house and the
    second is the annual rent of it - nonnegative float.

    Return: a string - the name of the chosen retirement house
    Return None if can't afford any house.

    You need to test the legality of savings and growth_rates
    but you can assume legal retirement_house list 
    You can assume that the types of the input are correct"""

    savings = live_like_a_king(savings, 100, [0], growth_rates, 0.1)
    
    #Checks special cases
    if savings is None:
        return
    if not retirement_houses:
        return
    
    # Define the variables beggining point
    retirement_houses = bubble_sort_2nd_value(retirement_houses)
    minus_infinity = -float("inf")
    afford = minus_infinity  # a smaller number than possible otherwise
    mn = 0
    mx = len(retirement_houses)

    # search
    while mn < mx:
        mdl = (mn+mx)//2
        mdl_val = retirement_houses[mdl][1]
        if savings > mdl_val:
            mn = mdl+1
            afford = retirement_houses[mdl][0]
        elif savings < retirement_houses[mdl][1]:
            mx = mdl
        else:
            afford = retirement_houses[mdl][0]
            return afford

    #if no house was affordable
    if afford == minus_infinity:
        return None
    return afford 

def get_value_key(value=0):
    """returns a function that calculates the new value of a house


    #Args:
    -value: the value added per opponent - a float - the default value is 0

    This function returns a function that accepts triple containing
    (house ,annual rent,number of opponents) and returns the new value of
    this house - annual_rent+value*opponents

    You can assume that the input is correct."""
    
    return lambda triple: triple[1]+value*triple[2]
    
def choose_retirement_home_opponents(budget, key, retirement_houses):
    """ Find the best retiremnt house that is affordable and fun

    A function that returns the best retiremnt house to live in such that:
    the house is affordable and
    his value (annual_rent+value*opponents) is the highest

    Args:
    -annual_budget: positive float. The amount of money you can
    expand per year.
    -key: a function of the type returned by get_value_key
    -retirement_houses: a list of houses (tuples), where  the first value
    is a string - the name of the house,
    the second is the annual rent on it - a non negative float, and the third
    is the number of battleship opponents the home hosts - non negative int
    
    Returns the name of the retirement home which provides the best value and
    which is affordable.

    You need to test the legality of annual_budget,
    but you can assume legal retirement_house list 
    You can assume that the types of the input are correct"""
    if budget <= 0:
        return
    minus_infinity = -float("inf")
    mx = minus_infinity  # to make sure something was added
    for ind in retirement_houses:
        crnt = key(ind)
        if mx < crnt and ind[1] <= budget:
            mx = crnt
            name = ind[0]
    if mx == minus_infinity:
        return
    return name
