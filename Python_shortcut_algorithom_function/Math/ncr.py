'''
In this class, we are going to find nCr. 
The formula of nCr = n!/r!/(n-r)!
We will use python build in function calculating factorial
Bacause by using our recursion method, python exceeds recursion limit for large number
'''
import math # import math for calculating factorial

def nCr(n, r):
	'''
	Function for calculating nCr

	Here we use '//' instead of '/' because it throws some errors when dealing with large number 
	So '//' divide with integral result (discard remainder)
	
	Also, we using abs(n-r). Because n can be less than r. 
	In this case, math.factorial throws error. 
	Because it can't handle negative value
	'''
    f = math.factorial
    ncr = f(n) // f(r) // f(abs(n-r))
    return ncr
