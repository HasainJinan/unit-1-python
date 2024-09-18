"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive
"""

#Password Function
def check() :
    #Ask for password.
    guess = str(input("Enter Password: "))
    #Check Password.
    if guess.lower() == "formatting":
        print("Correct.")
    else:
        print("Incorrect.")
        check()
#Running function.
check()

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""

#Ask for value.
value = str(input("Enter an actual value: "))
#Check for actual value.
if value.strip() == "":
    print("Invalid")
else:
    print("Valid")

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""

#Template sentence.
sentence = "I love cats. In fact, I have a cat named Cat. Cat is funny because they always sleep like a cartoon character."
#Make sentence lowercase.
sentence = sentence.lower()
#Replace words.
sentence = sentence.replace("cat", "dog")
#Print.
print(sentence)

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""

#Input.
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
#Replace.
fact = f"Your name is {name}. Your age is {age}."
#Print.
print(fact)

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""

#Float inputs.
flt_1  = float(input("Enter a decimal number: "))
flt_2  = float(input("Enter another decimal number: "))
#Division.
quo = flt_1 / flt_2
#Rounding.
answer = f"The quotient is {quo:.1f}."
#Print.
print(answer)