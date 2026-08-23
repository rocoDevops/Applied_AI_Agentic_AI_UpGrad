#In summary, the most commonly used operators in Python are as follows:
# Arithmetic operators -> It helps to perform mathematical operations like addition, subtraction, multiplication, division, etc.
# Assignment operators -> It helps to assign values to variables.
# Comparison operators -> It helps to compare values and return a boolean result (True or False).
# Logical operators -> It helps to perform logical operations like AND, OR, NOT.
# Membership operators -> It helps to check if a value is present in a sequence (like list, tuple, string).

#Arithmetic Operators
a = 10 + 12
b = a - 5
c = b * 2
d = c / 3
print("Value of a:", a)
print("Value of b:", b)
print("Value of c:", c)
print("Value of d:", d) 
#Exponential operator
e = 2 ** 3 #2 raised to the power 3 is 8
print("Value of e:", e)
#Floor division operator
f = 10 // 3 #Floor Value is 3.33 but it will return 3
print("Value of f:", f)
#Remainder operator 
g = 10 % 3 #Remainder is 1
print("Value of g:", g)
#Modulus operator
h = 10 % 3 #Modulus operator returns the remainder of the division of the left operand by the right operand.
print("Value of h:", h)

#Oprator Overloading
#In Python, operator overloading allows us to define the behavior of operators for user-defined classes
#String concatenation using + operator
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2 + '!' # Concatenating strings using the + operator
print("Concatenated string:", result)

#Arithmetic operations for boolean values
bool1 = True
bool2 = False
sum_result = bool1 + bool2  # True is treated as 1 and False as 0, so the sum is 1
print("Sum of boolean values:", sum_result)
bool3 = False
bool4 = False
sum_result2 = bool3 + bool4  # Both are False, so the sum is 0
print("Sum of boolean values:", sum_result2)
bool5 = False
bool6 = True
sum_result3 = bool5 + bool6  # False is treated as 0 and True
print("Sum of boolean values:", sum_result3)

a1 = 1 + 3 * 4 / 12 - 6
print("Value of a1:", a1)
a3 = 3 ** 4 // 5 % 3
print("Value of a3:", a3)

a5 = 'Python'
b6 = 'Programming'
print(a5 + b6 * 3)

#Operator Precedence
#Operator precedence determines the order in which operators are evaluated in an expression.
#In Python, the order of precedence is as follows:
# Parentheses ()
# Exponentiation **
# Multiplication *, Division /, Floor Division //, Modulus %
# Addition +, Subtraction - 

#Taking user name and age as an input
name = input('Enter your name: ')
age = input('Enter your age: ')
type_of_age = type(age)
print("Type of age:", type_of_age)
print("Hello, " + name + "! You are " + age + " years old.")
age_after_six_years = int(age) + 6
print("In 6 years, you will be " + str(age_after_six_years) + " years old.")
#String concatenation is possbile but not addition of string and integer. 
#We need to convert the integer to string before concatenation.
print("Hello", input("Enter your name: ") + "! You are " +str(int(input("Enter your age: ")) + 6) + " years old in 6 years.")

#If user input something it should be True else False
user_input = input("Enter something! ")
print("Did user enter something?", bool(user_input))  # True if user entered something, False if empty

#Take user age as float and convert it to years, months and days
age = float(input("Enter your age in years : "))
age_in_years = int(age)
age_in_months = int((age - age_in_years) * 12)
age_in_days = int((age - age_in_years - (age_in_months / 12)) * 365)
print(f"Your age is {age_in_years} years, {age_in_months} months, and {age_in_days} days.")

#Assignment Operators
a = b = 10
c, d, e = 11, 2.0, True
print("Value of a:", a)
print("Value of b:", b)
print("Value of c:", c)
print("Value of d:", d)
print("Value of e:", e)
b +=5
print("Value of b after +=5:", b)
b +=b
print("Value of b after +=b:", b)
a = a-3
print("Value of a after a-3:", a)
b -=b
print("Value of b after b-b:", b)
b = 15
b *=2
print("Value of b after b*2:", b)
b /=3
print("Value of b after b/3:", b)
type_of_b = type(b)
print("Type of b after b/3:", type_of_b)
type_of_a = type(a)
print("Type of a after a-3:", type_of_a)
b **=2 #Exponentiation assignment operator. It raises the value of b to the power of 2 
#and assigns the result back to b.    
print("Value of b after b**2:", b)
b //=3 #Floor division assignment operator. 
#It performs floor division of b by 3 and assigns the result back to b.
print("Value of b after b//3:", b)
b %=4 #Modulus assignment operator. 
#It calculates the remainder of b divided by 4
print("Value of b after b%4:", b)
a = 5
a += 1
print("Value of a after a+=1:", a)
a **= 2
print("Value of a after a**=2:", a)
a //= 3
print("Value of a after a//=3:", a)
a *= 0.5
print("Value of a after a*=0.5:", a)
print("Final value of a after multiple operations:", a)
a = 'abc'
user_input = input('Please input a number greater than 100: ')
a += user_input
print(a)
#Comparison Operators
1 == 1
print("Is 1 equal to 1?", 1 == 1)  # True
True == False
print("Is True equal to False?", True == False)  # False
"abc" == 'abc'
print("Is 'abc' equal to 'abc'?", "abc" == 'abc')  # True
5 != 3
print("Is 5 not equal to 3?", 5 != 3)  #
1 != 1
print("Is 1 not equal to 1?", 1 != 1)  # False
True != False
print("Is True not equal to False?", True != False)  # True
"abc" != 'abc'
print("Is 'abc' not equal to 'abc'?", "abc" != 'abc')  # False
"abc" != "abcd"
print("Is 'abc' not equal to 'abcd'?", "abc" != "abcd")  # True
1 < 5
print("Is 1 less than 5?", 1 < 5)  # True
100 < 4
print("Is 100 less than 4?", 100 < 4)  # False
5 < 5
print("Is 5 less than 5?", 5 < 5)  # False
1 > 2.0
print("Is 1 greater than 2.0?", 1 > 2.0)  # False
1 < 2.0
print("Is 1 less than 2.0?", 1 < 2.0)  # True
#Logical Operators
#and or & not is logical operators. 
#They are used to combine conditional statements.
#AND
True and False
print("True and False:", True and False)  # False
5 > 4 and 3 < 4
print("5 > 4 and 3 < 4:", 5 > 4 and 3 < 4)  # True
x = 5
x > 4 and x < 10
print("x > 4 and x < 10:", x > 4 and x < 10)  # True
x != 3 and x >=10
print("x != 3 and x >=10:", x != 3 and x >=10)  # False
#OR
True or False
print("True or False:", True or False)  # True
5 > 4 or 3 < 4
print("5 > 4 or 3 < 4:", 5 > 4 or 3 < 4)  # True
#NOT 
not True
print("not True:", not True)  # False
not False
print("not False:", not False)  # True
5 > 4 and not 3 < 4 #Logical operators can be combined with comparison operators to 
#create more complex conditions. Here and not 
print("5 > 4 and not 3 < 4:", 5 > 4 and not 3 < 4) #False
#Operator Precedence
#NOT --> AND --> OR
(1 < 2 or 2 < 3) and 3 > 4
print ("Will return the Value: ", (1 < 2 or 2 < 3) and 3 > 4)
not True or True
print ("Print the ouput of the expression: ", not True or True)
print (3 > 2 and (2 < 3 or 4 > 5) and not True)
#Truthiness and Falsiness
#The blank string is not equal to false but it is falsy.
print(bool(''))
print("Expression Empty String: ", '' == False)
#Non Empty string are not equal to truthy
print(bool('abc'))
print("Non-Empty String: ", 'abc' == True)
#Integer Zero is equal to False
# Non-empty strings are truthy, so the `and` expression returns the second value.
name = "Chandan"
greeting = name and "Hello " + name
print("Greeting:", greeting)

# An empty string is falsy, so the `or` expression returns the fallback value.
user_name = ""
display_name = user_name or "Guest"
print("Display name:", display_name)

# Zero is falsy, while a non-zero number is truthy.
user_score = 0
score_message = user_score or "No score available"
print("Score message:", score_message)








