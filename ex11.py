# Define a function generate_n_chars() that takes an integer n and a character c and returns a string,
# n characters long, consisting only of c:s. 
# For example, generate_n_chars(5,"x") should return the string "xxxxx".

def generate_n_chars(n,c):
	str=''
	while(n>0):
		str+=c
		n-=1
	return str

#test

print generate_n_chars(5,'l')	
print generate_n_chars(9,'z')
print generate_n_chars(1,'a')