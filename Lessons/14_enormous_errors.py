"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""

"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    result = num1 / num2
    print("Result:", result)

# Example usage:
try:
    divide_numbers(10, 0)
except: #Runs if number is 0.
    print("The second number is 0 so I cannot perform division.")

"""
Example 2: Opening Files
"""

def read_file(filename):
    file = open(filename, 'r')
    contents = file.read()
    print("File contents:", contents)
    file.close()

# Example usage:
try:
    read_file("nonexistent.txt")
except: #Runs if no file argument is defined or file does not exist.
    print("No file to read or file does not exist.")

"""
Example 3: List Items
"""

def get_item(lst, index):
    item = lst[index]
    print("Item:", item)

# Example usage:
my_list = [1, 2, 3]
try:
    get_item(my_list, 5)
except: #Runs if list does not exist or index is out of range.
    print("List does not exist or index is out of range.")

"""
Example 4: Dictionaries
"""

def get_value(dictionary, key):
    value = dictionary[key]
    print("Value:", value)

# Example usage:
my_dict = {"a": 1, "b": 2}
try:
    get_value(my_dict, "c")
except: #Runs if dictionart or requested key does not exist.
    print("Dictionary or key does not exist.")

"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError: #Runs if file does not exist.
        print("Error: File not found.")
    else: #Runs if file exists and is found.
        print("File retrieved without any errors.")
    finally: #Runs regardless of errors encountered or not.
        print("Action ended.")

# Example usage:
process_file("example.txt")