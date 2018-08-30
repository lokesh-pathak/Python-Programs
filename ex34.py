# Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a frequency
# listing of the characters contained in the file, and prints a sorted and nicely formatted character frequency table to
# the screen.

# Before running the code first comment ex21 output
from ex21 import char_freq


def char_freq_table():
	f=open('file_path','r+')
	file=f.read().lower().replace(" ", "").strip()
	z= char_freq(file)
	print sorted(z.items())
	f.close()
#test
char_freq_table()
