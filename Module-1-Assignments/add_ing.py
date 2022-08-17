'''Write a Python program to add 'ing' at the end of a given string (length should be at 
least 3). If the given string already ends with 'ing' then add 'ly' instead if the string
length of the given string is less than 3, leave it unchanged.'''

activity = input("Enter any activity : ")

ing_activity = activity + "ing"
ly_activity = activity + "ly"

if len(activity) < 3:
    print(activity)
elif activity[-3:] == "ing" :
    print(ly_activity)
else :
    print(ing_activity)
