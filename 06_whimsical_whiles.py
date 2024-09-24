"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""

#Starting variable.
x = 1
#While loop.
while x <= 10:
    print(x)
    x += 1

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""

#Starting variable.
i = 11
#While loop.
while i > 1:
    i -= 1
    print(i)

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""

#Factorial number.
fac = int(input("Enter a number: "))
fac_num = int(fac)
#Factorial calculation.
while fac > 1:
    fac -= 1
    fac_num = fac_num * fac
#Printing factorial number.
print(fac_num)

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""

print("Guess the password.")
#Asking for password.
guess = str(input("Guess: "))
#Checking password guess.
while guess != "forlenza44":
    print("Incorrect. Try again.")
    guess = str(input("Guess: "))
else:
    print("Correct.")

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""

#Enter number.
num = int(input("Enter integer number: "))
#Variables.
dig = 0
total = 0
#For loop.
for dig in str(num):
    total += int(dig)
#Printing sum.
print("The sum of digits is " + str(total) + ".")

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

#Variables.
n = int(input("How many numbers of the Fibonacci Sequence do you want to print: "))
counter = 1
num1 = 0
num2 = 1
#Fibonacci loop.
print("1")
while counter < n:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3)
    counter += 1