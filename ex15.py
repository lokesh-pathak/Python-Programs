# Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def find_longest_word(l):
	longest=l[0]
	for x in range(len(l)):
		if len(l[x])>len(longest):
			longest=l[x]
	return longest


#test

print find_longest_word(['This','is','done','for','testing'])