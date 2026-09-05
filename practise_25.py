#Formula for Area of a Triangle: Area = 1/2 * base * height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
print("Area of Triangle:", 0.5 * base * height)
#Write a Python program to take two integers x and y as input from a user and solve the following expression: (x^y+(x+y)^(x-y)) 
x = int(input("Enter the first integer (x): "))
y = int(input("Enter the second integer (y): "))
result = (x**y)+ ((x+y)**(x-y))
print("Result:", result)
#Write a Python program to take temperature in Celsius as input from the user and convert 
#it into Fahrenheit. The formula for conversion is: Fahrenheit = (Celsius * 9/5) + 32
Temperature_in_celcius = float(input("Enter the temperature in Celsius: "))
Fahrenheit = (Temperature_in_celcius * 9/5) + 32
print("Temperature in Fahrenheit:", Fahrenheit)
#Write a Python program to take base salary and bonus amount as input from the user and check 
#if the salary with bonus is greater than 50,000 and bonus amount is greater than 5,000. 
#The program should return True if both conditions are met, otherwise it should return False.
base_salary = float(input("Enter the base salary: "))
bonus_amount = float(input("Enter the bonus amount: "))
salary_with_bonus = base_salary + bonus_amount
print("Salary with bonus is greater than 50,000 and bonus amount is greater than 5,000.", bool(salary_with_bonus > 50000 and bonus_amount > 5000 ))
#Write a program that takes two variables representing a person's first name and last name, and prints the full name in the format "Last, First".
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
full_name = f"{last_name}, {first_name}"
print("Full name:", full_name)
#30 minutes to second
seconds = 30 * 60
print("30 minutes in seconds:", seconds)
