#String
empty_string = ' ' #For empty string we can use the single or double quotes. Here we are using single quotes.   
type_of_empty_string = type(empty_string)
print("Type of empty string:", type_of_empty_string)

#It will print Int as a string or a normal text as a string.
int_number = '10' #wrapped in single code
type_of_int_number = type(int_number)
print("Type of int number:", type_of_int_number)
print("Number is:", int_number)

#If we use single quotes for a string, 
#we can wrap the string in double quotes and vice versa.
single_quote_string = "'This is a string wrapped in double quotes.'"
double_quote_string = '"This is a string wrapped in single quotes."'
print("Single quote string:", single_quote_string)
print("Double quote string:", double_quote_string)

# Typecasting example: converting string to int
number = int(int_number)  # Converting string to int
type_of_number = type(number)
print("Type of number after conversion:", type_of_number)
print("Number after conversion:", number)

#Covert floating string to Int is not possible. 
# It will give ValueError. 
# We can convert floating string to float and then to int.   
floating_string = '3.14'  # Floating string
float_number = float(floating_string)  # Converting string to float
type_of_float_number = type(float_number)
print("Type of float number after conversion:", type_of_float_number)
print("Float number after conversion:", float_number)
int_from_float = int(float_number)  # Converting float to int
type_of_int_from_float = type(int_from_float)
print("Type of int from float after conversion:", type_of_int_from_float)
print("Int number after conversion:", int_from_float)

#Interger string can converted to float but the reverse is not possible. It will give ValueError..
int_string = '10'  # Integer string
float_from_int = float(int_string)  # Converting string to float
type_of_float_from_int = type(float_from_int)
print("Type of float from int after conversion:", type_of_float_from_int)
print("Float number after conversion:", float_from_int)

#Typecasting from Float to String
float_number = 3.14  # Float number
string_from_float = str(float_number)  # Converting float to string
type_of_string_from_float = type(string_from_float)
print("Type of string from float after conversion:", type_of_string_from_float)
print("String from float after conversion:", string_from_float)

#Typecasting from Int to String
int_number = 10  # Int number
string_from_int = str(int_number)  # Converting int to string
type_of_string_from_int = type(string_from_int)
print("Type of string from int after conversion:", type_of_string_from_int)
print("String from int after conversion:", string_from_int)

#Boolean Values
a = True
b = False
type_of_a = type(a)
type_of_b = type(b)
print("Type of a:", type_of_a)
print("Type of b:", type_of_b)

#Typecasting from Boolean to String
string_from_a = str(a)  # Converting boolean to string
string_from_b = str(b)  # Converting boolean to string
type_of_string_from_a = type(string_from_a)
type_of_string_from_b = type(string_from_b)
print("Type of string from a after conversion:", type_of_string_from_a)
print("Type of string from b after conversion:", type_of_string_from_b) 
print("String from a after conversion:", string_from_a)
print("String from b after conversion:", string_from_b)

#Typecasting from Bool to Int
# If True it will return 1 and for False it will return 0.
int_from_a = int(a)  # Converting boolean to int
int_from_b = int(b)  # Converting boolean to int
type_of_int_from_a = type(int_from_a)
type_of_int_from_b = type(int_from_b)
print("Type of int from a after conversion:", type_of_int_from_a)
print("Type of int from b after conversion:", type_of_int_from_b)
print("Int from a after conversion:", int_from_a)
print("Int from b after conversion:", int_from_b)

#typecasting from Bool to Float
# If True it will return 1.0 and for False it will return 0.0.
float_from_a = float(a)  # Converting boolean to float
float_from_b = float(b)  # Converting boolean to float
type_of_float_from_a = type(float_from_a)
type_of_float_from_b = type(float_from_b)
print("Type of float from a after conversion:", type_of_float_from_a)
print("Type of float from b after conversion:", type_of_float_from_b)
print("Float from a after conversion:", float_from_a)
print("Float from b after conversion:", float_from_b)

#Any non-zero number is considered True, 
#and zero is considered False.
number1 = bool(123456)
number2 = bool(0)
number3 = bool(-123456)
print("Boolean value of 123456:", number1)
print("Boolean value of 0:", number2)
print("Boolean value of -123456:", number3)

#Non empty strings are considered True, 
#while empty strings are considered False.
non_empty_string = bool("Hello")
empty_string = bool("")
non_empty_string2 = bool(" ")
print("Boolean value of non-empty string 'Hello':", non_empty_string)
print("Boolean value of empty string '':", empty_string)
print("Boolean value of non-empty string with space ' ':", non_empty_string2)

#We can use input function to store user input as string.
user_input = input()
print("User input:", user_input)
user_input_type = type(user_input)
print("Type of user input:", user_input_type)
bid_value = input("Enter your bid value: ")
print("Your bid value is:", bid_value)
bid_value_type = type(bid_value)
print("Type of bid value:", bid_value_type)

print('abc')
print(1, 2, 3)
print(True)

#Nonetype 
a = None
type_of_a = type(a)
print("Type of a:", type_of_a)
#Nonetype is a special type in Python that represents the absence
#of a value or a null value. It is often used to indicate that a 
#variable has no value assigned to it. 
# The NoneType is the type of the None object, 
#which is a singleton in Python.
#Covert NoneType to String
string_from_none = str(a)  # Converting NoneType to string
type_of_string_from_none = type(string_from_none)
print("Type of string from NoneType after conversion:", type_of_string_from_none)
print("String from NoneType after conversion:", string_from_none)
#We can not typecast NoneType to Int or Float. It will give TypeError.
#We can typecast to Bool. It will return False for NoneType.
bool_from_none = bool(a)  # Converting NoneType to boolean
type_of_bool_from_none = type(bool_from_none)
print("Type of boolean from NoneType after conversion:", type_of_bool_from_none)
print("Boolean from NoneType after conversion:", bool_from_none)
#Typecasting a String to NoneType is not possible. 
#It will give TypeError.
#How to typecast a varibale to NoneType. 
#We can assign None to a variable to make it of NoneType.
#The only way to set something to type NoneType is to manually reassign it to None.
