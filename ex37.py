# Write a program that given a text file will create a new text file
# in which all the lines from the original file are numbered from 1 to n
# (where n is the number of lines in the file).

def new_file():
	f=open('file_path','r+')
	file=f.readlines()
	copy=open('file_path', 'w+')
	sum=0
	for line in file:
		sum=sum+1
		z='Line Number %d - %s' %(sum,line)
		copy.write(z)
	f.close()
	copy.close()


#test
new_file()
