


#print("Hellow Sourabh")

#import sys
#print(sys.version)

#Python will give you an error if you skip the indentation
#The number of spaces is up to you as a programmer, the most common use is four,
#but it has to be at least one.
#if 5 > 2:
#    print("Five is greater than Two!")
#    print("Five is greater than Two!")

#Python Comments
#Comments can be used to explain Python code.
#Comments can be used to make the code more readable.
#Comments can be used to prevent execution when testing code.

#This is a comment
#x = 5
#y = "Hellow, World"

#multiline string (triple quotes)

"""
This is a comment
written in
more than just one line
"""
#print("Hello, World!")

#x = 4
# = "Sally"
#print(x)

# Python Veriables
"""
x = 5
y = "John"
print(x)
print(y)
"""
#x = str(3)
#y = int(3)
#z = float(3)

#print(x)
#print(y)
#print(z)
"""
x = 5
y = "john"
print(type(x))
print(type(y))
"""
#Variable names are case-sensitive.
"""
a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)

#Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"


Multi Words Variable Names
myVariableName = "John"
my_variable_name = "John"

x, y, z = "Red", "Orange", "Green"
print(x)
print(y)
print(z)

x = y = z = "Banana"
print(x)
print(y)
print(z)


fruits = ["apple", "banana", "cheery"]
x, y, z = fruits
print(x)
print(y)
print(z)


x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"

print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)



x = 5
y = 10
print(x + y)

#In-Correct
x = 5
y = "John"
print(x + y)

#Correct
x = 5
y = "John"
print(x, y)

a = 'Hello'
b = 'World'
print(a + b)
#Ans-HelloWorld
"""

"""
# Python - Global Variables
Variables that are created outside of a function (as in all of the examples in
 the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

If you create a variable with the same name inside a function, this variable
 will be local, and can only be used inside the function. The global variable
  with the same name will remain as it was, global and with the original value.
  
  so here output value is depends on the exact site of Print() 

x = "Awesome"

def myfun():
    print("Python is a " + x)

myfun()

x = "Awesome"

def myfun():
    x = "Fantastic"
    print("Python is a " + x)

myfun()

def myfun():
    global x
    x = "Fantastic"
    print("Python is a " + x )

myfun()

x = "Awesome"

def myfun():
    global x
    x = "Fantastic"
    print("Python is a " + x)

myfun()

x = 'awesome'
def myfunc():
  x = 'fantastic'
print('Python is ' + x)

myfunc()

x = 'awesome'

def myfunc():
    x = 'fantastic'

myfunc()
print('Python is ' + x)   (So here answer will be Print side ANS IS awesome)


x = 'awesome'

def myfunc():
    x = 'fantastic'
    print('Python is ' + x) (So here answer will be Print side ANS IS fantastic)

myfunc()

x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x) (So here answer will be fantastic because we mentioned here global x)
"""
"""
Built-in Data Types

In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types -->	int, float, complex
Sequence Types-->	list, tuple, range
Mapping Type  -->	dict
Set Types     -->	set, frozenset
Boolean Type  -->	bool
Binary Types  -->	bytes, bytearray, memoryview
None Type     -->	NoneType

#You can get the data type of any object by using the type() function:

x = 5.22
print(type(x))

x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

#Int, or integer, is a whole number, positive or negative, without decimals,
#of unlimited length.

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


#Float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex numbers are written with a "j" as the imaginary part:
#Complex

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))



x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x)
b = complex(z)
c = int(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Import the random module, and display a random number between 1 and 9:
import random
print(random.randrange(1,10))


#Strings
#Strings in python are surrounded by either single quotation marks,
# or double quotation marks.
print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hellow"
print(a)

a = "Hello, World!"
print(a[1])

for x in "Banana":
  print(x)

#String Length

a = "Hellow, World!"
print(len(a))

txt = "The best thing in the life are Free!"
print("Free" in txt)


txt = "The best thing in the life are Free!"
if "Free" in txt:
    print("Yes", 'Free is present.')

txt = "The best thing in the life are Free!"
print("expensive" not in txt)


txt = "The best thing in the life are Free!"
if "expensive" not in txt:
    print("No,'expensive' is not present.")



x = "Welcome"
print(x[3])

txt = "Hellow World"
print(txt[0])


#Get the characters from position 2 to position 5 (not included):
b = "Hellow, World"
print(b[2:5])


# By leaving out the start index, the range will start at the first character:
b = "Hellow, World"
print(b[:5])

# Get the characters from position 2, and all the way to the end:
b = "Hellow, World"
print(b[2:])


# Get the characters from position 2, and all the way to the end:
b = "Hellow, World"

#Get the characters:
#rom: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])
Ans-orl

#Upper Case

a = "Hello, World!"
print(a.upper())
print(a.lower())

#Remove Whitespace
#The strip() method removes any whitespace from the beginning or the end:
a = "Hello, World!"
print(a.strip())

a = "Hellow, World"
print(a.replace("H" , "j"))

a = "Hello, World!"
print(a.split(","))


# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Python - Format - Strings
age = 36
txt = "My name is John, I am  + 36"
print(txt)
"""

"""
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

#Python - Escape Characters

l = [12,89,'gh',78.89,[56,89,90],(56,89),89]
print(l[0])



print(12+9)


print(10 and 20)
print(10 or 20)


n1 = eval(input("10"))
n2 = eval(input("20"))

if n1>n2:
    print("10",n1)
else:
    print("20",n2)
"""