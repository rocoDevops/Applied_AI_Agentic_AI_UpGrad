#Conditional Statements in Python
#Looping Statements in Python
#Problem Statements in Python
#Decision Making in Python
#if-else key word for the decision making
age = int(input("Enter your age: "))
name = input("Enter your name: ")
if age >= 18:
    print(f"{name}, you are eligible to vote.") #indent represents the block of code that will be executed if the condition is true
else:
    print(f"{name}, you are not eligible to vote.") #indent represents the block of code that will be executed if the condition is false    

#Multipel conditions using elif keyword
rank = 7
if rank == 1:
    print("You are in the first position.")
elif rank == 2:
    print("You are in the second position.")
elif rank == 3:
    print("You are in the third position.")
else:
    print("You are not in the top three positions.")

#Ask the user to Enter a Number. Write logic or condition to determine is the number is Postitive, Negetive or Neutal.
enter_number = int(input("Enter a number: "))
if enter_number > 0:
    print("The number is Positive.")
elif enter_number < 0:
    print("The number is Negative.")
else:
    print("The number is Neutral (Zero).")

#Ask the user to provide Balance, Withdrawl Amount and Write logic / condition to check  
#if withdrawl Amount < 0 Print invalid amount
#if balance < withdrawl amount print 'Insufficiemnt Balance'
#if balance > withdrawl amount print 'Withdrawl Approved'
balance  = float(input("Enter your balance: "))
withdrawl_amount = float(input("Enter the withdrawl amount: "))
if withdrawl_amount < 0:
    print("Invalid amount")
elif balance < withdrawl_amount:
    print("Insufficient Balance")
else:
    print("Withdrawl Approved")

#Simulating employee payroll
#Ask the employee to enter basic pay
#If basic pay >= 5000
#the calculate HRA as 10% of basicpay and DA as 12% of Basicpay
#if basicpay < 5000
#then calculate HRA as 14% of basicpay and DA as 16% of basicpay
#Find Grosspay i.e Sum of Basicpay+HRA+DA
#Print the Salary details
basic_pay = float(input("Enter your basic pay: "))
if basic_pay >= 5000:
    hra = 0.10 * basic_pay
    da = 0.12 * basic_pay
else:
    hra = 0.14 *basic_pay
    da = 0.16 * basic_pay
gross_pay = basic_pay + hra + da
print(f"Basic Pay: {basic_pay}")
print(f"HRA: {hra}")
print(f"DA: {da}")
print(f"Gross Pay: {gross_pay}")

basicPay = int (input('enter basic Pay '))

if basicPay >= 5000 :
  HRA = basicPay * .1
  DA  = basicPay * .12

else:
  HRA = basicPay * .14
  DA  = basicPay * .16

grossPay = HRA + DA + basicPay

salarySlip=f'''
===========================================
================Salary Slip================
===========================================

Basic (💵) :   {basicPay}
HRA   (💶) :   {round(HRA,2)}
DA    (💷):   {round(DA,2)}
=====================
GROSS (💸):   {grossPay}
'''
print(salarySlip)

#Using logical operator 
attendance = int(input("Please enter your attendance percentage: "))
fees_paid = input('fees paid yes/no: ')
if fees_paid not in ('yes', 'no'):
  print(f'Invalid Choice')
else:
  if attendance >= 75 and fees_paid == 'yes':
    print('Eligible for exam. ')
  else:
    print('Not Eligible for exam. ')
#Using OR operator
attendance = int(input("Please enter your attendance percentage: "))
fees_paid = input('fees paid yes/no: ')
if fees_paid not in ('yes', 'no'):
  print(f'Invalid Choice')
else:
  if attendance >= 75 or fees_paid == 'yes':
    print('Eligible for exam. ')
  else:
    print('Not Eligible for exam. ')
'''
ECommerce Free Delivery ( AND + OR )
Problem:

AN online store gives free delivery when :

order amount is 1000 or more OR
customer is premium AND order is > 500
ask

amount
premium(yes/no)
'''
amount = float(input("Enter the order amount: "))
premium = input("Are you a premium customer (yes/no): ")
if premium not in ('yes', 'no'):
    print("Invalid Choice")
else:
    if amount >= 1000 or (premium == 'yes' and amount > 500):
        print("You are eligible for free delivery.")
    else:
        print("You are not eligible for free delivery.")

#Loops in Python
# looping is used for solving problems that are repetitive in nature.
#Python provides two types of loops:
#1. for loop
#2. while loop
meter = int(input("Enter the initial meter value: "))
if meter <= 5:
    print(f"Starting meter readings...")
    while meter <= 5:
        print(f"Meter reading {meter}")
        meter += 1
    print(f"Meter readings completed.")
else:
    print(f"Meter readings not started as initial meter value is greater than 5.")  
#print 10 to 1 using while loop
meter = 10
while meter >= 1:
        print(f"Meter reading {meter}")
        meter -= 1
print(f"Meter readings completed.")

#Sum of all numbers entered by the user (3 numbers)
meter = 1 
sum_numbers = 0 # Initialize the sum of numbers to 0
while meter <= 3: 
  num = int(input("Input any number: ")) 
  print(num) 
  sum_numbers += num
  meter = meter + 1 
print(f"Sum of all numbers {sum_numbers}. ")

'''
in a Survey , data about people's number of members in a family were collected.

the data is noisy/have some issues , you are asked to find the count of valid data points.

any datapoint <=0 is Invalid.

(3 , 2 , -5 , 6 , 4 , -2 , -6 , 8 )
'''
count = 0
for i in (3 , 2 , -5 , 6 , 4 , -2 , -6 , 8 ):
    if i <= 0:
        print(f"Invalid data point: {i}")
    else:
        print(f"Valid data point: {i}")
        count += 1
print(f"Count of valid data points: {count}")

#Even or Odd: Ask the user for a number and print whether it's even or odd.
number = int(input('Please enter a number: '))
if number%2 == 0:
  print(f'Entered number is Even number {number}')
else:
  print(f'Entered number is Odd number {number}')
#Largest of Three: Ask the user for three numbers and print the largest among them.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
if (num1 > num2) and (num1 > num3):
  print(f'Largest number is {num1}')
elif (num2 > num3) and (num2 > num1):
  print(f'Largest number is {num2}')
else:
  print(f'Largest number is {num3}')

'''
Grade Calculator: Ask for marks (0–100) and print the grade:

>= 90: A
>= 75: B
>= 50: C
below 50: Fail
'''
marks = int(input('Enter Marks: '))
if (marks >= 90):
  print(f'A')
elif (marks >= 75):
  print(f'B')
elif (marks >= 50):
  print(f'C')
else:
  print(f'Fail')
'''
Leap Year Check: Ask for a year and determine if it's a leap year.

(Rule: divisible by 4, but not by 100 unless also divisible by 400)
'''
year = int(input('Enter the year: '))
if ((year % 4 == 100) and (year % 100 != 0)) or (year % 4 == 0):
  print(f'{year} is leap year. ')
else:
  print(f'{year} is not leap year. ')
#Ticket Pricing: Ask for age. If age < 5, ticket is free. If age <= 12, ticket is $10. Otherwise, ticket is $20.
age_of_person = int(input('Please enter your age: '))
if age_of_person < 5:
  print(f'Ticket is free. ')
elif age_of_person <= 12:
  print(f'Ticket is $10. ')
else:
  print(f'Ticket is $20. ')
'''
Triangle Validity: Ask for three side lengths. 
Determine if they can form a valid triangle (sum of any two sides must be greater than the third),
and if valid, classify it as Equilateral, Isosceles, or Scalene.
'''
side1 = float(input('Enter the length of the first side: '))
side2 = float(input('Enter the length of the second side: '))
side3 = float(input('Enter the length of the third side: '))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    if side1 == side2 == side3:
        print('The triangle is Equilateral.')
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print('The triangle is Isosceles.')
    else:
        print('The triangle is Scalene.')
else:
    print('The sides do not form a valid triangle.')
'''
Login System: Ask for a username and password. Check against stored credentials (hardcode admin/1234). 
Print "Access Granted" or "Access Denied" — but also handle the case of empty input as "Invalid Input".
'''
username = input('Enter username: ')
password = input('Enter password: ')

if not username or not password:
    print('Invalid Input')
elif username == 'admin' and password == '1234':
    print('Access Granted')
else:
    print('Access Denied')
'''
Electricity Bill: Ask for units consumed and calculate the bill:

First 100 units: $1/unit
Next 100 units (101–200): $1.5/unit
Above 200 units: $2/unit
(Hint: this needs cumulative calculation based on slabs, not just a single condition.)
'''
unit = float(input('Units Consumed: '))
if unit <= 100:
  bill_1 = unit * 1
  print('Bill is: ', bill_1)
elif unit <=200:
  bill_2 = (unit - 100) * 1.5 + 100 * 1
  print('Bill is: ', bill_2)
else:
  bill_3 = ((unit - 200) * 2) + (100 * 1.5) + (100 * 1)
  print('Bill is: ', bill_3)

'''
BMI Categorizer: Ask for weight (kg) and height (m). 
Calculate BMI = weight / height². Classify as Underweight (<18.5), Normal (18.5–24.9), Overweight (25–29.9), or Obese (>=30).
'''
weight = float(input('Enter your weight (kg): '))
height = float(input('Enter your height (m): '))

bmi = weight / (height ** 2)
if bmi < 18.5:
    print('Underweight')
elif 18.5 <= bmi <= 24.9:
    print('Normal')
elif 25 <= bmi <= 29.9:
    print('Overweight')
else:
    print('Obese')
print(f'Your BMI is: {bmi:.2f}')

'''
Discount Voucher Logic: Ask for purchase amount and a voucher code (SAVE10, SAVE20, or NONE). 
Apply discount only if the voucher is valid AND purchase amount is above $500; otherwise no discount, and print an appropriate message for invalid vouchers.
'''
amount = float(input('please enter purchase amount: '))
voucher_code = input('Enter voucher code SAVE10, SAVE20, NONE: ')
if voucher_code not in ('SAVE10', 'SAVE20', 'NONE'):
  print('Invalid Voucher Code. ')
elif amount > 500 and voucher_code in ('SAVE10', 'SAVE20'):
  print('Discount Applied. ')
else:
  print('No Discount. ')