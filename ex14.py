# # Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.

def lenght_of_words(l):
	l1=[]
 	for x in range(len(l)):
 		l1.append(len(l[x]))
 	print ('List of words:'+str(l))
 	print ('List of wordlength:'+str(l1))

#test

lenght_of_words (['this', 'is', 'written', 'by', 'Lokesh'])
lenght_of_words (['This','Is','testing','of','mapping', 'of', 'words', 'in', 'the', 'list'])
