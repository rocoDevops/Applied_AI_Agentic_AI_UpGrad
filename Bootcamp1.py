#Todays Agenda:
# 1. Environment Setup
# 2. Writing & Running Python Codes
# 3. Understanding the Importance of Grammer/Syntax
# 4. Python DataTypes & Variables
# 5. Input/Output
# 6. Decision Making.
# ....(many more)
item = 'clock'
day = 'yesterday'
impact = 'time consuming'
print(f'i ate a {item} {day} , it was very {impact}')

farenheit = input("Enter the temperature in Fahrenheit: ")
celsius = (float(farenheit) - 32) * 5/9
print("Temperature in Celsius:", celsius)


salary = float(input("Enter your salary: "))
increment_salary = salary * 0.3
tds = increment_salary * 0.1
final_salary = increment_salary - tds
print(f"old salary: {salary}")
print(f"Salary after increment and TDS deduction: {final_salary}")
print(f"Final Payable Salary: {final_salary + salary}")

#Pizza Order Program
number_of_pizzas = int(input("Enter the number of pizzas you want to order: "))
price_of_pizza = float(input("Enter the price of a single pizza: "))
number_of_colddrinks = int(input("Enter the number of cold drinks you want to order: "))
price_of_colddrink = float(input("Enter the price of a single cold drink: "))
delivery_charge = float(input("Enter the delivery charge: "))

pizza_cost = number_of_pizzas * price_of_pizza
colddrink_cost = number_of_colddrinks * price_of_colddrink
delivery_cost = delivery_charge
print(f"Cost of pizzas: {pizza_cost} , Cost of cold drinks: {colddrink_cost} , Delivery charge: {delivery_cost}")
total_cost = (number_of_pizzas * price_of_pizza) + (number_of_colddrinks * price_of_colddrink) + delivery_charge
print(f"Total cost of your order is: {total_cost}")

#Arithmetic Assignment Operators
x = 10
x += 5  # Equivalent to x = x + 5
print("After += 5, x =", x)
x -= 3  # Equivalent to x = x - 3
print("After -= 3, x =", x)
x *= 2  # Equivalent to x = x * 2
print("After *= 2, x =", x)
x /= 4  # Equivalent to x = x / 4
print("After /= 4, x =", x)
x %= 3  # Equivalent to x = x % 3
print("After %= 3, x =", x)
x **= 2  # Equivalent to x = x ** 2
print("After **= 2, x =", x)    