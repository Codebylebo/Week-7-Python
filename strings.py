#Strings

messages = """Bob's birthday is on 5th May, 
and he is 30 years old."""

print(messages)

# Using triple quotes allows for multi-line strings
# You can also use single or double quotes for single-line strings
single_line_message = 'Hello, Bob!'
double_line_message = "Hello, Bob!"
print(single_line_message)
print(double_line_message)

# Advanced concepts - Strings

message = "Hello, Bob!"

print(message[0])  # First character
print(message[1])  # Second character

print(message[-1])  # Last character


print(len(message))  # Length of the string
print(message[0:5])  # Slicing - first 5 characters

#wide space
message = "Hello, Bob!  "
print(len(message))  # Prints with trailing spaces

# Strips
message = " Hello, Bob "
print((message.strip()))  # Removes leading and trailing whitespaces
print(message.lower())  # Converts all characters to lowercase
print(message.upper())  # Converts all characters to uppercase
print(message.replace("Bob", "Alice"))  # Replaces 'Bob' with 'Alice'
print(message.split(","))  # Splits the string into a list based on the comma

#Numeric data
num = 3
print(3)

#Numeric types
num = 3
print(type(num))  # Prints the type of num, which is int
num2 = 3.14
print(type(num2)) # Prints the type of num, which is float

# Variables
# Variables are used to store data. They have to start with a letter or underscore,
# therefore, they cannot start with a number or special character.
# Variables can contain letters, numbers, and underscores.
# They are case-sensitive, meaning 'num' and 'Num' are different variables.

# valid variables
my_variable = 5
total_amount = 100
user = 'Alice'

# invalid variables
#2nd_variable = 10  # Cannot start with a number
    #therefore use an actual word:
second_variable = 10  # Valid variable name

#user-name = 'Alice'  # Cannot contain special characters like '-'
    #therefore use an underscore:
user_name = 'Alice'  # Valid variable name


#Operators

# Arithmetic Operators:
# + (Addition)
# - (Subtraction)
# * (Multiplication)
# / (Division)
# % (Modulus)
# ** (Exponentiation)
# // (Floor Division)

# Example:
a = 10
b = 3

print(a + b)  # Addition
print(a - b)  # Subtraction 
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b)  # Exponentiation
print(a // b)  # Floor Division #rounds down to the nearest whole number

#assignment operators
# = (Assignment)
# += (Add and assign)
# -= (Subtract and assign)
# *= (Multiply and assign)
# /= (Divide and assign)
# %= (Modulus and assign)
# **= (Exponentiation and assign)
# //= (Floor division and assign) 
  
# Example:
x = 5
x = x + 2  # Equivalent to x += 2

print(x)  # Prints 7


#Operators with strings
# Concatenation:
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # Concatenates str1 and str2 with a space in between
# Repetition:
print(str1 * 3)  # Repeats str1 three times. uses multiplication operator for strings
#equivalent to:
print(str1 + " " + str1 + " " + str1)  # Concatenates str1 three times with spaces

# Conrol statements

# Control statements are used to control the flow of the program.
# They include conditional statements (if, elif, else) and loops (for, while).
# Conditional Statements:
# if (condition):
#     # code to execute if condition is true
# elif (condition):
#     # code to execute if the first condition is false and this condition is true
# else:
#     # code to execute if all previous conditions are false

# Example:
num = 10
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
elif num == 0:
    print("The number is zero.")
# Example with multiple conditions
    
num2 = -5
if num2 == 0:
    print("The number is zero.")
elif num2 < 0:
    print("The number is negative.")
elif num2 > 0:
    print("The number is positive.")
else:
    print("The number is neither positive nor negative.")
# Example with zero
# This will check if the number is zero, positive, or negative
    
num3 = 0
if num3 > 0:
    print("The number is positive.")
elif num3 == 0:
    print("The number is zero.")
elif num3 < 0:
    print("The number is negative.")
else:
    print("The number is either zero.")
    
# Control statements

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)
    
# Loops:
# for loop:
# for variable in iterable:
#     # code to execute for each item in the iterable
# Example:
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# while loop:
# while (condition):
#     # code to execute as long as the condition is true
# Example:
#using a while loop to count from 1 to 5
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1 #increment the count by 1
    
# Loops Continued:
#break, continue and pass statements
# break: Exits the loop immediately
# continue: Skips the current iteration and continues with the next iteration
# pass: Does nothing, acts as a placeholder

#for loop with break, continue, and pass
# Examples:
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "cherry":
        break  # Exits the loop when fruit is "cherry"
    print(fruit)

print()

for fruit in fruits:
    if fruit == "cherry":
        continue # Skips the iteration when fruit is "cherry"
    print(fruit)

print()

for fruit in fruits:
    if fruit == "date":
        pass  # Does nothing, acts as a placeholder. No action is needed for "date", no effect on the loop
    print(fruit)
    
# While loop with break, continue, and pass
# Examples:
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
    if count == 3:
        break  # Exits the loop when count is 3/ reaches 3

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue    # Skips the iteration when count is 3
    print("Count is:", count)

count = 0
while count < 5:
    count += 1 
    if count == 3:
        pass  # Does nothing, acts as a placeholder
    print("Count is:", count)
