# Write a program that will calculate the average word length of a text stored in a file
# (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).

def avg_word_length():
	f=open('file_path','r')
	# it gives a list of words in the from of list
	file=f.read().split()
	sum=0.0
	length=0
	for word in file:
		sum=sum+1
		length=length+len(word)
	average=length/sum
	return average
print avg_word_length()
