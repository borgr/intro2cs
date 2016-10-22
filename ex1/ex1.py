#############################################################
# FILE : ex1.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex1 200132014
# DESCRIPTION:
# This program asks for a 3 digit
# number and shows the Einstein's
# riddle with it.
#############################################################

print("Welcome to the Einstein puzzle")
num = (int)(input("Please enter a three digit number:"))
#Reverse the input:
reverse_num = (num%10)*(100-1) + num%100
reverse_num = reverse_num+num//100
print("For the number:", num, "the reverse number is:", reverse_num)
difference = abs(num-reverse_num)
print("The difference between", num, "and", reverse_num
      , "is", difference)
reverse_dif = (difference%10)*(100-1) + difference%100
reverse_dif = reverse_dif+difference//100
print("The reverse difference is:", reverse_dif)
print("The sum of:", difference, "and", reverse_dif, "is:",  difference+reverse_dif)
