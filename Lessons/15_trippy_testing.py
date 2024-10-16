"""
Exercise 1: Divide
"""

def divide(a, b):
  """Divides two numbers, handling potential division by zero.

  Args:
    a: The numerator.
    b: The denominator.

  Returns:
    The quotient, or None if b is zero.
  """

  if b == 0:
    return None
  else:
    return a / b

#Testing for divide by zero options.
assert divide(5, 0) == None
#Testing for normal division.
assert divide(6, 3) == 2

#Extra Credit:
try:
  assert divide(10, 2) == 7
except:
  print("Check assertion for potential typo.")
else:
  print("This should not run.")


"""
Exercise 2: Factorial
"""

def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

#Testing for 0.
assert factorial(0) == 1
#Testing for any other number.
assert factorial(5) == 120


"""
Exercise 3: String Reverse
"""

def reverse_string(string):
  """Reverses a given string.

  Args:
    string: A string to be reversed.

  Returns:
    The reversed string.
  """

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string

#Testing for string reversal.
assert reverse_string("Apple") == "elppA"
#Testing for full sentence reversal.
assert reverse_string("Hello, my name is...") == "...si eman ym ,olleH"


"""
Exercise 4: Fibonacci
"""
def fibonacci(n):
  """Generates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

#Testing for 10th (technically 11th) number in Fibonacci Sequence.
assert fibonacci(10) == 55
#Testing for 4th (technically 5th) number in Fibonacci Sequence.
assert fibonacci(4) == 3


"""
Exercise 5: Email Validation
"""

import re

def is_valid_email(email):
  """Determines whether email is valid or not

  Args:
    email: The email to validate

  Returns:
    Boolean value if email is valid
  """
  email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+"
  return re.match(email_regex, email) is not None

#Testing for email validity.
assert is_valid_email("hasainjinan11@gmail.com") == True
#Testing for non-email.
assert is_valid_email("imnotyou") == False