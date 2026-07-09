'''# 1. Area calculator
length = float(input('Enter area of length:-'))
breadth = float(input('Enter are of breadth:-'))

# Area of rectangle
area = length * breadth
print('Area of rectangle is', area)
# Perimeter of Rectangle 
perimeter = 2 * (length + breadth)
print('Perimeter of rectangle is', perimeter)
'''


'''# 2. Temperature Converter
c = float(input('Enter temperature in celsius ='))
f = (c * 9/5) + 32
print('Temperature in f =', f)
'''

'''# 3. Number Analyzer
number = float(input('Enter a number:'))
if number > 0:
    print("This is positive number")
elif number < 0:
    print("This is negitive number")
else:
    print(" This is Zero")
'''

'''
# 4. Largest Number
num1 = int(input('Enter first number:-'))
num2 = int(input('Enter second number:-'))

if num1 > num2:
    print("Large number is", num1)
elif num2 > num1:
    print("Large number is", num2)
else:
    print("Both numbers is same")
'''

'''
# 5. Even or Odd
num = int(input('Enter a number'))
if num%2==0:
    print('This is even number')
else:
    print('This is odd number')
'''

'''# 6. Employee Salary Bonus Calculator
employee_id = int(input("Enter Your Employee Id:- "))
employee_name = input('Enter your Name:- ')
employee_salary = int(input('Enter your salary:- '))
if employee_salary < 30000:
    bonus = employee_salary * 0.10
elif employee_salary <= 50000:
    bonus = employee_salary * 0.15
else:
    bonus = employee_salary * 0.20

final_salary = employee_salary + bonus

print("\n----- Employee Details -----")
print("Employee ID   :", employee_id)
print("Employee Name :", employee_name)
print("Salary        :", employee_salary)
print("Bonus Amount  :", bonus)
print("Final Salary  :", final_salary)
'''



'''
# 6. Student Result Processing System
student_name = input('Enter student name:-')
python_marks = int(input('Enter marks of python:-'))
sql_marks = int(input('Enter marks of SQL:-'))
excel_marks = int(input('Enter marks of excel:-'))
total_marks = python_marks + sql_marks + excel_marks
average = total_marks / 3

if average >= 90 :
    print("Student name is", student_name)
    print("Total marks =", total_marks)
    print("Avarage marks =", average)
    print('Grade A')
elif average >= 75 and average <90:
    print("Student name is", student_name)
    print("Total marks =", total_marks)
    print("Avarage marks =", average)
    print('Grade B') 
elif average >= 60 and average < 75:
    print("Student name is", student_name)
    print("Total marks =", total_marks)
    print("Avarage marks =", average)
    print('Grade C')
else:
    print("Student name is", student_name)
    print("Total marks =", total_marks)
    print("Avarage marks =", average)
    print('Fail')
'''

'''
# 7.Simple Calculator
num1 = int(input('Enter first number:-'))
num2 = int(input('Enter Second number:-'))
operator = input('Enter operator (+, -, *, /):-')
match operator:
    case '+':
        print('Result is', num1 + num2)
    case '-':
        print('Result is', num1 - num2)
    case '*':
        print('Result is', num1 * num2)
    case '/':
        print('Result is', num1 / num2)
    case _:
        print('Invalid operator')
'''

print("Warning!\a")