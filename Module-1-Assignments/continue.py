# Continue statement in python 
# conitnue program helps the loop to continue and omit the given condition

cities = ["Rajkot","Ahmedabad","Bhavnagar","Junagadh","Vadodara"]

for city in cities :
    if city == "Bhavnagar" :
        break;
    print (city)

for city in cities :
    if city == "Bhavnagar" :
        continue;
    print (city)