#This is the assigned task for Week 3
#This program reads in bank numbers, with any number of digits, and replaces the first 6 to maintain privacy. It displayes the final 4+ digits
#Author: OOS

import re #https://stackoverflow.com/questions/30141233/replacing-the-integers-in-a-string-with-xs-without-error-handling

ac_number = input("Input your 10 digit account number here:")
listed_ac_number = list(ac_number)

#This method adapted from https://www.pythonpool.com/replace-item-in-list-python/

listed_ac_number[0] = "X"
listed_ac_number[1] = "X"
listed_ac_number[2] = "X"
listed_ac_number[3] = "X"
listed_ac_number[4] = "X"
listed_ac_number[5] = "X"

#This code alters the first six numbers to be equal to X, assuming that at least 6 digits are present

string_ac_number = "" .join(listed_ac_number)

#The above line of code follows https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python

print("Your account number is {}".format(string_ac_number))
