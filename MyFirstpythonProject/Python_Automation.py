# Procedural programming Paradigm
# add 2 numbers
# a = 10
# b = 20
# c = a+b
# '''
import pandas as pd

# print("addition of two numbers is :",c)
# a = 100
# b = 200
# c = a+b

# print("addition of two numbers is :",c)

# Functional programming Paradigm
# add 2 numbers

# def addTwonumbers(num1,num2):
# sum = num1+num2

# print("addition of 2 numbers is :",sum)
# addTwonumbers(10,20)
#  addTwonumbers(-4,14)
#  '''

# Object Oriented programming Paradigm
# class OOPway:
# def addTwonumbers(self,num1, num2):
# sum = num1 + num2
# print("addition of 2 numbers is :", sum)
# ref = OOPway()
# ref.addTwonumbers(100,500)

# Indentation
# Python uses indentation to define blocks of code. Unlike other programming languages that use
# braces {}, Python uses indentation level to indicate a block of code.
# Consistent use of spaces or tabs is crucial. The convention is to use 4 spaces per indentation
# level.
# for i in range(10):
# print(i)
# Variables:
# Variables are containers for storing data values. Python has no command for declaring a variable. A
# variable is created the moment you first assign a value to it.
# e.g.
# In Java :    int age = 18;
#  In Python :    age = 18
#  Variable naming conventions:
#  For muti name variable we can use various technique to name the variable. Either of this can be used
#  o Camel case: each word starts with Upper case except first word
#  e.g. myFirstName = “Hetu”
#  o Pascal case: each word starts with Upper case.
#  e.g. MyFirstName = “Hetu”
#  o Snake case: each word separated by underscore
#  e.g. my_first_name = “Hetu”
#  Type Casting :
# Coverts the data in to a specific data type
#  Age = int(18)
#  O/P => 18
#  Weight = float(18)
#  O/P => 18.0
#  X = str(3)     
#  O/P => ‘18’
#  Check data type of a variable:
#  Type(age)
#  If Statement
#   Purpose: Executes a block of code if the condition is True.
#  x = 10
#  if x > 5:
#  print("x is greater than 5")
#  Else Statement
#   Purpose: Executes a block of code if the if condition is False.
#  x = 2
#  if x > 5:
#  print("x is greater than 5")
#  else:
#  print("x is not greater than 5")
#  Elif (Else If) Statement
#   Purpose: Checks multiple conditions, and executes a block of code for the first True condition.
#  x = 10
#  if x < 5:
#  print("x is less than 5")
#  elif x == 10:
#         print("x is 10")
#  else:
#         print("x is greater than 5 but not 10")
#  For Loop
#   Purpose: Iterates over a sequence (list, tuple, string, or range) and executes a block of code for
# each item.
#       e.g.
#             for i in range(5):    # Iterates over numbers from 0 to 4
#                 print(i)
#  While Loop
#   Purpose: Repeats a block of code as long as the condition is True.
#  e.g.
#  i = 0
#  while i < 5:
#         print(i)
#         i += 1
#  Assignment # 1
#  1. Write a Python program that calculates the factorial of a given number n (n!) using both a for loop
# and a while loop.
#  Example:
#      Input: n = 4
#  Output: 24
#  Explanation: (4! = 4 × 3 × 2 × 1 = 24)
# 2. Write a Python program that finds and prints all the prime numbers between 1 and N using both a
# for loop and a while loop.
#  Example :
#  Input:  N = 10
#  Output: 2 3 5 7
#  Explanation: (Prime numbers between 1 and 10 are 2, 3, 5, and 7)
#  1. Write a Python program that counts the number of digits in a given number using both a for
# loop and a while loop.
#  Example :
#  Input: n = 12345
#  Output: 5
#  Explanation: (Number of digits in 12345 is 5)
#  4. Write a Python program that calculates the sum of the first N natural numbers (1 + 2 + 3 + ... + N)
# using both a for loop and a while loop.
#  Example
# Input: N = 5
#  Output: 15
#  Explanation: (Sum of 1 + 2 + 3 + 4 + 5 = 15)

#  5. Write a Python program that generates the Fibonacci series up to N terms using both a for
# loop and a while loop.
#  Example
#  Input: N = 6
#  Output: 0 1 1 2 3 5
#  Explanation: (The first 6 terms of the Fibonacci series are 0, 1, 1, 2, 3, and 5)
#  Code from Pycharm for your reference
# Variable used to store values ( data elements )
# '''

# nameofstudent = "Abhinav"
# ageOfStudent = 25
# elligible_for_vote = True
# '''

# Naming conventions
# 1) Camel Case : each word starts with upper case except first word
# e.g. nameOfStudent = "Abhinav"
# 2) Pascal Case : each word starts with upper case
# e.g. NameOfStudent = "Abhinav"
# 3) Snake Case : each word will be seperated by _
# e.g. name_of_student = "Abhinav"
# '''

# nameOfStudent = "Abhinav"
# ageOfStudent = 25
# elligible ForVote = True
# print("Studnet name is :",nameOfStudent," and Age of the Student is :",ageOfStudent,
# " and student is ellibigle for voting : ",elligibleForVote)
# Type Casting ( converting data from one to another type ) e.g. string value to int
# age = "25"
# age_of_student = 25
# print("Age is of type : ",type(age))
# print("Age of Student is of type : ",type(age_of_student))
# convert the age from string type to integer
# age_converted =    int(age)
# print("converted Age is of type : ",type(age_converted))
# marks1 = "50"
# marks2 = "60"
# total_marks = marks1 + marks2
# print("Total marks : ",total_marks)
# total_marks_conv = int(marks1) + int(marks2)
# print("Total marks converetd    : ",total_marks_conv)
# upcasting ( converting lower data type to higher data type )
# weight_of_person_int = 75
#  print("Weight is float ",float(weight_of_person_int))
# downcasting ( converting higher data type to lower data type )
# weight_of_person_float = 75.8
# print("Weight is int ",int(weight_of_person_float))
# Control Statements ( if..else..elif ( else if ) )
# if statement
# age = 20
# if age > 18:
# print("Person is eliigible for voting")
# if . else    statement
# age = 18
# if age >=18:
# print("Person is eliigible for voting")
# else:
# print("Person is not eliigible for voting")
# if . elif statement
# age = 110
# if age < 18:
# print("Person is not elligible for voting")
# elif age >=18 and age < 95:
# print("Person is eliigible for voting")
# else:
# print("Person is super senior citizen..")
# Print ETL QA labs 10 times
# print("ETL QA Labs")
# print("ETL QA Labs")
# print("ETL QA Labs")
# print("ETL QA Labs")
# print("ETL QA Labs")
# print("ETL QA Labs")
# print("ETL QA Labs")
# print("ETL QA Labs")
# print("ETL QA Labs")
# print("ETL QA Labs")
# Using FOR loop

# range(10) => starts from 0 and goes up to 10-1 (9) . 0 to 9 = 10 times
# for val in range(1,10):
# print(val,": ETL QA Labs")
# while (Execute until its true )
# print("While loop demo :")
# start = 1
# end = 10
# while ( start < end ):
# print(start, ": ETL QA Labs")
# start = start + 1

# Data types available in Python
#  Text Type: str
#  Numeric Types: int, float
#  Sequence Types:

# List: A list is an ordered collection of items that can be changed (mutable). You can
# store different types of data in a list.
#  e.g. x = ["Ram", "Shyam", "Ghanshyam"]
# Accessing elements by index
# print(x[0])    # Output: Ram
# Adding elements
# x.append("Mohan")
# print(x)    # Output: ['Ram', 'Shyam', 'Ghanshyam', 'Mohan']
# Removing elements
# x.remove("Shyam")
# print(x)    # Output: ['Ram', 'Ghanshyam', 'Mohan']
# List slicing
# print(x[1:])    # Output: ['Ghanshyam', 'Mohan']
# tuple: A tuple is an ordered collection of items that cannot be changed (immutable).
# e.g. x = ("Ram", "Shyam", "Ghanshyam")
# Accessing elements by index
# print(x[1])    # Output: Shyam
# Tuples are immutable, so this would raise an error:
# x[0] = "Mohan"    # TypeError: 'tuple' object does not support item assignment
# Range : A range represents a sequence of numbers generated by the range() function,
# often used in loops.
#  x = range(10)
# Converting range to a list to see the numbers
# print(list(x))    # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Range with start, stop, and step
# x = range(2, 10, 2)
# print(list(x))    # Output: [2, 4, 6, 8]
# range: A range represents a sequence of numbers generated by the range() function,
# often used in loops.

#  range(10)

#  Here are practical examples for each of the sequence types, mapping types, and
# boolean type in Python. These examples will demonstrate how you can work with each
# type in real-world scenarios.
#  Set Types: A set is an unordered collection of unique items. Sets do not allow
# duplicate values.

#  Set:
# Example: Set
# x = {"Ram", "Shyam", "Ghanshyam"}
# Adding elements
# x.add("Mohan")
# print(x)    # Output: {'Ram', 'Shyam', 'Mohan', 'Ghanshyam'}
# Removing elements
# x.remove("Shyam")
# print(x)    # Output: {'Ram', 'Mohan', 'Ghanshyam'}
# Checking if an element is in the set
# print("Ram" in x)    # Output: True
# Sets do not allow duplicates:
# x.add("Ram")
# print(x)    # Output: {'Ram', 'Mohan', 'Ghanshyam'} (no duplicates)
# city_set = {"New Delhi","Kolkata","Mumbai","Chennai"}
# other_cities = {"Pune","Kolkata","Hyderabad","Chennai"}
# 1. Union ( | or .union() )
# Combines all unique elements from both sets.
# print(city_set | other_cities)                       
# print(city_set.union(other_cities))             
# Output:
# Using operator
# Using function
# {'New Delhi', 'Kolkata', 'Mumbai', 'Chennai', 'Pune', 'Hyderabad'}

# 2. Intersection ( & or .intersection() )

# Elements common in both sets.
# print(city_set & other_cities)
# print(city_set.intersection(other_cities))
# Output:
# {'Kolkata', 'Chennai'}

# 3. Difference ( - or .difference() )

# Elements in one set but not in the other.
# print(city_set - other_cities)                       
# print(city_set.difference(other_cities))
# Output:
# {'New Delhi', 'Mumbai'}

# 4. Symmetric Difference ( ^ or .symmetric_difference() )

# Elements in either set but not in both.
# print(city_set ^ other_cities)                       
# print(city_set.symmetric_difference(other_cities))
# Output:
# {'New Delhi', 'Mumbai', 'Hyderabad', 'Pune'}
# Other Useful Set Functions
# city_set.add("Bangalore")           
# city_set.remove("Mumbai")           
# city_set.discard("Surat")           
# Add a new element
# Remove element (Error if not found)
# Remove element (No error if not found)
# city_set.pop()                                 
# city_set.clear()                             
# Remove & return a random element
# Empty the set
# Boolean Type: A boolean type represents True or False. It is typically used to
# represent binary conditions, like comparisons and logical operations.
# Example: Boolean
# x = True
# y = False
# Logical operations
# print(x and y)    # Output: False
#  print(x or y)     
# print(not x)       
# Output: True
# Output: False
# Boolean values in conditional statements
# if x:
# print("x is True")    # Output: x is True
# if not y:
# print("y is False")    # Output: y is False

# List vs Tuple:
# 1. Mutability
# List: Mutable. You can change, add, or remove elements after the list is created.
# Tuple: Immutable. Once a tuple is created, its contents cannot be modified.

# 2. Syntax
# List: Defined using square brackets [].
# my_list = [1, 2, 3]
# Tuple: Defined using parentheses ().
# my_tuple = (1, 2, 3)

# 3. Performance
# List: Generally slower than tuples due to their mutability and the additional overhead for
# dynamic resizing.
# Tuple: Faster than lists for iteration and access due to their immutability.

# 4. Methods
# List: Comes with a variety of methods for manipulation, such
# as .append(), .remove(), .extend(), and more.

# Tuple: Has fewer built-in methods, primarily .count() and .index().

# 5. Use Cases
# List: Use when you need a collection of items that can change over time (e.g., a dynamic
# list of user inputs).
# Tuple: Use when you need a fixed collection of items (e.g., coordinates or pairs of
# values) or when you want to ensure that the data cannot be modified.

# 6. Storage
# List: Typically uses more memory because it needs to support dynamic resizing.
# Tuple: More memory-efficient for storing a fixed number of items.

# List vs Set:
# 1. Mutability
# List: Mutable. You can change, add, or remove elements after the list is created.
# Set: Mutable as well

# 2. Order
# List: Ordered. The items maintain their insertion order, allowing duplicate elements.
# Set: Unordered. The items do not maintain any specific order, and duplicate elements
# are not allowed.

# 3. Syntax
# List: Defined using square brackets [].
# my_list = [1, 2, 3]

# Set: Defined using curly braces {} or the set() constructor.
# my_set = {1, 2, 3}

# 4. Performance
# List: Generally slower for membership tests (checking if an item is in the list) because it
# may require scanning through all elements.
# Set: Faster for membership tests due to its underlying hash table implementation.
# 5. Methods

# List: Comes with methods for manipulation, such as .append(), .remove(), .extend(), and
# more.
# Set: Has methods specific to set operations,
# like .add(), .remove(), .union(), .intersection(), etc.

# 6. Use Cases
# List: Use when you need a collection of items that can contain duplicates and where
# order matters (e.g., a list of tasks).

# Set: Use when you need a collection of unique items and don’t care about order (e.g., to
# track unique user IDs).

# How to write and execute ( call ) a function that does not return any valuein Python
# define the function

# def display():
# print(" i am inside the function : Line 1")
# print(" i am inside the function : Line 2")
# print(" i am inside the function : Line 3")
# print(" i am inside the function : Line 4")
# Execute (Calling) a function
# display()
#  How to write and execute ( call ) a function that returns values in Python
# define the function
# def getLength():
# name = "ETL QA Labs"
# return len(name)
# Execute (Calling) a function
# size =    getLength()
#  print(size)
#  Code from today’s class
# Collection/Sequence data types
# '''
# List:

# a) ordered collection of items ( the order in which data is stored)
# b) Mutable ( which can be changed )
# c) Insertion order is preserved
# d) It can store duplicate values
# e) In python, we use []
# f) e.g. name_of_student = ["Malthi","Aarti","Abhinav","Malthi"]
# Tuple
# a) ordered collection of items ( the order in which data is stored)
# b) Immutable ( once created can not be changed )
# c) Insertion order is preserved
# d) It can store duplicate values
# e) In python, we use ()
# f) e.g. name_of_student = ("Malthi","Aarti","Abhinav","Malthi")

# Set

# a) un-ordered collection of items ( the order in which data is stored)
# b) Mutable ( once created can be changed )
# c) Insertion order is not preserved
# d) It can not store duplicate values
# e) In python, we use {}
# f) e.g. name_of_student = {"Malthi","Aarti","Abhinav"}
# List methods/functions
# name_of_students_list = ["Malthi","Aarti","Abhinav","Malthi"]
# datatype check
# print(type(name_of_students_list))
# print(name_of_students_list)
# Display each elements/items form the list
# print("Hello ! welcome ",name_of_students_list[0])
# print("Hello ! welcome ",name_of_students_list[1])
# print("Hello ! welcome ",name_of_students_list[2])
# print("Hello ! welcome ",name_of_students_list[3])
# using for loop
# name_of_students_list = ["Malthi","Aarti","Abhinav","Malthi"]
# range(0,4,1) equailvalent range(4)
# range(1,10,2) => 1,3,5,7,9
# Way 1:
# for idx in range(0,4,1):
# print("Hello ! welcome ",idx,":",name_of_students_list[idx])
# Way2 :
# for item in name_of_students_list:
# print(item)
# Add "Rakesh" in the list
# name_of_students_list = ["Malthi","Aarti","Abhinav","Malthi"]
# print("Before adding Rakesh .....",name_of_students_list)
# name_of_students_list.append("Rakesh")
# print("After adding Rakesh.....",name_of_students_list)
# remove "Aarti" from list
# print("Before removing Aarti .....",name_of_students_list)
# name_of_students_list.remove("Aarti")
# print("After adding Aarti.....",name_of_students_list)

# List slicing

# name_of_students_list = ["Malthi","Aarti","Abhinav","Malthi","Rakesh","Thomas","Pankaj"]
# Get me first 3 items from list and store in another list ( idx : 0,1,2 )
# way 1
# ans_list = []
# for idx in range(0,3,1):
# ans_list.append(name_of_students_list[idx])
# print(ans_list)
# way 2 list slicing ( similar to range( startindex, endIndex, steps )
# syntax : list_name[startIndex:endIndex:steps]
# print("Using slicing operator ",name_of_students_list[0:3:1])

# Tuple
# name_of_students_tuple = ("Malthi","Aarti","Abhinav","Malthi")
# print(type(name_of_students_tuple))
# occurence_of_an_element = name_of_students_tuple.count("Malthi")
# no_of_elements = len(name_of_students_tuple)
# print(no_of_elements)

# Set
# name_set1 = {"Ram","Shyam","Rakesh"}
# name_set2 = {"Ram","Shyam","Ghanshyam"}
# print("Before : ", name_set1)
# name_set1.add("Shyam1")
# print("After : ", name_set1)
# Union
# ans_set =    name_set1.union(name_set2)
# print(ans_set)
# Interection
# ans_set =    name_set1.intersection(name_set2)
# print(ans_set)
# Difference
# ans_set =    name_set1.difference(name_set2)
# print(ans_set)
# ans_set =    name_set2.difference(name_set1)
# print(ans_set)
# symmetric Difference ( set1 - set 1 union    set2 - set1 )
# ans_set =    name_set1.symmetric_difference(name_set2)
# print(ans_set)
# '''
# get me first 3    and last 3 elements    from the list
# first 3 elements will be at indexes = 0,1,2
# last 3 elements will be at indexes = n,n-1,n-3 (10,9, 8)
# list_numbers = [1,2,3,4,5,6,7,8,9,10,"Akash"]
# ans = []
# f
# irst_list = list_numbers[0:3:1]
# last_list = list_numbers[7::1]
# print(first_list)
# print(last_list)
# ans = first_list+last_list
# print("answer list : ",ans)
# print("Before : ",list_numbers)
# list_numbers[1] = 100
# print("After : ", list_numbers)
# Assignments 2:
# 1. Write a function to return the grade based on percentage
# 2. Write a function that return a list of common elements from two different sets
# 3. Convert a String to a List of Characters
# 4. Write a function to check if list contains any duplicate element and return True or False as
# applicable
# 5. Given a list, write a function that provide the occurrence of element against each element
# in the list.

# e.g. List = [1,2,3,4,5,1,3]

#       Expected Output:
#         1: 2
#         2:1
#         3: 2
#         4: 1
#         5: 1
#  6. Write a function return a substring where it starts from 2rd occurrence of ‘a’ and end at

# occurrent of ‘b’
# e.g. s = "abracadabra"
# start_char = 'a'
# end_char = 'b'
# Expected output: acadab
# Assignments 3:

# 1. Given a string , write a python code to reverse the string using for loop and slice operator both
# ways?

# Input: city = "ETLQALabs"
# expected output: “sbaL AQ LTE”
# 2. Extract a substring form character "Q" and ends at "b"
# Input: city = "ETLQALabs"
# Expected O/P : QAlab
# 3. Write a python code to check if the given list contains duplicate elements and print yes or no as
# per input
# e.g.
# list1 =[1,2,3,4,3] => Yes
# list2 =[1,2,3,4] => No

# 4. How would you use slicing to create a new list containing only the odd-indexed elements of a
# given list?

# Input : list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected output : [1, 3, 5, 7, 9]

# 5. How would you use slicing to create a new list containing only the even-indexed elements of a
# given list?

# Input : list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected output : [0, 2, 4, 6, 8]

# Data type Dictionary
my_dict = {'name':'Mayank', 'age':35,'city':'Bangalore'}
# print(my_dict)

# Accessing a value using a key
# print(my_dict['name'])

# Accessing a value using the .get() method
# print(my_dict.get('age'))

# Adding a new key-value pair
# my_dict['gender'] = 'Male'

# Modifying an existing key-value pair
# my_dict['age'] = 26
# print(my_dict)

# Removing a specific key-value pair using del
# del my_dict['city']
# print(my_dict)

# Removing a key-value pair using pop
# age = my_dict.pop('age')

# Removing and returning the last key-value pair using popitem
# last_item = my_dict.popitem()

# Iterating over keys
# for key in my_dict:
#    print(key)


# Iterating over values
# for value in my_dict.values():
#     print(value)

# Iterating over key-value pairs
# for key, value in my_dict.items():
# print(key, value)

# Write a function that doesn’t return but print the max number from the list
#def getMax(list1):
#    max = list1[0]
#    for num in list1:
#        if num > max:
#            max = num
#    print(max)

# getMax([1, 4, 3, 19, 5])

# Store the returned value and add 100 to it and print
# def getMax(list1):
#    max = list1[0]
#    for num in list1:
#        if num > max:
#            max = num
#    return max

# maxinumber = getMax([1,4,3,19,5])
# print(maxinumber+100)




#df  = pd.read_csv("venv/employee_data.csv")
#print(df)




# Functions in Pandas:
# 1.Reading CSV Files[by default delimiter is comma(,)]

# df = pd.read_csv("venv/employee_data.csv",usecols=['A','B','C'])
# print(df_preview.columns)

