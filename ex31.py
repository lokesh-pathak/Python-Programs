# Implement the higher order functions 
# map(), 
# filter() and 
# reduce(). 
# (They are built-in but writing them yourself may be a good exercise.)
"""Implement the higher order functions map(), filter() and reduce(). 
(They are built-in but writing them yourself may be a good exercise.)"""

#1) map() function

def my_map(function, sequence):
	result = []
	for c in sequence:
		result.append(function(c))
	return result

#test
print my_map(lambda x: x * 2, [1,2,3,4])



#2) filter() function

def my_filter(function,sequence):
	result=[]
	for c in sequence:
		if function(c):
			result.append(c)
	return result
#test

print my_filter(lambda word:len(word)>3,['pig','lion', 'zebra', 'elephant', 'panda'])



#3) reduce() function

def my_reduce(function,sequence):
	result=sequence[0]
	for c in sequence[1:]:
		result=function(result,c)
	return result	

#test
print reduce(lambda a,b: a if (a > b) else b, [1, 2, 3, 4, 5])