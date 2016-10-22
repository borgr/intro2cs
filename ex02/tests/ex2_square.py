#############################################################
# FILE : ex2_square.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex2 200132014
# DESCRIPTION:
# This program prints a # square and a * rhumbus.
# The rhumbus side is n.
# ARGUMENTS:
# int n>0
#############################################################
#!/usr/bin/env python3
def square_printing(n):
    #This program makes a square and a rhombus out of # and *
    #where the square's side is n (the input).
    i = 1
    output = []
    output.append("#"*(2*n+1))
    print(output[0])
    output.append("#"+" "*(n-1)+"*"+" "*(n-1)+"#")
    print(output[1])

    #Prints and creates the top half of the picture.
    while(i<n):
        output.append("#"+" "*(n-1-i)+"*"+" "*(i*2-1)+
                      "*"+" "*(n-1-i)+"#")
        i= i+1
        print(output[i])

    #Prints the other half
    i = 1
    while(i<=n):
        print(output[-1-i])
        i=i+1

#Here to help you test your code.
if __name__=="__main__":  #If we are the main script, and not imported
    from sys import argv
    try:
        n = int(argv[1])
    except:
        n = int(input("Please enter a positive integer: "))
    square_printing(n)
