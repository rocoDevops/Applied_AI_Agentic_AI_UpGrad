#Repetative Task we do in Python
# a = 10
# b = 20
# print("Sum:", a + b)

# c = 30
# d = 40
# print("Sum:", c + d)

# print("\nAbove code repeats logic \n")

#Using Function to avoid repetitive code
#A function is a block of code which only runs when it is called. You can pass data,
#known as parameters, into a function. A function can return data as a result.
#Advantages of using functions:
# - Reuse code without repeating the same logic
# - Improve readability and organization
# - Make debugging easier by isolating behavior
# - Allow inputs (parameters) and outputs (return values)
# - Support modular design and easier maintenance
#Addition, Subtraction, Multiplication, Division of two numbers using function
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

subtraction = subtract(20, 1.42)
print("Subtract:", subtraction)
addition = add(30, 40)
print("Addition:", addition)
product = multiply(30, 40)
print("Multiplication:", product)
quotient = divide(30, 40)
print("Division:", quotient)

# We can reuse the stored `addition` variable value later in another calculation.
bonus = addition + 100
print("Addition plus bonus:", bonus)
print("Original stored addition value reused:", addition)

# This code prints results directly and does not return values.
def print_sum(a, b):
    print("Sum:", a + b)

def print_difference(a, b):
    print("Difference:", a - b)

print("\nSeparate print-only example:")
print_sum(10, 5)
print_difference(10, 5)

def power(num1 , num2):
    print("Power:", num1 ** num2)
power(2, 3)

# Write a code where input can be a different data type and output can be a different data type.
# This function takes a number (int or float) as input and returns a string as output.
def convert_to_string(num):
    result = "Number is " + str(num)
    return result

# Call the function with different input types and print the returned string. 
# It will return int and float as string or normal text as string.
converted_int = convert_to_string(25)
print("Converted int:", converted_int)

converted_float = convert_to_string(3.14)
print("Converted float:", converted_float)

string_input = convert_to_string("Hello")
print("Converted string:", string_input)

# Simple interest example: input is numeric values, output is two values (interest and final amount).
def simple_interest(principal, time, rate):
    interest = (principal * time * rate) / 100
    final_amount = principal + interest
    return interest, final_amount

interest_value, total_amount = simple_interest(60000, 5, 12)
print("Interest:", interest_value)
print("Final amount:", total_amount)

def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

circle_area = calculate_area(5)
print("Area of the circle:", circle_area)

