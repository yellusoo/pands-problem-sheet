#Week 2 problem sheet
#This programme seeks user input of two currency amounts, adds them and outputs the result in Euro
#Author; OOS

firstvalue = input("Enter your first amount in cents please ")
secondvalue = input("Enter your second amount in cents please ")
total = int(firstvalue) + int(secondvalue)
totaleuro = total/100
totalreadable = "€" + (str(totaleuro))
print("Your total is " + (str(totalreadable)))