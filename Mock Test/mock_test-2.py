'''# check whether a number is even or odd
num = int(input("Enter the number:- "))

if num % 2 == 0:
    print('This is is even Number')
else:
    print('This is odd number')
    
# output
# Enter the number:- 10
# This is is even Number
# Enter the number:- 11
# This is is odd Number'''

'''# The largest of two numbers
num1 = int(input('Enter the first number:-'))
num2 = int(input('Enter second number:- '))

if num1 > num2:
    print(num1,' is the largest numer')
elif num1 < num2:
    print(num2,' is the largest numer')
else:
    print('Both numbers are equal')'''
    
'''# Write a program to print numbers from 1 to 20 using a loop.
for i in range(1, 21):
    print(i)'''
    

'''# Write a program to calculate the sum of first 10 natural numbers.
num = 0
for i in range (1, 11):
    num = num + i
print('Sum is', num) #sum is 55'''


'''# Write a program to count the number of vowels in a string.
text = input("Enter a string: ") # Python Programming
count = 0

for i in text.lower():
    if i in "aeiou":
        count += 1

print("Number of vowels:", count) # 4
'''


'''# Write a function that accepts two numbers and returns their sum.
def add_numbers(num1, num2):
    return num1 + num2

print(add_numbers(10,30)) # 40
'''

'''# 29. Write a function to check whether a number is prime or not.
num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")'''
    
    
'''# 30. Write a function to calculate the factorial of a number.
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial =", fact)

num = int(input("Enter a number: "))
factorial(num)'''


'''# 35. Write a menu-driven calculator using functions that performs:
#  Addition
#  Subtraction
#  Multiplication
#  Division 
def calculator(a, b):
    return a + b, a - b, a * b, a / b

add, sub, mul, div = calculator(10, 5)

print("Addition =", add) # 15
print("Subtraction =", sub) # 5
print("Multiplication =", mul) # 50
print("Division =", div) # 2.0'''


'''# 36. Write a program that accepts 5 student marks, stores them in a list, and displays:
# Total Marks
# Average Marks
# Highest Marks
# Lowest Marks
marks = []

for i in range(5):
    mark = int(input("Enter mark: "))
    marks.append(mark)

print("Total Marks =", sum(marks))
print("Average Marks =", sum(marks) / len(marks))
print("Highest Marks =", max(marks))
print("Lowest Marks =", min(marks))'''

#leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")