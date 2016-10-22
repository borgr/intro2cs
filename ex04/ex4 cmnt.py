#############################################################
# FILE : ex4.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex4 200132014
# DESCRIPTION: functions for post retirement
# 
#############################################################

##def constant_pension(salary, save, growth_rate, years):
##
##    """ calculate retirement fund assuming constant pesnion
##
##    A function that calculates the value of a retirement fund in each year
##    based on the worker salary, savings, working years and assuming constant
##    growthRate of the fund
##
##    Args:
##    - salary: the amount of money you earn each year,
##           a non negative float.
##    - save: the percent of your salary to save in the investment account
##            each working year -  a non negative float between 0 and 100
##    - growth_rate: the annual percent increase/decrease in your investment
##           account, a float larger than or equal to -100 (minus 100)
##    - years: number of years to work - non negative int
##
##    return: a list whose values are the size of your retirement account at
##      the end of each year.
##
##    In case of bad input: values are out of range
##    returns None
##
##    You can assume that the types of the input arguments are correct. """
##
##    if (salary >= 0 and save >= 0 and save <= 100
##        and years > 0 and growth_rate >= -100):
##        rtrn = [salary*save*0.01]
##        for i in range(years-1):
##            rtrn.append(rtrn[i]*(1+growth_rate*0.01)+salary*save*0.01)
##    elif years == 0:
##        rtrn = []
##    else:
##        return
##    return rtrn
##
##
##

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
    if len(growth_rates) > 0 and growth_rates[0]<-100:
        return
    if salary >= 0 and save >= 0 and save < 101 and len(growth_rates) >= 1:
        rtrn = [salary*save*0.01]
        for i in range(len(growth_rates)-1):
            if growth_rates[i+1] < -100:
                return
            rtrn.append(rtrn[i]*(1+growth_rates[i+1]*0.01)+salary*save*0.01)
    elif len(growth_rates) == 0:
        rtrn = []
    else:
        return
    return rtrn



##def choose_best_fund(salary,save,funds_file):    
##    """find the best fund to invest in
##
##    A function that calculates the best fund to invest money in from a list
##    of funds in a file.
##
##    Args:
##    - salary: the amount of money you earn each year, a non negative float.
##    - save: the percent of your salary to save in the investment account
##    each working year -  a non negative float between 0 and 100
##    - funds_file: A file that lists the different funds that you may choose
##    to invest in
##    format of the file:
##    nameOfFund0,annoalGrowthYear0, annoalGrowthYear1, annoalGrowthYear2 …
##    nameOfFund1,annoalGrowthYear0, annoalGrowthYear1, annoalGrowthYear2 …
##    nameOfFund2,annoalGrowthYear0, annoalGrowthYear1, annoalGrowthYear2 …
##
##
##    return: a tuple, where its first value is the name of the best fund to
##    invest in assuming such an annual deposition, and the seocnd value in the
##    tuple is the value of the pension fund in its end assuming we choose the
##    best fund.
##
##    In case of bad input: values are out of range
##    returns None
##
##    Note that for this specific exercise you may assume a correct form
##    of the file. If an error accourd (File not exist, wrong type inside
##    the file - Let python print its error and exit (Will happen
##    automatically)
##
##    You may also assume that the lists of growthRates have the same length
##    and that the types of the inputs arguments are correct. """
##    
##    bst_ttl = -200 
##    with open(funds_file) as opn:
##
##        for crn_fnd in opn:
##            #Adds the name to the current fund name and gets to the growths
##            i = 1
##            comma = crn_fnd[i]
##            crn_nam = ""
##            while comma != "," and i+1 < len(crn_fnd):
##                crn_nam += comma
##                i += 1
##                comma = crn_fnd[i]
##            growth_rates = []
##                
##            #adds each growth to a list
##            i += 1
##            yr_grth = "0"     
##            while i < len(crn_fnd): 
##                if crn_fnd[i] == ",":
##                    growth_rates.append(float(yr_grth))
##                    yr_grth = "0"
##
##                #Splits the string to numbers, without letters. 
##                elif crn_fnd[i] == "-":
##                    yr_grth = "-"+yr_grth
##                elif crn_fnd[i].isdigit() or crn_fnd[i] ==".":
##                    yr_grth += crn_fnd[i]
##                if i+1 == len(crn_fnd):
##                    growth_rates.append(float(yr_grth))
##                i += 1
##            crn_ttl = variable_pension(salary, save, growth_rates)
##            
##            #If needed, updates the best fund details.
##            if crn_ttl and crn_ttl[-1] > bst_ttl:
##                bst_ttl = crn_ttl[-1]
##                bst_nam = crn_nam
##        if bst_ttl != -200:
##            return bst_nam, bst_ttl
##        return
##        
##

##def growth_in_year(growth_rates,year):
##    """return the growth value in a given year
##
##    Args:
##    - growth_rates: the annual percent increase/decrease in your investment
##    account - a float larger than or equal to -100
##    -year: the index in the list we are intersted in
##    a int between 0 and the size of growthRates
##
##    return: a float with the value of growthRates in the specified year or
##    None in case of a year not in the list
##
##    You can assume that the types of the input arguments are correct."""
##    
##    if year>len(growth_rates)-1 or year < 0:
##        return
##    for i in range(len(growth_rates)):
##        if growth_rates[i] < -100:
##            return
##    return growth_rates[year]
##    
##
##  
##
##
##def inflation_growth_rates(growth_rates,inflation_factors):
##    """ Calculate the adjusted growth list given inflation
##
##
##    A function that return a new list with a adjusted growth rates due to
##    the inflation. inflation should be adjusted for all years there is both
##    inflation factor and growth factor.
##    inflation is defined as 100*((100+g)/(100+i)-1)
##    where g is growth in that year and i is the inflation.
##
##    Args:
##    - growth_rates: the annual percent increase/decrease in your investment
##    account - a float larger than or equal to -100
##    -inflation_factors: the annual inflation in percents.
##    a float larger than (BUT NOT EQUAL) to -100 .
##    The list may have different size from growth_rates.
##
##    returns a NEW list with the same length as growth_rates but during the
##    inflation years the rates are adjusted.
##    In case of bad input: values are out of range returns None
##
##    You can assume that the types of the input arguments are correct."""
##    rtrn = []
##    i = -1
##    #looks for the inflation rates
##    for i in range(len(growth_rates)):
##        if ((i < len(inflation_factors) and (inflation_factors[i] <= -100))
##            or growth_rates[i] < -100):
##            return
##        elif (i <= len(inflation_factors) -1):
##            rtrn.append(100*((100+growth_rates[i])/
##                              (100+inflation_factors[i])-1))
##        else:
##            rtrn.append(growth_rates[i])
##            
##    #Finishs checking exceptions
##    while i+1 < len(inflation_factors):
##        i+=1
##        if inflation_factors[i] <= -100:
##             return
##    return rtrn
##
##
##
##def post_retirement(savings, growth_rates, expenses):
##    """ calculates the account status after retirement
##
##    A function that calculates the account status after retirement, assuming
##    constant expenses and no income
##    Args:
##    -savings: the initial amount of money in your savings account.
##    A float larger than 0
##    - growth_rates: the annual percent increase/decrease in your investment
##    account - a float larger than or equal to -100
##    -expenses: the amount of money you plan to spend each year during
##    retirement. A non negative float
##
##    return: a list of your retirement account value at the end of each year.
##
##    Note in case of a negative balance - the growth rate will change into
##    rate on the debt
##    In case of bad input: values are out of range returns None
##
##    You can assume that the types of the input arguments are correct."""
##    account = []
##    if not growth_rates:
##        return account
##    if (expenses >= 0 and growth_rates[0]>=-100
##        and savings > 0):
##        account.append(savings*(1+growth_rates[0]*0.01) -expenses)
##        for i in range(1, len(growth_rates)):
##            if growth_rates[i]<-100:
##                return
##            account.append(account[i-1]*(1+growth_rates[i]*0.01)-expenses)
##        return account
##    return
        
#new functions
##def check (lst):
##    """checks if everything in the list or tuple, is not above -100
##
##    Args:
##    List to be checked.
##    Returns:
##    False if all numbers are above -100 otherwise True."""
##    
##    for i in lst:
##        if i<-100:
##            return True
##    return False

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
    if not post_retire_growth_rates or epsilon <= 0:
        return
    product = variable_pension(salary, save, pre_retire_growth_rates)
    if product == None:
        return
    if len(product) == 0:
        return 0
    else:
        product = product[-1]
    denominator = 0
    for i in post_retire_growth_rates:
        if i<-100:
            return
    for i in post_retire_growth_rates:
        product = product*(1+i/100)
        denominator = denominator*(1+i/100) +1
        
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
    for i in range(len(ordered)):
        for j in range(len(ordered)-i-1):
            if(ordered[j][1] > ordered[j+1][1]):
                ordered[j+1],ordered[j] = ordered[j],ordered[j+1]
    return ordered





def choosing_retirement_home(savings,growth_rates,retirement_houses):
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
    if savings == None:
        return
    if not retirement_houses:
        return
    
    # Define the variables beggining point
    retirement_houses = bubble_sort_2nd_value(retirement_houses) 
    mx = len(retirement_houses)-1
    mn = 0
    afford = -1

    mn = 0
    mx = len(retirement_houses)
    while mn<mx:
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
    if afford == -1:
        return None
    return afford

##    #Search with binaric algorithm for best affordable house
##    while mn < mx:
##        mdl = (mx+mn)//2
##        if retirement_houses[mdl][1] < savings :
##            mn = mdl+1
##            afford = retirement_houses[mdl][0]
##        elif retirement_houses[mdl][1] == savings:
##            return retirement_houses[mdl][0]
##        else:
##            mx = mdl
##    if (mx == 0 and retirement_houses[mx][1] <= savings):
##        return retirement_houses[mx][0]
##
##    #Return the best house if exists
##    if afford == -1:
##        return
##    return afford    
    

def get_value_key(value = 0):
    """returns a function that calculates the new value of a house


    #Args:
    -value: the value added per opponent - a float - the default value is 0

    This function returns a function that accepts triple containing
    (house ,annual rent,number of opponents) and returns the new value of
    this house - annual_rent+value*opponents

    You can assume that the input is correct."""
    
    def new_value(triple):
        return triple[1]+value*triple[2]
    return new_value
    

   

def choose_retirement_home_opponents(budget,key,retirement_houses):
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
##    fun_func = get_value_key(key)
    mx = -1
    for i in retirement_houses:
##        crnt = fun_func(i)
        crnt = key(i)
        if mx < crnt and i[1] <= budget:
            mx = crnt
            name = i[0]
    if mx == -1:
        return
    return name

   

    
