"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""

#Asking for string.
string = str(input("Type what you want: "))
#Iterating through string.
for x in string:
    print(x)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""

#Adding items to list.
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))
num_3 = float(input("Enter a third number: "))
list_of_num = [num_1, num_2, num_3]
#Variable to find sum of list items.
sum_list = 0
#Iterating through list.
for x in list_of_num:
    sum_list = sum_list + x
#Printing sum of list.
print(sum_list)

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""

#Asking for sentence.
sentence = str(input("Enter a sentence: "))
sentence.strip()
#Splitting sentence.
split_sen = sentence.split()
word_length = 0
#Iterating through sentence.
for x in split_sen:
    print(len(x))

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result.

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""

#Stating inventory contents.
inv = {
    "logs" : 1000,
    "gravel" : 987,
    "copper ore" : 357,
    "bronze ingot" : 534,
    "iron ore" : 648,
    "steel ingot" : 159
}
#Printing inventory.
for x in inv:
    print(x)

#Answering excercise 4.
'''
The code outputted every key in order, however it did not print the values 
assigned to each key. I did not expect this output but it makes sense since 
each part of the dictionary seperated by commas has 2 values, therefore python 
just prints the key and does not print the value assigned to the key.
'''