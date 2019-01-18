# function for finding factorial 
# we use recursion here 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# also you can use python library for that 

t = int(input())

from math import factorial

for i in range(t):
    n = int(input())
    
    print(factorial(n))