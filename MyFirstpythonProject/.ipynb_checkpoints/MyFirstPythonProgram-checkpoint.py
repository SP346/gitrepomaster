
# key points
# To comment all lint with(#-symbol) keyword is [ ctrl + / ]


# lecture no -1

# Python....
# Web Development
# Data Analytics
# Automation



# Python ======> 30%
# java   ======> 20%
# JS     ======> 8.5%
# C#     ======> 7%
# PHP    ======> 6%
# C/C++  ======> 5.5.%
#
# Calculation
# Simple lan english
# try to practice during session
#
#    ===> 1991 Feb-Mar -> Guido Van
#
# 1. ===> Development => [Web Application + Web Services]
#
# 2. ===> Machine Learning [Data Science]
#
# 3. ===> Automation
#
# 4. ===> Data Analytics
# ------------------------
# on to Python Download Python &
#
# Setup Environment
#
# Python + PyCharm
# ------------------
# Python
# +
# PyCharm => Any Python Code =>



# lecture no - 2 

# Today I am going to learn Python
'''
My First Name is Yogesh
My Last Name is Tyagi
I am from Noida'''
from difflib import diff_bytes
from xml.dom.xmlbuilder import DOMBuilder

# from doctest import FAIL_FAST
#
# print("This is my first Python Program")
# Right click => execute
# Button
# Shift + F10
# Command Prompt
#
# Variables & constants

# int variable name......

# Comments ============>
# from file input import lineno

# single line number
# multi lineno

# My first name is Sourabh
# My Second name is Patil
# I am from Kolhapur

'''
My first name is Sourabh
My Second name is Patil
I am from Kolhapur'''


# Why python is more in use?
# Very Very easy => any one can try

# print("This is my first Python Program")

# Variables & constants    --Main Point of this lecture
# Automatically detect the data types in Python

# Variable - A variable is a name that refers to a value.
# It's a way to store information that can be changed or manipulated throughout the program.

# age = 10
# first_name = "Sourabh"
# last_Name = "Patil"
#
# Semi colons but it's Optional;
# it is case sensitive
# Indentation
#
# print(age);
# print(first_name+last_Name);
# print(first_name+" "+last_Name);
#
# Req No-2  --> My First name is sourabh and last name is patil and my age is 27
# print("my first name is "+first_name+" and my last name is "+last_Name+" and my age is 10")
# print("my first name is "+first_name+" and my last name is "+last_Name+" and my age is "+str(age))

# Type casting => we convert data types => int => string or string to int
# Variable => are using to store data and value can change
# age = 20
# print(age)


# Multiple variables assigned same values
# x=y=z=10
# print(x)
# print(y)
# print(z)

# Multiple variables and multiple values
# a,b,c=10,20,30
# print(a)
# print(b)
# print(c)

# user input
# data = input("Please enter your age: ")
# print(data)
# print("My age is: "+data)

# datanew = int(data)+5
# print(datanew)

# Constant

# Constant - A constant is a value that remains unchanged once defined.
# By convention, constants are usually defined using uppercase letters.
# While Python does not have built-in support for constants (i.e., there
# is no keyword to define a constant), the convention of using uppercase
# letters signals to other programmers that these values should not be changed.
# EX:-
# PI = 3.14159
# MAX_SPEED = 120


# FIRST_NAME = "Yogesh"
# print(FIRST_NAME)

# FIRST_NAME = "Vivek"
# print(FIRST_NAME)



# lecture no - 3

# from importlib.metadata import files

# from typing import Concatenate

# 1. New project
# 2. new files
# 3. project settings
# 3. simple print statement
# 5. Comment 1,2
# 6. how to execute ?
# 7. how take input
# 8. how to use input for further calculation
# 9. Create variables
# 10. how to use variables
# 11. Constants
# 12. Concatenate
# 13. Continuation
# 14. Type Casting
#     int to string
#     string to int


# ========= Conditional Handling =====================
# In Python, conditional statements allow you to execute certain pieces
# of code based on whether a given condition is true or false. They are
# essential for controlling the flow of a program

# Single Condition (if)
# Two Condition (if - else)
# Multiple Condition (if elif-elif-else)

# Notes
# We can not apply the condition to the else statement
# and else is not mandatory

# 1 Single Condition (if)
# We will take input from user
# check this number => if this number is even => This is even number
# If number will odd then we will not do anything

# 2,4,....100
# 1,3,....99


# data = input("Please enter your Number: ")
# data = int(data)
#
# if(data % 2 ==0):
#     print("This is even number")
#     print("This is my first conditional program")
#     print("This is my first conditional program")
# print("This is out of if statement")  -- This is something independent line not related to if condition
#
#
#
# 2 Two Condition (if - else)
#
# we will take input from user -> Number
# Check that number if number is even => print that number is even
# if the number is odd then => print number is odd
#
#
# num = input("please enter your number: ")
# num = int(num)
#
# if(num % 2 ==0):
#     print("This is even Number: "+ str(num))
# else:
#     print("This is odd Number: "+ str(num))


# 3 Multiple Condition (if elif-elif-else)
# take input from user - Number
# check this number => number is negative => Negative number?
# check this number is zero => Number is Zero
# Check if this is a positive number => Even



# data = input("Please enter your Number: ")
# data = int(data)
#
# if(data < 0):
#     print("This is a Negative Number: "+str(data))
# elif(data == 0):
#     print("This is is zero: "+str(data))
# elif(data % 2 ==0):
#     print("This is a even number: "+str(data))
# else:
#     print("This is a odd number: "+str(data))
#
#
#
# We can use here the extra elif for odd number showing with condition
# data = input("Please enter your Number: ")
# data = int(data)
#
# if(data < 0):
#     print("This is a Negative Number: "+str(data))
# elif(data == 0):
#     print("This is is zero: "+str(data))
# elif(data % 2 ==0):
#     print("This is a even number: "+str(data))
# elif(data % 2 ==1):
#     print("This is a odd number: "+str(data))
#


# 4 Multiple Condition (if elif-elif-else)
# Take input from user => Marks > 0 or Marks < 0 => Invalid Marks
# if the Marks is in between 0 to 100 => Valid Marks



# Marks ==>
# Subject => 100 => 40, 50, 90
# Marks < 0 ==> Invalid Number
# Marks >100 ==> Invalid Number
# Marks between 0 and 100 ==> valid Marks


# marks = input("Enter Marks: ")
# marks = int(marks)
#
# check condition
# if(marks < 0 ):
#     print("This is Invalid Number: ")
# elif(marks > 100):
#     print("This is invalid Number: ")
# else:
#     print("Marks is valid")



# Lecture No-4


# AND ========> Conditions?
# Taking input from user

# 1 
# +ve and number is divided by 2 => even number
# +ve and number is not divided by 2 =? Odd number

# taking input from user
 
# num=input("Enter Number: ")
# num=int(num)
#
# if((num>0) and (num%2==0)):
#     print("This is even number")
# elif((num>0) and (num%2==1)):
#     print("This is odd number")

# Range:-

# In Python, the range function is used to generate a sequence of numbers.
# It is often used in for-loops to iterate over a block of code a
# specified number of times.

# 2 (By using range function)
# Starting and ending point
# num * count = 7

# num=input("Please enter number: ")
# num=int(num)
#
# for i in range(1,11):
#     print(str(num)  + " * " + str(i) +" = "+ str(num*i))


# 3 

# no starting value, only final value or range
# when you will not give starting point in python it would start from zero
# final value never prints

# num=input("Please enter any number: ")
#
# for i in range(int(num)):
#     print(i)


# 4
# For loop with starting and ending values, increment logic
# from traceback import print_tb

# If i want to print number 0 to 10

# for i in range(1,50,5):
#     print(i)

# for loop with decrement
# print a number with decreased order

# num=input("Enter the Number: ")
# num=int(num)

# for i in range(10,0,-1):
#     print(num*i)
#


# For loop with List
# Difference between variable & list
# Variable will always store one value at a time
# list will store n number of values at a time
# whenever you will be using for loop with list

# list=[1,2,3,4,5.............,Testing,Yogesh, abc@gmail.com,.]

# list1 = [1,2,5,9,100,'Sourabh','Patil','abc@gmail.com']
#
# for i in list1:
#     print(i)
#

# extract values from string

# Testing
# 'Sourabh'
# 'Sourabh'
# """Sourabh"""

# "o'abc"
# "o'abc"


# get the sum of all values available in the list
# it will show the list values total sum

# list1=[33,45,67,89,100]
# a=0
# for i in list1:
#     a=a+i
# print("This is outside of for loop: "+str(a))


# =======> integer => string =>
# =======> string => integer =>



# Why we need loops
# You will have to do the same task again and again like 10 times & 100 times
# Database connection => Failed => try 100 times


# Lecture No - 5

# String is group of multiple character


# String Handling
# What is string?
# How to define string in Python?
# Concatenate String?
# Multiplication of String
# Type Casting

# Substring --
# Fetch Substring by Given Index
# Fetch Substring by Given Starting index & End Index
# Only Starting Index
# Only ending Index

# Common Operation
# Length of any String
# Upper case
# Lower case
# Take first char of String in upper case

# remove space from left side
# remove space from right side
# remove space from both side

# replace data into string
# find data into string
# split string on behalf of any character [Splitter]

# String Comparison
# Case Sensitive
# Not case Sensitive

# Define String


# 1 
# email = "sourabh346@gmail.com"    # String in Double quotes

# name = 'Sourabh'         # String in Single Quotes

# data = """
#       My name is Sourabh
#       I am From Maharashtra
#       I am doing job in Telecom sector

# print(email)
# print(name)
# print(data)

# if you will have in your string

# concatinate

# a = 'Sourabh'
# b = 'Patil'

# c = a + " " + b

# print(a + " " + b)

# 2
# name = input("Please enter your name: ")
# phonenumber = input("Please enter your phone number: ")

# print(name)
# print(phonumber)

# print("My name is "+name+" and my phone number is "+phonenumber)

# print(name*2)     # Their will not be any manipulation in between. multplication it will come one line only

# 3
# Type casting
# Take input from user and ask enter name and marks
# add 5 extra marks

# name = input("Please enter your name: ")
# marks = input("Please enter your marks: ")

# marks = int(marks) + 5

# Hellow sourabh you got? marks

# print("Hellow "+name+" you got "+str(marks)+ " marks")

# 4
# Find length of any string
# from trace back import print_tb

# data = "This is my fifth session of python"

# length
# print(len(data))
# -->34

# Upper case
# print(data.upper())
# -->THIS IS MY FIFTH SESSION OF PYTHON

# Lower case
# print(data.lower())
# -->this is my fifth session of python
#
# only initial character in upper case
# print(data.capitalize())
# -->This is my fifth session of python
#
# 5 Index

# Index will always start from 0

# data = "This is my fifth session of Python"
#
# Fetch specific character by using index
# print(data[15])
# -->h
#
# print(data[5:10])
# -->is my
#
# print(data[2:18])
# -->is is my fifth s
#
# Fetch substring by given starting index
# print(data[5:])
# -->is my fifth session of python

# Fetch substring by given end index
# print(data[:25])
# -->This is my fifth session

# 6

#ltrim => istrip()
#rtrim => rstrip()
#trim  => strip()

# data = "  This is my fifth session of Python "
#
# print(len(data))
# -->36
#
#Remove space from left side
# print(len(data.lstrip()))
# -->34
#
# Remove space from right side
# print(len(data.rstrip()))
# -->36


#Remove space from both side
# print(len(data.strip()))
# -->34

# 7 

# Advanced string handling
# replace

# data = "This is my fifth session of python"
#
# print(data.replace(" ",""))
# -->Thisismyfifthsessionofpython
#
# print(data.replace("fifth","Fifth"))
# -->This is my Fifth session of python

# print(data.replace("python","My Training"))
# -->This is my fifth session of My Training
#
# print(data.replace("s","ABC"))
# -->ThiABC iABC my fifth ABCeABCABCion of python
#
# print(data.replace("Sourabh","Patil"))   # if the content is not matching then it will print same



# Lecture No - 6


# List
# Tuple
# Dictionary

# myfirstlist = [10,20,30,"Testing"]
# myfirsttuple = (10,20,30,"Testing")


# Key Value pair
# a = 100
# b = "Sourabh"
#
# myfirstdictionary = {"a":100,"b":"Sourabh"}
#
#
# We will be learning list operations
# Define a list
#
# 1.
#
# finalist = [2000,2001,"Testing","Java","Python"]
#
# Display complete data from the list:
# print(finalist)
# -->[2000, 2001, 'Testing', 'Java', 'Python']
#
#
# print the length of list
# print(len(finalist))
# -->5
#
# Fetch data from list by given index:
# print(finalist[3])
# --> Java


# Fetch data from list by given range on index:
# print(finalist[2:4])
# -->['Testing', 'Java']

# Fetch data from list by given first index value and till end
# print(finalist[1:])
# -->[2001, 'Testing', 'Java', 'Python']

# Fetch data from list by given end index value and till first
# print(finalist[:3])
# -->[2000, 2001, 'Testing']

# Define a list

# finalist = [2000,2001,"Testing","Java","Python"]

# get length of list
# lenlist = len(finalist)

# Approach# 1 run the loop on the list

# for i in range(0,lenlist):
#     print(finalist[i])
# -->
# 2000
# 2001
# Testing
# Java
# Python


# Approach #2 to get data from list
# for data in finallist:
#     print(data)
# -->
# 2000
# 2001
# Testing
# Java
# Python

# Merge List

# Listf = [10,20,30,"Testing"]
# Lists = ["PHP","Java","C++"]

# merge two list using concatination
# final_list = Listf + Lists

# Print final merged list
# print(final_list)

# length of murged list
# print("*********Length list*****************")
# print(len(final_list))



# 3
# Update
# Insert
# Removed

# Define list
# mylist = [10,20,30,"Testing"]
# print(list)

 
# Update
# first identify which value you want to update  [2]
# By which value you want to update [50]

# For replace the Value data type does not matter it will update int to char

# mylist[2] = 50
# print("*************Updated list********************")
# print(mylist)
# -->[10, 20, 50, 'Testing']


# mylist = [10,20,30,"Testing"]
# Insert Operation -
# print("*****************Original List********************")

# print list
# print(mylist)
# print("*****************insert Value********************")

# mylist.insert( 2,"Sourabh")
# print(mylist)
# -->[10, 20, 'sourabh', 30, 'Testing']

# Remove
# mylist = ["Testing",10,20,30,"Testing"]

# print("*****************Original List********************")
# print(mylist)

# mylist.remove("Testing")

# print("*****************Updated List********************")
# print(mylist)
# -->[10, 20, 30, 'Testing']

# List [10,20]
# Read & Write


# Tuple (10,20)  ------ Limitations
# read data, it doesn't allow to write data.

# Define Tuple
# mytuple = (10,20,30,"Testing","Java","Noida")
# print(mytuple)
# -->(10, 20, 30, 'Testing', 'Java', 'Noida')

# Note-Very IMP
# index(Position of data) will come always square braces while fetching any value in range list tuple
# Fetch data from any specific index

# print("**************Fetch data from any specific index***************")
# print(mytuple[2])
# -->30

# Fetch data from any range
# print("********Fetch data from any range********************")
# print(mytuple[2:5])
# -->(30, 'Testing', 'Java')

# Fetch data from Starting Index to till end
# print("********Fetch data from Starting Index to till end ********************")
# print(mytuple[1:])
# -->(20, 30, 'Testing', 'Java', 'Noida')

# Fetch data from Starting from begning and till given end index
# print("********Fetch data from Starting from begning and till given end index ********************")
# print(mytuple[:5])
# -->(10, 20, 30, 'Testing', 'Java')

# Get length of tuple
# print(len(mytuple))
# --> 6

# For loop on tuple

# mytuple = (10,20,30,"Testing","Java","Noida")
# tuple_len = len(mytuple)
#
# print(mytuple)

# 1st Approach
# print("**********************Read data from tuple***********************")
# for i in range(0,tuple_len):
#     print(mytuple[i])

# Second Approach
# print("**********************Read data from tuple using second Approach***********************")
# for data in mytuple:
#     print(data)
#

# Concatination
# Define Tuple

# mytuplef = (10,20,30,"Testing","Java","Noida")
# mytuples = (50,"Delhi")

# final_tuple = mytuplef + mytuples

# Print Tuple
# print(final_tuple)

# Update Operation on Tuple (Tuple Will not insert update & Delete Operation)
# mytuplef[2] = "Sourabh"

# print(mytuplef)


# Dictionary

#list[10,20,30,"Testing"]
#tuple(10,20,30,"Testing")

#Dictionary{}
# Dictionary is used to store in Key Value Form

# a = 10
# b = 20
# c = 30
# d = "Testing"

# mydictionary = {a = 10,b = 20,c = 30,d = "Testing"}
# mydictionary = {"a" = 10,"b" = 20,"c" = 30,"d" = "Testing"}

# mydictionary = {"a":10,"b":20,"c":30,"d":"Testing"} # This is the correct way to define the Dictionary

# print(mydictionary)
# --> {'a': 10, 'b': 20, 'c': 30, 'd': 'Testing'}

# Lecture No - 7

# List

    # Data placed in [] and data is separated by comma (,)
    # Can save multiple data of diff data types
    # Can fetch data by giving Index
          # specific Index
          # range [3:8]
          # range [1:]
          # range [:5]
    # Support read & Write Operations.
          # Loop through complete list to fetch data
          # Two approach to fetch data using for loop
          # Add item
          # remove item
          # update item
    # Find the length of list
    # Concatenate multiple lists



# Tuple

   # Data placed in () and data is separated by comma (,)
   # Can save multiple data of diff data types
   # Can fetch data by giving Index
          # specific Index
          # range [3:8]
          # range [1:]
          # range [:5]
   # Support read Operations
          # Loop through complete list to fetch data
          # Two approach to fetch data using for loop
   # Find the length of Tuple
   # Concatenate multiple Tuples


#Disctionary
    # Data placed in {} and data is separated by comma (,)
    # Data is stored in Key-Value Pair
    # Key and Values are separated by:
    # Values can be duplicate
    # Keys must be unique
    # Can save multiple data of diff data types
    # Can fetch data by given Key
    # It supports Read and write Operations
    # Fetch all keys or values from Dictionary
    # Find the length of Dictionary


# Define Dictionary

# myDics = {"a":100, "b":200, "c":"Testing",10:"Yogesh"}

# Fetch the complete data from dictionary

# print(myDics)
# --> {'a': 100, 'b': 200, 'c': 'Testing', 10: 'Yogesh'}

# Get length of Dictionary
# print(len(myDics))

# Fetch any specific values from Dictionary
# print("*************** Fetch any specific values from Dictionary *****************")
# print(myDics["a"])
# print(myDics["b"])
# print(myDics["c"])
# print(myDics[10])


# Add value in my Dictionary
# myDics["Email"] = "sourabh1234@gmail.com"

# print(myDics)

# Add anathor value in my Dictionary
# myDics[105] = "My first Program"
# print(myDics)

# Updated Key & value will show in Dictionary
# myDics["c"] = 500
# print(myDics)

# Delete value from Dictionary
# print("************** Updated Disc After Removing ******************")

# myDics.pop("a")
# print(myDics)

# fetch only all keys from Dictionary
# print(myDics.keys())

# name key => First Name
# Later new requirement came => Full name
# name = "Full Name"

# Tables => 10 columns  =>

# list => allow duplicate values => order
# tuple => allow duplicate values => order
# Dictionary=> will not allow => not follow order


# => Complex Data types =>>


# Note:-

# Creating a list my_list = [1, 2, 3, "apple", "banana"] 
# Printing the entire list print(my_list) 
# Printing a specific element print(my_list[2]) 
# Output: 3 # Printing all elements using a loop for item in my_list:

# Creating a tuple my_tuple = (1, 2, 3, "apple", "banana") 
# Printing the entire tuple print(my_tuple) 
# Printing a specific element print(my_tuple[2]) # Output: 3 
# Printing all elements using a loop for item in my_tuple: print(item)

# Creating a dictionary my_dict = { "name": "Alice", "age": 30, "city": "New York" } 
# Printing the entire dictionary print(my_dict) 
# Printing a specific value print(my_dict["name"]) # Output: Alice 
# Printing all key-value pairs using a loop for key, value in my_dict.items(): print(f"{key}: {value}")



# Lecture No - 8


# What is a function?
# Why we create function?
# How to create function?

# Function can be defined as a group of code.
# Function is a group of connections.
# which is used to perform any task. Example is database connection.

# 1. ?
# 2. Reusability.
# 3. Removing the duplicacy of the code.

# To define a function, you use the def keyword, followed by the function
# name and parentheses (). The code block within the function is indented.
# Def kind of short code of Define.
# it is nothing but keyword.
# Def is a unique identifier of function. Def means Define.

# Ex-1
# def testing():
#     "This is my first line of code as optional"
#     print("Today I am going to learn functions in Python")
#
#     print("This is my good learning")
#
# testing()

# Rules to create functions

# 1. Function Body should Started with:(colon) (with same indentation)
# 2. def => is a keyword to create a function and it's unique identifier for functions.
# 3. First line of function is optional, can be used for commenting.
# 4. Return keyword => Return keyword shows end of the function.

# Ex:-2
# def myfun():
#     print("I am going to use Return keyword in this function")
#     return
#     print("I may be wrong")
#
# myfun()


# Diff type of Functions

# 1. Function not taking argument and not returning values
# 2. Function is taking argument but not returning values
# 3. Function is taking argument and returning values
# 4. Function without argument and returning values

# starting with first combination
# Ex:-3

# def myfun():
#     print("This is my first combination of Function")
# myfun()

# Ex:-4

# def sum():
#     a=10
#     b=20
#     c=a+b
#     print("sum of two numbers: - " + str(c))

# sum()
#
# Ex:-5
# def sumofvalue(a,b):
#     c=a+b
#     print("sum of two numbers: - " + str(c))
#
# sumofvalue(12,13)

# (10*20) + 100

# Create a manipulation function
# define function

# def multiply(a,b):
#     c=a*b
#     return c
#
# def addition(o,p):
#     r=o+p
#     print("This is the final outcome of Multiplication and Addition:- "+ str(r))
 
# x=multiply(10,20)
# print("This is multiplication of two values: - "+str(x))
# print("This is my hardcoded value: - " + str(x+100))
#
# addition(x,40)
#

# Function without argument and returning value

# def retdata():
#     a=100
#     b=200
#     c=a+b
#     return c
#
# x=retdata()
# print("This is the outcome of my function which is not taking any argument: - " + str(x))



# Lecture no - 9

# Type of argument

# 1. => Required Arguments
# 2. => keyword Arguments
# 3. => Default Arguments

# Required parameters

# def takeinput(a,b):
#     c=a+b
#     print("sum of both parameter: - " + str(c))

# takeinput(10,100)


# Between => Parameter & Argument
# Between => Function & Method

# Keyword Parameter

# def takeMyInput(a,b):
#     c=a+b
#     print("sum of both argument: - " + str(c))
#
# takeinput(x=200,b=250)

# Default parameter
# def MyDefaultFun(a,b=20,c=10):
#     c=a+b
#     print(c)

# MyDefaultFun(a=550)


# 10th Class 100 Students

# 1. Red color balls => 100 balls

# 2. blue color balls => 100 balls

# 3. white color balls => 100 balls

# Class

# 1.Python is an Object oriented Programming Language
# 2.We can write our code in classes
# 3.Class can have variables, constants, functions, constructor
# 4.We can access class members by creating object of class

# Creating my first class

# class A:
#    # creating a method inside my class
#    def myclassfun(self):
#        print("This is my method inside my first class")

# to call any member of a calls, creating an object
# obj = A()

# call function of class by using object of a class
# obj.myclassfun()

# Multiple Functions

# Function with no Argument and no return value
# Function with Argument and no return value
# Function with Argument and return value

"""
class A:
    #Create first function => Function with no argument and no return value
    def test(self):
        print("I am from Noida")

#   Create second function => Function with Argument and no return value
    def sum(self,a,b):
        c=a+b
        print("sum of arguments: - " + str(c))

#   Create third function => Function with argument and return value
    def multiply(self,a,b):
        c=a*b
        return c
        print("Multiply of two parameters: - " + str(c))
"""
# Create an object
# obj=A()


# call first function
# obj.test()

# call second function
# obj.sum(10,40)

# Key Points: For call second function
# With Arguments: The function sum takes two arguments,
# a and b. These are input values provided when the function is called.
# No Return Value: The function does not have a return statement.
# Instead, it prints the result of the operation (c).

# call 3rd method
# x=obj.multiply(10,50)
# print(x)

# Key Points:call 3rd method return value means with help of Return
# With Arguments: The function multiply takes two arguments,
# a and b. These are inputs provided when the function is called.
# Return Value: The function calculates the product of a and b and
# uses the return statement to send the result (value of c) back to the caller.
# Note:-
# In Python, the return keyword is used to end the execution of a
# function and optionally pass back a value to the caller


# Lecture no - 10

# OOPS

# 1.CLASS
# 2.Constructor

# 3.Inheritance
# 4.Encapsulation
# 5.Polymorphism
# 6.Abstraction

# What is constructor?
# Why we use Constructor?

# constructors are special kind of method
# Constructs always called automatically, when we create the object of the class.
# Constructors created with__init()__=> first argument is always self that will be default

# Constructors can take arguments
# Constructors never returns any value
# Constructors are used for initialization.

# Create object of a class in another Python file
# 1.First we need to import Python file
# 2.Then create object of that class and start to use that.....

# Requirement:1
"""
class A:

    def __init__(self):
        print("First line of code")
        print("Second line of code")
        print("Third line of code")

    #method#1
    def sum(self,a,b):
        c=a+b
        print("Here is sum of two values: " + str(c))

    #methos#2
    def mul(self,a,b):
        c=a*b
        print("Here is multiplication of two numbers: " + str(c))

obj =A()
obj.sum(2,2)

# -->Here is sum of two values: 4

obj.mul(12,12)
# -->Here is multiplication of two numbers: 144
"""

# Requirement:2
"""
class A:
    def __init__(self, fname=None, lname = None):
        if fname and lname:
            self.value = f"Two arguments fname & lname: {fname},{lname}"
        elif fname:
            self.value = f"one Argument: {fname}"
        else:
            self.value = "No Argument"

obj1 = A()   # Constructor without argument
obj2 = A("Yogesh") # Constructor with one argument
obj3 = A("Yogesh","Tyagi")  # Constructor with two argument


print(obj1.value)
print(obj2.value)
print(obj3.value)

"""
# Lecture No - 12

# Python => Import & From Import
# Python Module

# Lambda Function

# Import if you want to access any python => 2 class [A & B], 2 method in each class
# from Import => Importing Class A => only we will be able to access the limited things

# ==================>

# Python File => .py =>
# Python Module => Python File => .py

# =>Reusability of code =>

"""
# class -1

class A:
    def __init__(self):
        print("This is a class constructor")

    def methodForClassA(self):
        print("This is a class A Method")
        print("My First Class")

# Class 2

class B:
    def __init__(self):
        print("This is B class constructor")

    def methodForClassB(self):
        print("This is a class B Method")
        print("My second Class Method")

class C:
    print("class")

    def mul(self,a,b):
        c=a*b
        print("This is my method: Multiplication: " + str(c))



import CommonModule

objA = CommonModule.A()
objA.methodForClassA()

objB = CommonModule.B()
objB.methodForClass()



from CommonModule import A

objA = A()
objA.methodForClass()

"""



# You are going to use this file somewhere else means this is working as an module
# You can right the code at any places whatever you want but you will be importing one file as somewhere else
# then whatever file you going to import that will be working as python module


# Python File
# Definition: A Python file is simply a file that contains Python code. These files have a .py extension.
# Usage: Python files are used to write scripts, functions, classes, and other code that can be executed or imported.
# Examples: script.py, program.py, example.py

# Python Module

# Definition: A Python module is a file containing Python code that can be imported and used
# in other Python programs. A module can include definitions of functions, classes, and variables,
# as well as runnable code.
# Usage: Modules are used to organize and reuse code. They allow you to structure your
# code in a logical way and make it easier to maintain and debug.

# Examples: Any Python file can be a module if it is intended to be imported and used
# in other code. For instance, mymodule.py can be imported using import mymodule.

# Key Differences
# Purpose: While all Python modules are Python files, not all Python files are
# intended to be modules. A file may be a standalone script meant to be executed directly.

# Usage: Modules are specifically designed for reuse and are typically imported
# into other scripts using the import statement.


# Lambda Function
# Add two numbers
# add lambda a,b: a+b
# print (add (10,20))

# Multiplication => passing two arguments

# multi lambda a, b a*b

# print (multi (5,4))

# Multiplication => Single argument

# multi lambda a: a*a
# print (multi (10))

# Default values
# add lambda a,b=1: a+b
# print(add (30))
# print(add (10,20))

# lambda function in map()

# num= [1,2,3,4,5,6,7,8]

# squre map (lambda x: x**2, num)
# even_number = filter (lambda x: x 2 0, num)
# print (list(even_number))

# lambda inside a function

# def multiplication(a):
#     return lambda x: x*a

# f_times multiplication (5)
# t times multiplication (3)
# print (f_times (10))
# print(t_times (3))

# compare two values with lambda function
# data lambda x,y: x if x>y else y
# print (data (10,30))


# Lecture No - 12


# Exception handling in python (Try, Except)
# Exception handling purpose

# while executing any code if we get any error in runtime.this type of

# try:
#     num1 = input("Please enter first number: ")
#     num2 = input("Please enter second number: ")
#     c = int(num1) + int(num2)
#     print(c)
#
# except:
#     print("Your input is incorrect, Please enter correct data")
#
# finally:
#     print("This code i want to execute at the end always")

# ----- Exceptions-------------

# 1.End of file Exception: EOFError
# 2.IO Error
# 3.Index Error: 1,2,3,4 => 50
# 4.ImportError: python file is not available
# 5.ImportError:That functionality is not available
# 6.TypeError
# 7.ZeroDivisionError:
# 8.KeyboardInterrupt:
# 9.KeyError


# FileHandling
# from os import write

# ETL Projects
#
# Source:
#     1. CSV File
#     2. XML File
#     3. DB Table => Oracle
#     4. Parquet File

# Staging:
#    1.Load Data in Staging Tables => SQL Server

# Target:
#    1.Target [DWH]

# => Process to handle a file =>
# => Shared Location => Can? I download and place at server location?

# File is available at our own shared location:

# Your VDI => Yes
# Your Automation Server => Fails

# Your Automation Server => Good to execute your

# if code...:

# text file
# ABC.TXT =>

# open ("Complete directory", "r")

# c drive: folder1=>folder2 => folder3 => folder4 => test.txt
# my system => C drive direct file => test.txt

# open("c:\test.txt","r")

# myfile= open("c:\folder1\folder2\folder3\folder4\test.txt","r")

# => r => ready only
# => w => write only
# => a => append

# => read & write => r+
# => write & read => w+, a+

# myfile.close()

# Open file => try to access that file =>

# -=-=-=-=-=-==> Performing operations

# Creating a file in C:\Python Source file => source file => csv file

# EmpID, Name, Salary, City

# 101, Test, 50000, Noida
# 102, abc, 55000, Delhi

# Requirement#1 => Read Data from file
# Requirement#2 => Add two more rows in source file
# Requirement#3 => Append data in Name column

# EmpID, Name, Salary, City
# 101, 101 Test, 50000, Noida
# 102, 102_abc, 55000, Delhi

# => open() => will open the file with command

# => read() => will help to read data from file

# => Steps to read data:

# Step#1 => Open a file with command
# Step#2 => create an object of that file or variable => obj
# ======>Step#3 => read() => obj.read() => obj.readline() --(In 3rd step operation will perform)
# step#4 => close() => obj.close()

# so here we are used r seprate from this Double coat path means r will take row wise data.

# myfile = open(r"C:\Python\MySourceFile.csv","r")
# filedata = myfile.read()
# print (filedata)
# myfile.close()

# myfile = open(r"C:\Python\Employees.xlsx","r")
# filedata = myfile.read()
# print (filedata)
# myfile.close()


# Lecture No - 13

# will read from CSV
# Database

# PANDAS-
# PIP => is responsible to install Python libraries in your system.
# installing package => database, pandas
# SQL Server =>pyodbc => install


# import pyodbc
# print("pyodbc is installed and imported successfully!")



# Lecture No -15

# Python Library

# 1. Data Analytics
# 2. Data Manipulation
# 3. Automation

# Install pandas => cmd => pip

# lst = ['amit','Harsh','punit']

# dataframe
# Create DataFrame

# import pandas as pd
# list = [500,2000,5000,8000]
# print(list)
# df = pd.DataFrame(list)
# print(df)

# list of list
# import pandas as pd
# list1 = [101,'Amit','Noida',50000],[102,'Harsh','Delhi',65000],[103,'Kiran','Gurgaon',70000]
# print(list1)

# df = pd.DataFrame(list1)
# df = pd.DataFrame(list1,columns=['EMPID','NAME','CITY','SALARY'])
# df = pd.DataFrame(list1,index=['Row1','Row2','Row3'])
# df = pd.DataFrame(list1,columns=['EMPID','NAME','CITY','SALARY'],index=['Row1','Row2','Row3'])
# print(df)

# Create DataFrame on Dictionary
# import pandas as pd
# data = {'Name':['Kiran','Harsh','Prakash','Manish'],
#        'Marks':[450,455,560,470]}

# df =  pd.DataFrame(data)
# print(df)

# List using Dictionaries

# list2 = [ {'EmpID':100,'Name':'Amit','City':'Noida','Salary':5000},
#           {'EmpID':101,'Name':'Manish','City':'Delhi','Salary':55000},
#           {'EmpID':102,'Name':'Kiran','City':'Pune','Salary':6000},
#           {'EmpID':103,'Name':'Harsh','City':'HYD','Salary':7000}]

# import pandas as pd
# df = pd.DataFrame(list2)
# print(df)

# Multiple list and combine those list together

# listEID = [101,102,103,104,105]
# listEname = ['Amit','Manish','Kiran','Harsh','Abha']
#
# list5 = list(zip(listEID,listEname))
# print(list5)


# from functions.readcsv import mismatch

# Requirement
# CSV =
# Table =

# All failures/mismatches => write in a file

# source => csv file
# Target => database table

# import => pandas, pyodbc

# read data from csv

# setup connect with DB =>

# list []


# same data between source & target => no failures
# => ?
# => ?

# Failures in a list

# dataframe for a list[failure]
# write all failure in csv

# import pyodbc
# import pandas as pd
#
# read data from csv file
# csv_file = r'C:\Python\data.csv'
# data_csv = pd.read_csv(csv_file)
# print(data_csv)
#
# setup database connection
# my_conn = (
#       r'DRIVER={ODBC Driver 17 for SQL Server};'
#       r'SERVER=DESKTOP-2EGJ017;'
#       r'DATABASE=master;'
#       r'Trusted_Connection=yes;'
# )

# conn = pyodbc.connect(my_conn)
# query = 'select * from employee_2'
# data_db = pd.read_sql(query,conn)
# print(data_db)
#
# data comparison started
# mismatches = []

# for index, row in data_csv.iterrows():              # here we compared row wise
#     db_row = data_db[data_db['EID'] == row['EID']]  # here csv file and data table both side compared(key column)
#     if db_row.empty:
#         mismatches.append(row.to_dict())
#     else:
#         for col in data_csv.columns:                # here we compared column wise
#             if row[col] != db_row.iloc[0][col]:   # it will start from zero index till the last column
#                 mismatches.append(row.to.dict())
#                 break
#
# create dataframe for mismatches # Dataframe is nothing get the data in row and column format in two dimentional error
# df = pd.DataFrame(mismatches)
# df.to_csv(r'c:\Python\mismatchrec.csv')
#
# print("Data comparison is completed and mismatches has been written in csv file")



