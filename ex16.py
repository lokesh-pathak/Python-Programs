# # Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.


def filter_long_words(l,n):
	word=[]
	for x in range(len(l)):
		if len(l[x])>n:
			word.append(l[x])
	return word


#test

print filter_long_words(['lion', 'zebra', 'elephant', 'panda'], 4)

print filter_long_words(['abc', 'pqr', 'rty', 'poihvg'], 2)
