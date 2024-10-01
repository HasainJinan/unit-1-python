#Exercise 1.
#Initial text and count.
text = "Hello, world, my name is"
count = 0
#Loop through the string to count spaces.
for char in text:
    if char == " ":
       count += 1
#Print number of spaces.
print(count)

#Exercise 2.
#Asks for a number.
print("give me a number")
n = int(input())
#Considers each number in a range from 1 to n + 1 and decides if it's even or odd.
for num in range(1, n + 1):
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")

#Exercise 3.
#Asks for an integer.
num = int(input("Enter an integer: "))
#Finds factorial of the number while barring negative numbers.
if num < 0:
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num + 1):
    result *= i   
#Prints the factorial. 
print("Factorial of", num, "is", result)

#Exercise 4.
#Correct password and initial attempt count.
attempts = 0
correct_password = "secret"
#Infinte loop to continuously ask for password as long as password is incorrect and you have less than 3 attempts.
while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:
        print("Correct password!")
        break
    else:
        print("Incorrect password")

    if attempts > 2:
        print("Too many attempts")
        break