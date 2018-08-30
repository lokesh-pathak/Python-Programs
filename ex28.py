# Write a function find_longest_word() that takes a list of words 
# and returns the length of the longest one. 
# Use only higher order functions.

def find_longest_word(l):
	z=map(lambda x: len(x),l)
	y=reduce (lambda a,b:a if a>b else b,z)
	return y
	
#test

print find_longest_word (['this', 'is', 'written', 'by', 'Lokesh'])