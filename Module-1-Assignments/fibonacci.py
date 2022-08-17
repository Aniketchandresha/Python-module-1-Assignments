#to print fibonacci series
from typing import Counter


n = int(input("Enter Any number:"))
x=0
y=1

''' for i in range(1,n+1):
    print(x)
    fib = x+y
    x = y
    y = fib'''

counter = 0
while counter < n:
    print(x)
    fib = x + y
    x = y
    y = fib
    counter += 1
