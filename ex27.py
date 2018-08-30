# Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. 
# Write it in three different ways: 
# 1) using a for-loop, 
# 2) using the higher order function map(), and 
# 3) using list comprehensions.

# 1) using a for-loop, 
# same as ex14.py

def lenght_of_words(l):
	l1=[]
	for x in range(len(l)):
		l1.append(len(l[x]))
	print str(l1)

#test

lenght_of_words (['this', 'is', 'written', 'by', 'Lokesh'])
lenght_of_words (['This','Is','testing','of','mapping', 'of', 'words', 'in', 'the', 'list'])
																																	

# 2)
def using_map(l):
	
	l1 = map(lambda x: len(x),l)
		
	return l1

#test 2

print using_map (['this', 'is', 'written', 'by', 'Lokesh'])
print using_map (['This','Is','testing','of','mapping', 'of', 'words', 'in', 'the', 'list'])	

# 3)
def list_comp(l):
	#list comprehensions example
	#new_list = [expression(i) for i in old_list if filter(i)]
	return [len(word) for word in l] 

#test 3

print list_comp (['this', 'is', 'written', 'by', 'Lokesh'])
print list_comp (['This','Is','testing','of','mapping', 'of', 'words', 'in', 'the', 'list'])

