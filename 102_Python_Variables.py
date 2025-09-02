"""Variables
        Variables are containers for storing data values.

 Creating Variables -
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it."""

x = 10
y = 'priyanka'
print(x)
print(y)

a = 10
print(type(a))
a = 'piya'
print(type(a))

"""Variables do not need to be declared with any particular type, 
and can even change type after they have been set."""

b = 10  # b is of type int
b= 'piya' # b is now of type str
print(type(b))

"""Casting -
If you want to specify the data type of a variable, this can be done with casting."""

x = int(3)
y = float(3)
z = str(3)
print(x)
print(y)
print(z)

"""Get the Type -
You can get the data type of a variable with the type() function."""

a = 10
print(type(a))
b = 10.11
print(type(b))
c = 'piuu' #String variables can be declared either by using single or double quotes
print(type(c))

"""Variable Names -
    Rules -
        1. A variable name must start with a letter or the underscore character
        2. A variable name cannot start with a number
        3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ 
        4. Variable names are case-sensitive (age, Age and AGE are three different variables)
        5.A variable name cannot be any of the Python keywords."""

a = 10 
a_ = 20
a_1 = 30
#-a = 40 not work syntax error variable declare karte time 
a1 = 50
b = 60
B = 70

x,y,z = 10,20,30
print(x,y,z)

#you can assign the same value to multiple variables in one line
x = y = z = 'arsh'
print(x)
print(y)
print(z)

names = ['Oma','piuu','Vivek']
x,y,z = names
print(x)
print(y)
print(z)

"""Output Variables
     Python print() function is often used to output variables."""

a = 'I am a good Boy'
print(a)

x = 'Python'
y = 'is'
z = 'Awesome'
print(x,y,z)

x = 'Python'
y = 'is'
z = 'Awesome'
print(x + y + z)

x = 'Python '
y = 'is '
z = 'Awesome '
print(x + y + z)

# Global Variables - Global variables can be used by everyone, both inside of functions and outside.

#Create a variable outside of a function, and use it inside the function
x = 'Awesome'
def myfunc() :
    print("Python is " + x)
myfunc()

#Create a variable inside a function, with the same name as the global variable
x = 'Awesome'
def myfunc() :
    x = 'Good'
    print("Python is " + x)
myfunc()
print("Python is " + x)

#If you use the global keyword, the variable belongs to the global scope:

def myfunc() :
    global x
    x = 'Good'
    print("Python is " + x)
myfunc()
print("Python is " + x)

