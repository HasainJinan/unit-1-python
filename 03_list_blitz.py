"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""

#Creating list.
moves = ["dodge", "run", "attack", "block"]
#Printint list.
print(moves)

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

#Adding to list.
moves.append("item")
#Printing updated list.
print(moves)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""

#Removing specific item.
moves.remove("run")
#Printing updated list.
print(moves)


"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

#Modifying list item.
moves[0] = "evade"
#Printing updated list.
print(moves)

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""

#Appending moves to list.
new_moves = ["skip", "talk", "leave"]
for x in new_moves:
    moves.append(x)
#Printing updated list.
print(moves)

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""

#Removing specific move.
del moves[5]
#Printing updated list.
print(moves)

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""

#Creating variable.
partial_moves = moves[0:2]
#Printing variable.
print(partial_moves)

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

#New list.
list_2 = ["save", "reset"]
#Extending list.
new_list = moves + list_2
#Printing list.
print(new_list)