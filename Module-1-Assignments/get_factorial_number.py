#Get factorial number of given number
# from math import factorial
# number = int(input("Enter any number: "))

# print(factorial(number))
n = int(input("Enter any number :"))
fact = 1

for i in range(1,n+1):
    fact *= i

print(fact)