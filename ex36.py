# A hapax legomenon (often abbreviated to hapax) is a word
# which occurs only once in either the written record of a language,
# the works of an author, or in a single text.
# Define a function that given the file name of a text will return all its hapaxes.
# Make sure your program ignores capitalization.

def hapax():
	f=open('file_path','r+')
	file=f.read().lower().split()
	#print file
	frequency = {}
	l=[]

	for n in file:
		key = frequency.keys()
		#print key
		if n in key:
			frequency[n] += 1
		else:
			frequency[n] = 1
	#print frequency
	for x in frequency:
		if frequency[x]==1:
			l.append(x)
	print l
	f.close()
#test
# char_freq("this is a test case and the test is a success")
hapax()
