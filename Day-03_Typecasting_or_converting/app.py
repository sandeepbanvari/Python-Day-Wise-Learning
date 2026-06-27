'''
Typecasting or converting is the process of converting one data type to another data type.
In Python, we can use the following built-in functions for typecasting:
1. int() - to convert a value to an integer
2. float() - to convert a value to a floating-point number
3. complex() - to convert a value to a complex number
4. str() - to convert a value to a string
5. bool() - to convert a value to a boolean
6. list() - to convert a value to a list
7. tuple() - to convert a value to a tuple
8. set() - to convert a value to a set
9. dict() - to convert a value to a dictionary
'''

'''
Types of Typecasting:
1. Implicit Typecasting
    -- Implicit typecasting is the automatic conversion of one data type to another data type by the Python interpreter.
    -- It happens when we perform an operation between two different data types, and Python automatically converts one of
       the data types to the other data type to perform the operation.
2. Explicit Typecasting
    -- Explicit typecasting is the manual conversion of one data type to another data type by the programmer using built-in functions.
    -- It is done when we want to convert a value from one data type to another data type explicitly.
'''


# Example of typecasting

a = 10
b = 3.14
# c = "Hello"
c = "123"  # This will work for typecasting to int and float
d = True
e = 10+5j

# Checking the data types of the variables
print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'str'>
print(type(d))  # Output: <class 'bool'>
print(type(e))  # Output: <class 'complex'>



# Typecasting of variable "a" to other data types
print(float(a))  # Output: 10.0
print(str(a))  # Output: '10'
print(bool(a))  # Output: True
print(complex(a))  # Output: (10+0j)



# Typecasting of variable "b" to other data types
print(int(b))  # Output: 3
print(str(b))  # Output: '3.14'
print(bool(b))  # Output: True
print(complex(b))  # Output: (3.14+0j)



'''# Typecasting of variable "c" to other data types
print(int(c))  # Output: ValueError: invalid literal for int() with base 10: 'Hello'
print(float(c))  # Output: ValueError: could not convert string to float: 'Hello'
print(bool(c))  # Output: True
print(complex(c))  # Output: ValueError: complex() arg is a malformed string
'''

# Typecasting of variable "c" to other data types (with numeric string)
print(int(c))  # Output: 123
print(float(c))  # Output: 123.0
print(bool(c))  # Output: True
print(complex(c))  # Output: (123+0j)


# Typecasting of variable "d" to other data types
print(int(d))  # Output: 1
print(float(d))  # Output: 1.0
print(str(d))  # Output: 'True'
print(complex(d))  # Output: 1+0j


# Typecasting of variable "e" to other data types
print(int(e))  # Output: TypeError: can't convert complex to int
print(float(e))  # Output: TypeError: can't convert complex to float
print(str(e))  # Output: '(10+5j)'
print(bool(e))  # Output: True


#converting a string to a list
s = "Hello World"
print(list(s))  # Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

#converting a string to a tuple
t = "Hello World"
print(tuple(t))  # Output: ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

#converting a string to a set
s = "Hello World"
print(set(s))  # Output: {'H', ' ', 'l', 'o', 'r', 'W', 'd', 'e', 'l', 'H'}

#converting a string to a dictionary
s = "Hello World"
print(dict(s))  # Output: {'H': 'H', 'e': 'e', 'l': 'l', 'o': 'o', ' ': ' ', 'W': 'W', 'r': 'r', 'd': 'd'}


'''
Decimal to Binary, Octal and Hexadecimal
1. Decimal to Binary: To convert a decimal number to binary, we can use the built-in function bin() in Python. 
    The bin() function takes an integer as input and returns a string representation of the binary number.
2. Decimal to Hexadecimal: To convert a decimal number to hexadecimal, we can use the built-in function hex() in Python. 
    The hex() function takes an integer as input and returns a string representation of the hexadecimal number.
3. Decimal to Octal: To convert a decimal number to octal, we can use the built-in function oct() in Python. 
    The oct() function takes an integer as input and returns a string representation of the octal number.
'''
# Decimal to Binary
a = 10
print(bin(a))  # Output: '0b1010'

# Decimal to Hexadecimal
a = 10
print(hex(a))  # Output: '0xa'

# Decimal to Octal
a = 10
print(oct(a))  # Output: '0o12'