# print("HelloWord")

# Identifiers

# Identifiers in python are the names you give to variables, functions, classes & other objects in your code.
# A name in Python program is called Identifiers.
# It can be Variable name,Module name,Function name,Class name.
# Identifiers should not start with digit.

# Rules to define Identifiers in python:-
# --------------------------------------

# 1.The only allowed characters in python are:-

# -> Alphabet symbols(either lower case or upper case).
# -> digits(0 to 9)
# -> underscore symbol(_)

# ex:-

# pay_bill = 2000
# print(pay_bill)
# 2000


# pay&bill = 2000
# SyntaxError: cannot assign to operator
# 2.Identifiers should not start with digit.

# _pay_bill = 2000
# print(_pay_bill)
# 2000

# 100_pay_bill = 2000
# SyntaxError: invalid decimal literal


# 23/10/2021
# ----------
#            Reserved words or keywords
#            -------------------------
# In python some words are reserved to represent some meaning or functionality.
# such type of words are called Reserved words.

# In python there are 35 reserved words are represent.

# import keyword
# print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else','except', 'finally', 'for', 'from', 'global', 'if', 'import',
# 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
#  'return', 'try', 'while', 'with', 'yield']

# Note:-
# 1.All Reserved words in python contain only alphabet symbols.
# 2.Except The True,False and None  reserved words,all contain only lower case alphabet symbol.

# Data Types
# ----------
# Data Type represent the type of data present inside a variable.
# in python we are not required to specify the type explicitly.
# Based on value provided,the type will be assigned automatically.
# hence python is dynamically typed language.

# In python there are 14 data are present:-

# 1.int 		:- Integer
# 2.float		:- Float
# 3.complex  	:- Complex
# 4.bool 		:- Boolean
# 5.str 		:- String
# 6.bytes 	    :- Bytes
# 7.bytesaary   :- Bytearray
# 8.range 	    :- Range
# 9.list	    :- List
# 10.tuple	    :- tuple
# 11.set 		:- Set
# 12.frozenset  :- Frozenset
# 13.dict 	    :- Dictionary
# 14.None		:- None

# Note:- All data types also python in-built function,we can use these function for base conversation.
#        Only None  represent the In-built func,keyword and data type also.


# None is indeed a unique and significant element in Python. Here’s how it fits into the different
# categories you mentioned:

# Keyword:

# None is a reserved keyword in Python. It is used to define a null value or "no value at all."

# Data Type:

# None has its own type called NoneType. You can check its type using the type() function:

# python
# print(type(None))  # Output: <class 'NoneType'>
# Built-in Function:

# None itself is not a built-in function. However, it is a special value that can be returned by
# functions when there is no specific value to return.
# So, while None plays a crucial role in Python as a keyword and a data type, it's not classified
# as a built-in function. Here’s an example of how None is used:

# python
# def my_function():
#     return None

# result = my_function()
# if result is None:
#     print("The function returned None")

# identity of the object a
# a = 10
# print(id(a))
# --> 140719173593816

# print(id(10))
# --> 140719173593816

# a = 20
# b = 20
# print(id(a))
# --> 140719173594136
#
# print(id(b))
# --> 140719174970392

# Garbage collector:-
# -----------------
#
# The process by which python periodically frees and reclaims block of memory that no longer are in use is
# called Garbage collection.
# Python garbage collector runs during program execution and is triggered when on object's reference count
# reaches zero.

# memory location
# a =10
# print(a)
# -->10
# a = 20
# print(a)
# 20
#
# Several In-built function:-
# -------------------------

# 1.type():- To check the type of variable:- which type of data is indicated a variable

# >>> a =10
# >>> type(a)
# <class 'int'>
# >>>

# 2.id() :- Track the location of data or variable.

# a =10
# print(id(a))
# -->2889387764304
# print(id(10))
# -->2889387764304


# 3.print():- To print the value

# a =10
# print(a)
# -->10

# 4.dir():-

# 5.help():-


#  26/10/2021
# ----------

# Integer(int data type):-
# -----------------------

# we can use int data type to represent whole numbers(Integral Value).

# >>> a = 100
# >>> type(a)
# <class 'int'>

# >>> b = -100
# >>> type(b)
# <class 'int'>

# Base Conversion:-
# ----------------

# we can represent int values in the

# 1.Decimal Form
# 2.Binary Form
# 3.Octal Form
# 4.Hexa Decimal Form

# 1.Decimal Form(Base-10):-
# ---------------

# It is the default number system in python.
# The allowed digits are:- 0 to 9
# int to decimal :- float()---data type

# a = 12
# print(type(a))
# --><class 'int'>

# b = float(a)
# print(b)
# 12.0
# type(b)
# <class 'float'>


# 2.Binary Form(Base-2):-
# -----------------
# The allowed digits are:- 0 and 1
# Literal value should be prefixed with 0b or 0B
# int to binary :- bin()

# >>> a = 10
# >>> b = bin(a)
# >>> b
# '0b1010'

# 3. Octal Form(Base-8):-
# ---------------
# The allowed digits are :- 0 to 7
# Literal value should be prefixed with 0o or 0o.
# int to octal :- oct()

# >>> a = 100
# >>> b = oct(a)
# >>> b
# '0o144'

# 4.Hexa Decimal Form(Base-16):-
# --------------------

# The allowed digits are:- 0 to 9 , a-f (both lower and upper case)
# Literal value should be prefixed with 0x and 0X
# int to Hexa decimal :- hex()

# >>> a = 100
# >>> b = hex(a)
# >>> b
# '0x64'
# we can use float data type to represent floating point values(decimal values).

# Indexing:-
s = 'Scodeen'
# print(s[0:3])

# print(s[4:])

# print(s[:3])

# -->Sco
# -->een
# -->Sco

# print(s[-6:-2])
# code
# print(s[-1:-5]) --No Result



# l = [10,20,30,40,50]
# print(dir(l))
# print(len(l))
#
# print(l.index(10))

# 5.extend():- To add all items of one list to another list.

l1= []
l2 = []

print(l1.extend(l2)) #:- l2 items will be added to l1

# l2.extend(l1):- l1 items will be added to l2

# Important Function of list:-
# 1.count():- It returns the number of occurrence on specified item in the list.
# 2.index():- Returns the index of the first occurrence of the specified item.
# 3.append():- we can use append() to add item at the end of the list.
# 4.insert():- To insert at specified index position.
# 5.extend():- To add all items of one list to another list.
# 6.remove():- we can use this function to remove specified item from the list.
#              If the item present multiple times then only first occurrence will be removed.
# 7.pop():- It removes and returns the last element of the list.
#           This is only function which manipulates list and returns some element.
# 8.clear():- It's clear the all data from respective list.
# 9.copy():- copy the same data from another list.
# 10.reverse:- we can use to reverse() order of element list.
# 11.sort():-  In list by default insertion order is preserved.If want to sort the elements of list
#              according to default natural sorting order then we should go for sort() function.


# s = (1,2,3,4)
# print(type(s))
# print(dir(s))
# [count', 'index']
