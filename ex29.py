# Using the higher order function filter(), 
# define a function filter_long_words() that takes a list of words 
# and an integer n 
# and returns the list of words that are longer than n.

def filter_long_words(l,n):

	return filter(lambda word:len(word)>n, l)


#test

print filter_long_words(['this', 'is', 'written', 'by', 'Lokesh'],4)