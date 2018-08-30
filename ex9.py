# Write a function is_member() that takes a value 
# (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. 

def is_member():
	ele=raw_input("enter value")
	lst=raw_input().split()
	for e in lst:
		if ele == e:
			return True
	return False
	print type(ele)
	print type(lst)


# #test
# print is_member("e", ['a', 'e', 'i', 'o', 'u'])
# print is_member(19, [1,3,4,6,18,20])
# print is_member('abc', ['abc', 'pqr', 'rty', 'poihvg'])
# print is_member('panda', ['lion', 'zebra', 'elephant', 'panda'])

print is_member()