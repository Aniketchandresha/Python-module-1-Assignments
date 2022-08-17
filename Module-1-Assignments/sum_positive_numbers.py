# Write a python program to sum of the first n positive integers.

n1 = int(input("Enter any number :"))
n2 = int(input("Enter any number :"))
n3 = int(input("Enter any number :"))

sum = n1+n2+n3

if n1 == n2 or n2 == n3 or n1 == n3:
    print("0")
elif (n1 >= 0) and (n2 >= 0) and (n3 >= 0):
    print(sum)
else :
    print("Enter only positive number")