# SUm of 3 input integers

n1 = int(input("Enter any number : "))
n2 = int(input("Enter any number : "))
n3 = int(input("Enter any number : "))

sum = n1 + n2 + n3

if n1 == n2 :
    print("The sum is Zero because of same enterd integers ")
elif n1 == n3 :
    print("The sum is Zero because of same enterd integers ")
elif n2 == n3 :
    print("The sum is Zero because of same enterd integers ")
else :
    print(f"The sum is : {sum}")
