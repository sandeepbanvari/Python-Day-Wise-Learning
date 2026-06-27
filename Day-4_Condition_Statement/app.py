'''
Condition Statement in python
    -- Condition statement is used to perform different actions based on different conditions.
    -- It is used to make decisions in the code and execute a block of code based on the condition.
    -- There are several types of condition statements in Python:
        1. if statement
        2. if-else statement
        3. if-elif-else statement
        4. match statement
        5. nested if statement
'''
'''
1. if statement
    -- The if statement is used to test a specific condition. If the condition is true, the block of code inside
       the if statement is executed.
    Syntax:
        if condition:
            # block of code to be executed if the condition
'''

# Example of if statement
# a = 10
# if a > 5:
#     print("Yes, a is grater than 5")
    

'''
2. if-else statement
    -- An if-else statement is a decision-making statement in Python that executes one block of code
       when a condition is true and another block when the condition is false.
    Syntax:
        if condition:
            # block of code to be executed if the condition is true
        else:
            # block of code to be executed if the condition is false
'''

# Example of if-else statement
# num = 10
# if num > 0:
#     print('This is positive number')
# else:
#     print('This is negitive number')
    

# Example of if-else statement using input method
'''
input() method:
    -- input() is a built-in Python function used to accept data from the user at runtime. 
    -- It always returns the entered value as a string, which can be converted to other data types using functions like int(), float(), etc.
'''

# num = int(input("Enter the Number:"))
# if num >=18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")
    
    
# Example of if elif-else statement

percentage = int(input('Enter your percentage:-'))
if 90<=percentage and 101>percentage:
    print("Grade A")
elif 70<=percentage and 90>percentage:
    print('Grade B')
elif 50<=percentage and 70>percentage:
    print('Grade C')
elif 35<=percentage and 50>percentage:
    print('Grade D')
else:
    print('Fail')


# Example of nested statement

percentage = int(input("Enter your percentage:-"))
if 0 <= percentage and percentage <= 100:
    if 90<=percentage and 101>percentage:
        print("Grade A")
    elif 70<=percentage and 90>percentage:
        print('Grade B')
    elif 50<=percentage and 70>percentage:
        print('Grade C')
    elif 35<=percentage and 50>percentage:
        print('Grade D')
    else:
        print('Fail')
else:
    print('Enter Prorper Percentage')
    
    
# Example of match statement
day = int(input("Enter a number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")
        
        
'''
3. if elif else statement:
    -- An if-elif-else statement is a decision-making statement in Python that executes one block of code
       when a condition is true, another block when the condition is false, and another block when the condition is false.
    Syntax:
        if condition1:
            # block of code to be executed if the condition1 is true
        elif condition2:
            # block of code to be executed if the condition2 is true
        else:
            # block of code to be executed if none of the above conditions are true
'''

        
        
        
        