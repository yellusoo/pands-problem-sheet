#This program imports the filename from the CMDline and counts the number of "e" letters in the text file
#Author: OOS

#Code taken from https://www.tutorialspoint.com/How-to-read-a-file-from-command-line-using-Python

FILENAME = "newarguments.txt"
with open(FILENAME, 'x') as f:
    f.write("eeeieepouyyeeeeerrtytrtjfrjjfjjf4325636262e")
print(FILENAME)

import sys
with open("newarguments.txt", 'r') as f:
    contents = f.read()

#Code taken from https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/


# function to return the letter count
def letterFrequency(fileName, letter):
	
	file = open("newarguments.txt", 'r')

	# store content of the file in a variable
	text = file.read()

	# using count()
	return text.count(letter)


# call the function and display the letter count
print("There are " + str(letterFrequency('newarguments.txt', 'e')), "e's in this file")