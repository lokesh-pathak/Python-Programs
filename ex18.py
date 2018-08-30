# A pangram is a sentence that contains all the letters of the English alphabet at least once, 
# for example: The quick brown fox jumps over the lazy dog. 
# Your task here is to write a function to check a sentence to see if it is a pangram or not. 

#pangram = lambda s: not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())

# # A set is an unordered collection with no duplicate elements
# The first set is for alphabet letters, in lowercase
# The second set is the characters from the test string, also in lowercase. And all the duplicates are gone as well.


#test

# print pangram('The quick brown fox jumps over the lazy dog')
# print pangram('The list is not pangram')	


pang = "abcdefghijklmnopqrstuvwxyz"

def is_pangram(str):
	count = 0
	str1 = ""
	
	# to remove duplicates from the string

	for char in str:
		for c in pang:
			if char == c and char not in str1:
				str1 += char

	# to check the char in the string 

	for char in str1:
		for c in pang:
			if char == c:
				count += 1
	if count == 26:
		return True
	else:
		return False

#test

print is_pangram("The quick brown fox jumps over the lazy dog")
print is_pangram('The list is not pangram')
