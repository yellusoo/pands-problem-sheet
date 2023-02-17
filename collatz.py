#This is the assigned task for Week 4
#This program 
#Author: OOS

# The following code is from: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

value = input("Please enter a positive whole integer: ")

def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


while value != 1:
    value = collatz(int(value))