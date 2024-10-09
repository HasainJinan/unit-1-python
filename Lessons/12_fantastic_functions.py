"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""

#Greeting function.
def greeting(name):
    print("Hello " + name + "!")

#Function.
greeting("Hasain")

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

#Asking for integer.
num = int(input("Enter an integer: "))

#Square root function.
def square():
    return num**2
    
#Returning square root.
sqrt = square()

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""

#Asking for a number.
example = int(input("Enter a number: "))

#Function to determine if number is even or odd.
def even_or_odd():
    if example % 2 == 0:
        return True
    elif example % 2 ==1:
        return False

#Returning evaluation.
is_even = even_or_odd()

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""

#Asking for length and width of a rectangle.
l = float(input("Enter the length of the rectangle: "))
w = float(input("Enter the width of the rectangle: "))

#Function to calculate area.
def area():
    return l * w

#Returning area of rectangle.
area = area()

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

#Asking for temperature in Celsius.
deg_c = float(input("Enter temperature in degrees Celsius: "))

#Function converting to Fahrenheit because 'Murica.
def C_to_F():
    return (deg_c * 9/5) + 32

#Returning temperature in Fahrenheit.
deg_f = C_to_F()

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

#Initial list.
list = []

#Add number or leave?
choice = input('"Add" a number or "Exit": ')
print()

#Loop to ask for numbers or exit.
while choice == "Add":
    num1 = float(input("Enter a number: "))
    print()
    list.append(num1)
    choice = input('"Add" a number or "Exit": ')
    print()

while choice == "Exit":
    print("Calculating...")
    break

#Function to find average.
def avg():
    total = 0
    for x in list:
        total = total + x
    if len(list) != 0:
        return total / len(list)

#Returning the mean.
average = avg()

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, and returns the total.
Your function should also optionally accept a 3rd argument for discount, and return the discounted if provided.
"""

#Asks for unit price and quantity.
unit_price = float(input("Enter unit price: "))

number = float(input("Enter quantity of items: "))

#Asks if you have a discount and evaluates.
dis = input("Do you have a discount? Yes/No: ")
while dis.lower() != "yes" and dis.lower() != "no":
    print("Sorry I do not understand. Please try again.")
    dis = input("Do you have a discount? Yes/No: ")
else:
    if dis.lower() == "yes":
        dis_amount = float(input("How much is your discount as a decimal: "))

    elif dis.lower() == "no":
        print("Very well then.")

#Function to determine total price.
def total(price, quantity, discount = 0):
    if discount == 0:
        return price * quantity
    else:
        return price * quantity * discount
    
#Returning total price.
if dis.lower() == "no":
    total_price = total(unit_price, number)
    print(total_price)
elif dis.lower() == "yes":
    total_discount = total(unit_price, number, dis_amount)
    print(total_discount)