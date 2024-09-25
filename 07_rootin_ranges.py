"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""

#Iterating through loop.
for x in range(1, 11):
    print(x)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""

#Iterating through loop.
for x in range(900, 1001, 10):
    print(x)

"""
Exercise 3:
Write a program that counts from 1-100 by 9
"""

#Iterating through loop.
for x in range(1, 101, 9):
    print(x)

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""

#Variables.
total = 0
#Iterating through loop.
for x in range(1, 11):
    total = total + x
print(total)

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5

for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()

'''
The code outputs asterisks, where the number of asterisks each line increments by one each iteration.

"rows" is set to 5. the for loop containing i repeats itself 5 times, which is why there are 5 iterations of asterisks.
The loop containing j simply states "print i + 1 asterisks each time this code is run." Since i starts at 0, the initial
iteration prints one asterisk. With each iteration, the number of asterisks printed increases by 1 each time until the
i loop has run 5 times.
'''