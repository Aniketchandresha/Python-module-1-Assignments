"""Write a Python program that will return true if the two given integer values are equal 
or their sum or difference is 5."""

from difflib import Differ


n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))

sum = n1 + n2
difference = n1-n2
difference2 = n2-n1

if n1 == n2:
    print("True1")
elif sum == 5:
    print("True2")
elif difference == 5 :
    print("True3")
elif difference2 == 5 :
    print("True4")
else : 
    print("False")
    
