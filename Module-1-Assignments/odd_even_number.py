# Find out if the input number is odd or even

from math import remainder


number = int(input("Enter any number : "))
remainder = number % 2

if remainder == 1:
    print("This is an odd number")
else:
    print("This is an even number")
