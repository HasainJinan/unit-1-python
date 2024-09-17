"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.
"""

#Creating float variable.
flt = 1.5
#Converting float to int.
flt_2 = int(flt)
#Printing original float and converted int.
print(flt)
print(flt_2)

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""

#Asking for number.
num = float(input("Input a number: "))
#Deciding if number is positive, negative, or zero.
if num == 0:
    print("This number is 0.")
elif num > 0:
    print("This number is positive.")
else:
    print("This number is negative.")

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""

#Taking int and float as inputs.
num_int = int(input("Input an integer: "))
num_flt = float(input("Input a decimal number: "))
#Performing operations.
num_add = num_int + num_flt
num_sub = num_int - num_flt
num_mul = num_int * num_flt
num_div = num_int / num_flt
#Printing results.
print(num_add)
print(num_sub)
print(num_mul)
print(num_div)

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""

#Defining fruit inventory.
fruit_inv = {
    "apples": 4,
    "bananas": 2,
    "oranges": 0,
    "kiwis": 6
}
#Printing quantities.
print(list(fruit_inv.values()))

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

#Creating string.
strng = "1,2,3,4,5,6"
#Converting to tuple.
strng_2 = tuple(strng.split(","))
#Printing string and tuple.
print(strng)
print(strng_2)