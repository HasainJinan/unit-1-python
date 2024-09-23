import math
print("CALCULATOR 1.0")
print()
print()
#Ask for first number.
num1 = float(input("Enter number one: "))
#Ask for second number.
num2 = float(input("Enter number two: "))
print()
print()
#Operation list.
print("Operations:")
print()
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponential")
print("7. Remainder")
print()
#Calculator choice.
choice = int(input("Enter the number of the operation you want to perform: "))
print()
#Calculation and printing results.
def calc():
    if choice == 1:
        num3 = num1 + num2
        print("Answer: " + str(num3))
    elif choice == 2:
        num3 = num1 - num2
        print("Answer: " + str(num3))
    elif choice == 3:
        num3 = num1 * num2
        print("Answer: " + str(num3))
    elif choice == 4:
        num3 = num1 / num2
        print("Answer: " + str(num3))
    elif choice == 5:
        num3 = num1 // num2
        print("Answer: " + str(num3))
    elif choice == 6:
        num3 = num1 ** num2
        print("Answer: " + str(num3))
    elif choice == 7:
        num3 = num1 % num2
        print("Answer: " + str(num3))
    else:
        print("Sorry I do not understand. Please try again.")
        calc()
calc()