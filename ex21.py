# Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. 
# Represent the frequency listing as a Python dictionary. 
# Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").

def char_freq(str):
	frequency = {}
	for n in str:
		key = frequency.keys()
		if n in key:
			frequency[n] += 1
		else:
			frequency[n] = 1
	return frequency


#test
print char_freq('abbabcbdbabdbdbabababcbcbab')
print char_freq('qqqqqqqqqbuyfcvadkdnigfnclddncidug')
