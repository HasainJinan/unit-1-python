#Importing modules.
from datetime import datetime
from datetime import date

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""

#Sets current date and time.
dt_now = datetime.now()
#Printing results.
print(dt_now)


"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

#Sets current date and time.
dt_now_2 = datetime.now()
#Formatting date.
fdt_now_2 = dt_now_2.strftime("%m/%d/%Y")
#Printing results.
print(fdt_now_2)


"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

#Defining strings.
string_1 = "10/02/2019"
string_2 = "09/05/2023"
#Converting to dates.
date_1 = datetime.strptime(string_1, "%m/%d/%Y")
date_2 = datetime.strptime(string_2, "%m/%d/%Y")
#Finding and printing difference.
print(abs((date_1 - date_2).days))


"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

#Asks for birthday.
bday = str(input("Enter your birthday in MM/DD/YYYY format: "))
#Converts string to date.
bday_date = datetime.strptime(bday, "%m/%d/%Y")
#Takes current date and calculates user age.
today = datetime.today()
difference = (today - bday_date).days
#Printing results.
print("You are " + str(difference) + " days old.")