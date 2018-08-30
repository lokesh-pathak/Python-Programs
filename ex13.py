# The function max() from exercise 
# 1) and the function max_of_three() from exercise 
# 2) will only work for two and three numbers, respectively. 
# But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? 
# Write a function max_in_list() that takes a list of numbers and returns the largest one

def max_in_list(l):

	largest= l[0]
	for x in l:
		if x>largest:
			largest=x
	return largest

#test

print max_in_list([1, 2, 3, 4])
print max_in_list([2, 3, 6, 5])
print max_in_list([100, 99, 1001, 501])
print max_in_list([65, 97, 45, 77])