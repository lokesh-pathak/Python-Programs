# Write a version of a palindrome recogniser that accepts a file name from the user, 
# reads each line, and prints the line to the screen if it is a palindrome.
def palindrom():
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

	f=open('/home/tapfame/prog/palindrom','r+')
	file=f.readlines()
	#print file
	

	for line in file:
		#import pdb; pdb.set_trace();
		line = line.strip()
		for char in line:
			#print char
			if char in punctuations:
				line = line.replace(char,'')
		
		if line.lower()==line[::-1].lower():
			print True
		else:
			print False
	f.close()

palindrom()