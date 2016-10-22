from hash_table import hash_table
import simulations
import string
from hash_functions import hash_functions  

n= 10
int_lst = []
str_lst = []
##table = hash_table(n*2)
rnd_int = simulations.id_generator(string.digits)
rnd_str = simulations.id_generator()
for num in range(n):
    int_lst.append(next(rnd_int))
    str_lst.append(next(rnd_str))
##print(int_lst,str_lst)
##simulations.simulation(int_lst,10,n*2)
##simulations.simulation(str_lst,10,n*2)
##simulations.main() [-m]
##

##print(hash_functions[1](100)("134") == hash_functions[1](100)("1"))
print(hash_functions[6](128)("m"))
print(hash_functions[6](128)("m"))
x = hash_functions[6](128)
