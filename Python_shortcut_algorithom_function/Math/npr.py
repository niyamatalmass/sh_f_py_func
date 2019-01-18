# nPr is (n!) / (n-r)!
# so we have to calculate n! and (n - r)!

# first factorial function 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def npr(n, r):
	# then calculate the npr
	# we wrap with int because we perform divide operation that will produce fraction. and we want just numbers
	# you can ignore int() wrap also if problem accept decimal
	return int(factorial(n) / factorial(n-r))
