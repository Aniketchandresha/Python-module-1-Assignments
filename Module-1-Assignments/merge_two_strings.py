'''Write a Python program to get a single string from two given strings, separated by a 
space, and swap the first two characters of each string.'''

fname = input("Enter your first name : ")
lname = input("Enter your last name : ")

new_fname = lname[:2] + fname[2:]
new_lname = fname[:2] + lname[2:]
print(f"{new_fname} {new_lname}") 