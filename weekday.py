#Week 5 Weekly Task
#This program outputs whether or not today is a weekday. 
#Author OOS

from datetime import datetime

# get current datetime
dt = datetime.now()

#Above code sourced from https://www.programiz.com/python-programming/datetime/current-datetime

if dt.isoweekday() == 1 or 2 or 3 or 4 or 5:
    print("Yes, unfortunately today is a weekday.")
else:
 print("Yay, it's the weekend")

# Information around isoweekday sourced from https://docs.python.org/3/library/datetime.html#datetime.date.isoweekday




