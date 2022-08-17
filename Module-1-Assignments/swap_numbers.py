# swap two numbers with temp variable and without temp

from re import A


a=5
b=10

print(a)
print(b)

# using temp variable 

temp = a
a = b
b = temp
print(a)
print(b)

# Without temp

a , b = b , a

print(a)
print(b)