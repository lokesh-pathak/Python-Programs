# Using the higher order function reduce(), 
# write a function max_in_list() that takes a list of numbers and returns the largest one. 
# Then ask yourself: why define and call a new function, 
# when I can just as well call the reduce() function directly?

from functools import reduce
def max_in_list(l):
	z=reduce (lambda a,b:a if a>b else b,l)
	return z
#test
print max_in_list([99,5,555,100,1235,45])
print max_in_list([22,55,33,77,66,44])