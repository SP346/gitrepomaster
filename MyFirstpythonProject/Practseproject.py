# variables
from csv import DictReader

# a = 10
# first_name = 'Sourabh'
# last_name = 'Patil'
# age = 28

#print(a)
#print(b)
#print(c)

# Req No-2  --> My First name is sourabh and last name is patil and my age is 27
# print("my first name is "+first_name+" and my last name is " +last_name+" and my age is "+str(age))

# user defined values
# Data = input("Please enter the number: ")
# print(Data)
# print("My age is: " +Data)


# Garbage collector
# a = 10
# print(id(a))
# --> 140715045087960

# a = 10
# print(a)

# a = 20
# print(a)
#  --> 20


# Several In-built function:-

# a = 10
# print(type(a))
#
# a = 10.10
# print(type(a))
#
# <class 'int'>
# <class 'float'>

# 2.id() :- Track the location of data or variable.
#
# >>> a =10
# >>> print(id(a))
# 2889387764304


# 3.print():- To print the value
#
# >>> a =10
# >>> print(a)
# 10
#
# 4.dir():-
#
# 5.help():-
#

# Integer(Int Data Type);-

# a = 45
# print(type(a))
#
# b = -100
# print(type(b))

# --><class 'int'>
# --><class 'int'>


# we can represent int values in the
#
# 1.Decimal Form
# 2.Binary Form
# 3.Octal Form
# 4.Hexa Decimal Form
#


# 1.Decimal Form(Base-10):-
# ---------------
#
# It is the default number system in python.
# The allowed digits are:- 0 to 9
# int to decimal :- float()---data type

# a = 10
#
# b = float(a)
# print(type(b))
# print(b)
#
# --> <class 'float'>
# --> 10.0



# 2.Binary Form(Base-2):-
# -----------------
#
# The allowed digits are:- 0 and 1
# Literal value should be prefixed with 0b or 0B
# int to binary :- bin()
#
# a = 10
# b = bin(a)
# print(type(b))
# print(b)

# In Python, the bin() function converts an integer to its binary representation as a string.
# The prefix 0b indicates that the number is in binary format, and the rest of the string
# represents the binary digits
#--> <class 'str'>
#--> 0b1010

# 3. Octal Form(Base-8):-
# ---------------
#
# The allowed digits are :- 0 to 7
# Literal value should be prefixed with 0o or 0o.
# int to octal :- oct()


# Scooden Practise

# Data types

# int
# float
# complex
# bool
# str
# bytes
# bytesaary
# range
# list
# tuple
# set
# frozenset
# dict
# None


# a = 10
# print(type(a))

# b = -100
# print(type(b))

# int Data type
# a = 100
# print(type(a))

# b = float(a)
#
# print(type(b))
#
# binary form

# a = 10
# print(type(a))

# b = bin(a)
# print(b)

# f = 1.224
# print(type(f))

# f = 1.2e6
# print(f)
#
# f = 1.23e34
# print(f)
#
# Complex number

# a = 7+8j
# b = 80+6j
# Real part: 7+80=87
# Imaginary part: 8+6=14j
# print(a+b)
#-->(87+14j)

# a = -9-89j
# b = 6+9j
# print(a-b)
# Real part: −9−6=−15
# Imaginary part: −89−9=−98j


# Boolean(bool())

# a = True
# print(type(a))

# b = False
# print(type(b))

# Internally Python Represents True as 1 and False as 0
# print(True + True)
# print(True - True)
# print(True - False)
# print(False - True)
# print(False + True)

# a = 10
# b = 20

# print(a > b)
# print(a < b)
# print(a <= b)

# l = ['a','b',22,78,90,'c']

# print('a' in l)
# print(44 in l)


# String(str())

# s = '1c4k!&'
# print(type(s))

# s1 = ' '
# print(type(s1))

# ds = '23546g^&*('
# print(type(ds))

# In python String follows Zero based index.
# [] operator is called slice operator,which can be used to retrieve part of string.

# s = 'Sourabh Patil'

# +ve index
# print(s[0:3])
# print(s[:4])
# print(s[2:5])

# -ve index
# print(s[-6:-2])
# print(s[-6:])
# print(s[:7])

# H/w:-
# ----

# first_data = 'Sourabh Patil'
# dob = '09-12-1997'
# requirement = Sourabh1997

# a = 'Sourabh Patil'
# b = '09-12-1997'
#
# print(a[0:7],b[6:10])
# print(a[0:7] + b[6:10]) # Without Space


# l = [1,2,45,78,'ab',78.89,[22,44,66],(56,89),99]
# print(type(l))

# print(l[-1])
# print(l[4:9])

# print(dir(l))
# print(len(l))
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# Count()
# l = [1,1,2,2,2,2,3,3,4,4,5,5,8]
# print(l.count(2))

# len()

# 1.Count()

# print(l.count(4))

# 2.index():-
# print(l.index(2))
# print(l.index(4))

# 3.append():-

# l = [1, 2, 3]

# l.append(20)
# print(l)
#
# l.append(40)
# print(l)

# l = [10,20,30,40]

# l.insert(1,15)
# print(l)

# l.insert(3,25)
# print(l)








