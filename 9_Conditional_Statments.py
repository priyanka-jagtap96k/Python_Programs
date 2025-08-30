"""Types of Conditional Statements in Python

if statement

if-else statement

if-elif-else ladder

Nested if statements

Nested if-else statements"""

#if statement
print("if statement")
a = 10
b = 20

if a > b:
    print("b is greater than a")   # indentation is correct (4 spaces)

#if-else statement
print("if-else statement")
a = 10
b = 20

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

#if-elif-else ladder
print("if-elif-else ladder")
num = 0

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

#Nested if statements
print("Nested if statements")
num = 25

if num > 0:
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

#Nested if-else statements
print("Nested if-else statements")
num = -2

if num > 0:
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")   
else :
    print("Number is Negative")     


