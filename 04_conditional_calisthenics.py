'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
#Integer.
integer = 14
#Checking if integer is eve nand greater than 10.
print(((integer % 2) == 0) and integer > 10)

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

#Ask for age.
age = int(input("What is your age in only years? "))
#Ask for student status.
status = input("Are you a student? ")
#Check for discount eligibility.
if age < 18 or status.lower() == "yes":
    print("The price for your ticket is $10.")
else:
    print("The price for your ticket is $20.")

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

#List of fruits.
my_fruits = ["apple", "banana", "kiwi", "orange", "pineapple"]
#Checking variable.
check = 0
#Asking for fruit.
fruit = input("Name a fruit: ")
#Checking fruit with list.
for x in my_fruits:
    if str(fruit.lower()) == x:
        print("Your fruit is in the list.")
        check = check + 1
#If fruit is not in list.
if check == 0:
    print("Your fruit is not in the list.")

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

#Asking for year.
year = int(input("Enter a year: "))
#Checking for century year status.
if (year % 100) == 0:
    print("Your selected year is a century year.")
else:
    print("Your selected year is not a century year.")
#Checking for leap year status.
if (year % 4) == 0:
    print("Your selected year is a leap year.")
else:
    print("Your selected year is not a leap year.")

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

#Weight.
weight = input("Enter weight in kg: ")
#Destination.
zone = input("Zone A or B? ")
#Shipping cost calculator.
if zone.lower() == "zone a" or zone.lower() == "a":
    cost = int(weight) * 5
    print("This order will cost $" + str(cost) + ".")
elif zone.lower() == "zone b" or zone.lower() == "b":
    cost = int(weight) * 7
    print("This order will cost $" + str(cost) + ".")

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
#Side 1.
s1 = int(input("Enter unit length of side 1: "))
#Side 2.
s2 = int(input("Enter unit length of side 2: "))
#Side 3.
s3 = int(input("Enter unit length of side 3: "))
#Caclulate.
if s1 > (s2 + s3) or s2 > (s1 + s3) or s3 > (s1 + s2):
    print("This is not a triangle.")
elif s1 == (s2 + s3) or s2 == (s1 + s3) or s3 == (s1 + s2):
    print("This is not a triangle.")
elif s1 < (s2 + s3):
    if s2 == s3:
        print("This triangle is an isosceles triangle.")
    elif s2 < s3 or s3 < s2:
        print("This triangle is a scalene triangle.")
    else:
        pass
elif s2 < (s1 + s3):
    if s1 == s3:
        print("This triangle is an isosceles triangle.")
    elif s1 < s3 or s3 < s1:
        print("This triangle is a scalene triangle.")
    else:
        pass
elif s3 < (s1 + s2):
    if s1 == s2:
        print("This trianlge is an isosceles triangle.")
    elif s1 < s2 or s2 < s1:
        print("This triangle is a scalene triangle.")
    else:
        pass
elif s1 == s2 and s2 == s3:
    print("This triangle is an equilateral triangle. It is also isosceles.")
else:
    print("This is not a triangle.")