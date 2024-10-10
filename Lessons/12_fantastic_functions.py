"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""

#Asks for name.
you = input("What is your name: ")

#Greeting function.
def greeting(name):
    """
    Takes an argument called name and inputs the argument into the string "Hello {0}!"
    """
    print("Hello " + name + "!")

#Function.
greeting(you)

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

#Asking for integer.
num = int(input("Enter an integer: "))

#Square root function.
def square():
    """
    Takes a input called num and squares it, returning the final value to a variable called "sqrt".
    """
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
    """
    If the inputted integer returns 0 when you perform "[input] % 2," the number is even and the function returns the boolean value "True."

    If the inputted integer returns 1 when you perform "[input] % 2," the number is odd and the function returns the boolean value "False."
    """
    if example % 2 == 0:
        return True
    elif example % 2 == 1:
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
    """
    The area of a rectangle is determined by the length of the rectangle multiplied by its width.

    The function takes two previously asked for variables called "l [Length]" and "w [Width]" and multiplies them.
    """
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
    """
    Celsius is converted to Fahrenheit through the formula "C * (9/5) + 32 = F."
    
    C represents the inputted value of degrees Celsius, and F represents the output of degrees Fahrenheit.
    """
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
    """
    If the length of the list is greater than 0, meaning the list contains numbers, then each item in the list is added to a value called total.

    After that, the final value of total is divided by the length of the list which is found using len(list) and the final value is returned to the variable "average".

    If the length of the list is equal to 0, meaning the list is empty, then the function simply returns the string "Empty list."
    """
    total = 0
    for x in list:
        total = total + x
    if len(list) != 0:
        return total / len(list)
    else:
        return "Empty list."

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

#Asks if you have a discount and evaluates. Just making it convenient.
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
    """
    If the discount amount is unaltered and is still 0, the function only multiplies the quantity by the unit price and returns that value as "total_price".

    If the discount is not 0, then the function multiplies the price by the quantity before multiplying by the discount which will be a decimal.

    Then the function returns the discounted price as "total_discount".
    """
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