print("Hello 123!")

# Formated string
print(f"I am {21 + 10}")

# True and False need to be uppercased

# List equality
# [1,2,3] == [1,2,3] # True
# [1,2,3] is [1,2,3] # False (compares identity)

nums = [1, 2, 3]
copy = nums
print(nums is copy)  # True

# formatting loops (indentation is critical in python)
for i in nums:
    print(i)

# Else if statements
age = 19
if age >= 21:
    print('Welcome')
elif age >= 18:
    print("Come in, but no drinks")
else:
    print("Go Away")

# Ternary operator
# do_if_true 'if' CONDITION 'else' do_if_false
msg = "go vote!" if (age >= 18) else "go play!"
print(msg)

# and / or / not
if age < 15 or age > 65:
    print("discounted pricing")
else:
    print("full price")

print(True and False)  # False

# What's False: ( 0, "", None, False >>> [], {}, set() )

#  While loop & break
num = 0
while num < 10:
    if num == 4:
        print('loop broken')  # works
        break
        print("I'm broke")  # won't work
    print(num)
    num += 1
print('\n')
# Get user input
# guess = input("Guess the number")


# Using range (range (start, stop, step)
for i in range(5):
    print(i)  # 1,2,3,4

for i in range(0, 10 + 1, 5):
    print(i)  # 0, 5, 10

lst = list(range(5))  # [0,1,2,3,4]
print(lst, '\n')

# negative step
lst2 = list(range(5, 0, -1))  # [5,4,3,2,1]
print(lst2)


# Functions
def greet(person):
    return f'Hello there, {person}!'


print(greet("Sean"))  # Hello there, Sean!


def send_email(to_email, from_email, subject, body):
    email = f"""
    to: {to_email}
    from: {from_email}
    subject: {subject}
    ---------------------
    body: {body}
    """
    return email


my_email = 'mlanden1221@gmail.com'
new_email = send_email(from_email=my_email, to_email='sean@gmail.com', subject="How are you?",
                       body="Been a while. Let's talk")
print(new_email)


# Create docstring (will explain how function works/purpose)
def add_limited_numbers(a, b):
    """Add two numbers, making sure sum caps at 100."""  # always use tripple quotes
    sum = a + b

    if sum > 100:
        sum = 100

    return sum


print(help(add_limited_numbers))  # vvv
### add_limited_numbers(a, b)
# Add two numbers, making sure sum caps at 100.

# get length
print(len([1, 2, 3, 'hi']))  # 4
print(len('Hello'))  # 5

# list method
print(list('hello'))  # ['h','e','l','l','o']

# Automatic list slicing >>> lst[start:stop:step]
nums = list(range(10))
print(nums[0:8:2])  # [0,2,4,6]
print(nums[8:])  # [8,9]
print(nums[0::2])  # [0, 2, 4, 6, 8]

# List splicing
colors = ['red', 'orange', 'yellow']
colors[0:1] = ['dark red', 'pink']
print(colors)  # ['dark red', 'pink', 'orange', 'yellow']

# List methods
lst1 = [1, 2, 3, 4, 1, 2, 3, 4, ]
lst2 = lst1.copy  # Copies contents, not memory location
lst1.count(2)  # 2
new_nums = [11, 12, 13]
lst1.extend(new_nums)  # extend list to list
print(lst1.index(2))  # 1 (prints first matching index)
lst1.insert(4, 50)  # [1, 2, 3, 4, 50, 1, 2, 3, 4, 11, 12, 13]

########### String methods
# str.count(t)	Returns # times t occurs in str
# str.endswith(t)	Does str end with string t?
# str.find(t)	Index of first occurence (-1 for failure)
# str.isdigit()	Is str entirely made up of numbers?
# str.join(seq)	Make string of list str joined by seq ("|".join(nums))
# str.lower()	Return lowercased copy of str
# str.replace(old,new,count)	Replace new from all occurrences of 'old' in str (default count: all)
# str.split(sep)	Return list of items made from splitting str on sep
# str.splitlines()	Split str at newlines
# str.startswith(t)	Does str start with t?
# str.strip()	Remove whitespace at start/end of str

names = ["Matt", 'Cara', 'Bella', 'Vito']
print('|'.join(names))  # Matt|Cara|Bella|Vito

# Dictionaries (ordered by insertion order / are an Object type)
# Quicker than arrays when adding, retrieving, or deleting items -- O(1) vs. O(n)
person = {'first': 'Henry', 'last': 'Zarkoface'}

print(person['first'])  # to access data

# Get method in dictionaries
person.get('last')  # 'Zarkoface'
person.get('age', 32)  # 32 (2nd param becomes default if not found)

print('last' in person)  # True
# print('Zarkoface' in person) #doesn't work


print('\n')
# Iterating dictionaries
ages = {"Sean": 6, "Fluffy": 3, "Ezra": 7}

for key in ages.keys():
    print(key)

for age in ages.values():
    print(age)

for name_and_age in ages.items():  # get tuple back
    print(name_and_age)

for key, value in ages.items():
    print(f"key: {key} & value: {value}")

# dictionary methods
person2 = {'first': 'Henry', 'last': 'Zarkoface', 'age': 55}
person3 = person2.copy()  # create copy without simply being a reference to memory.

# Sets (collection of unordered unique items)
# *created like a dictionary, but without keys
# *Only work with immutable values
colors = {'red', 'blue', 'blue', 'white'}
print(colors)  # {'white', 'red', 'blue'}

lst5 = ['ruby', 'javascript', 'scala', 'ruby', 'ruby']
set_list = set(lst5)
print(set_list)  # {'scala', 'javascript', 'ruby'}

# Set methods
print('red' in colors)  # True

# set1.add(val)
# set1.copy()
# set1.pop() / set1.pop(index)
# set1.remove(val)

# Set operations
### Returns a set ###
moods = {"happy", "sad", "grumpy"}
dwarfs = {"happy", "grumpy", "doc"}

a = moods | dwarfs  # union: {"happy", "sad", "grumpy", "doc"}

b = moods & dwarfs  # intersection: {"happy", "grumpy"}

c = moods - dwarfs  # difference: {"sad"}
d = dwarfs - moods  # difference: {"doc"}

e = moods ^ dwarfs  # symmetric difference (all elements that are in exactly one of the sets): {"sad", "doc"}

bad_moods = ['angry', 'frustrated', 'sad']
# lists can work, but must be the passed in value
moods.intersection(bad_moods)  # works
# bad_moods.union(moods) #doesn't work

# Sets are iterable (iterate a set)
for adj in moods | dwarfs:
    print(adj)

print(list(moods))  # Can convert set to list

# Tuples (ordered collection of values, but are immutable)
# *Immutable: Can't be changed after creation
new_colors = ('red', 'yellow', 'green', 'brown', 'red')
len(new_colors)  # works
new_colors[1]  # yellow
# new_colors.append('black') #doesn't work
new_colors.count('red')  # 2
new_colors.index('yellow')  # 1

tup = (5,)  # creates single tuple

# tuple can be used as dictionary key
board = {
    (0, 0): 'X',
    (0, 1): None,
    (0, 2): "O",
    (1, 0): 'X',
    (1, 1): "O",
    (1, 2): None
}

print(f"Line 249: {board[(0, 0)]}")  # Line 249: X

##################################
# Comprehension (returns new list)
# [what_to_append for each_item in list]
# Python does have filter() & map(), but you should use comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

############
evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)

print(evens)  # [2,4,6,8,10]

#### VS #####
evens2 = [num for num in nums if num % 2 == 0]
print(evens2)  # [2, 4, 6, 8, 10]

# More Comprehension
doubled = [num * num for num in nums]
print(doubled)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = [char for char in 'lmfao']
print(x)  # ['l', 'm', 'f', 'a', 'o']

# Nested list comprehension
board = [[0 for y in range(3)] for x in range(3)]
print(board)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def gen_board(size, initial_val='?'):
    return [[initial_val for y in range(size)] for x in range(size)]


new_board = gen_board(4)
print(new_board)  # [['?', '?', '?', '?'], ['?', '?', '?', '?'], ['?', '?', '?', '?'], ['?', '?', '?', '?']]

# Add if statement to filter

odds = [x for x in range(10) if x % 2 == 1]
print(odds)  # [1, 3, 5, 7, 9]

chickens = [
    {'name': "Henry", 'sex': 'Rooster'},
    {'name': "Lady", 'sex': 'Hen', 'age': 4},
    {'name': "Susie", 'sex': 'Hen'},
    {'name': "Butters", 'sex': 'Rooster'},
]

hens = [i['name'] for i in chickens if i['sex'] == 'Hen']
print(hens)  # ['Lady', 'Susie']

# Comprehension using if else statement
# [do_this if something else do_this for thing in things]
scores = [55, 89, 99, 87, 60, 70, 74, 76, 90, 82]
passed = ['Pass' if i >= 70 else 'Fail' for i in scores]
print(passed)

# dictionary comprehension
week_chart = {day: 'work' for day in 'MTWRFSU'}
print(week_chart)  # {'M': 'work', 'T': 'work', 'W': 'work', 'R': 'work', 'F': 'work', 'S': 'work', 'U': 'work'}

# Create a Set w/ comprehension
letter = {i for i in 'abracadabra'}  # {'a', 'b', 'c', 'd', 'r'}

############ Packing & Unpacking ##########
point = (100, 58)
x, y = point  # 100 / 58

# Get rest (*)
letters = list('abcd')
first, *rest = letters
print(first)  # a
print(rest)  # ['b', 'c', 'd']

# double unpacking
color_pairs = [['red', 'green'], ['purple', 'orange']]
((p1, s1), (p2, s2)) = color_pairs
print(f'{p1} & {s1} & {p2} & {s1} ')

# Spread / unpacking (works with sets & lists)
nums = [2, 4, 6, 8]
spread_nums = [-2, 0, *nums]  # Creates new list
print(spread_nums)  # [-2, 0, 2, 4, 6, 8]

rainfall = {'Jan': 2.5, 'Feb': 3.8}
new_Set = {*rainfall}  # returns keys {'Feb', 'Jan'}
# MUST USE ** to spread dictionary
new_dict = {**rainfall}  # {'Jan': 2.5, 'Feb': 3.8}


####### Error Handling ##########
def get_days_alive(person):
    try:
        days = person['age'] * 365
        print(f'{person["name"]} have been alive for {days} days')
    except KeyError as exc:
        print(f"Missing key: {exc}")
    except:
        print("Expected person to be a dict")


sean = {'name': 'Sean', 'age': 31}
mary = {'age': None}
get_days_alive(sean)  # You have been alive for 11315 days
get_days_alive(mary)  # Missing key: 'name'
get_days_alive(9)  # Expected person to be a dict


# Raise your own exception
def raise_error(msg):
    raise ValueError(msg)


# raise_error("I don't like that value")
# ValueError                                Traceback (most recent call last)
# <ipython-input-19-631d208b5761> in <module>
# ----> 1 raise_error("I don't like that value")
#
# ~\OneDrive\Springboard\Python\notes.py in raise_error(msg)
#     366 # Raise your own exception
#     367 def raise_error(msg):
# --> 368     raise ValueError(msg)
#     369
#     370
#
# ValueError: I don't like that value

######## Common to create a function to handle the errors
def bounded_avg(nums):
    "Return avg of nums (makes sure nums are 1-100)"  # this is the docstring

    for n in nums:
        if n < 1 or n > 100:
            raise ValueError("Outside bounds of 1-100")

    return sum(nums) / len(nums)


def handle_data(ages):
    try:
        avg = bounded_avg(ages)
        print("Average was", avg)

    except ValueError as exc:
        # exc is exception object -- you can examine it!
        print("Invalid age in list of ages")


##### Doctests (python's version of Jasmine) #######
# * Run using > python -m doctest -v file_name.py

# def bounded_avg(nums):
#     """
#     Return avg of nums (makes sure nums are 1-100)
#     >>> bounded_avg([2,4,6])
#     4.0
#
#     >>> bounded_avg([10,20,30,40,50])
#     30.0
#
#     >>> bounded_avg([10,50,110])
#     Traceback (most recent call last):
#         ...
#     ValueError: Outside bounds of 1-100
#     """
#
#     for n in nums:
#         if n < 1 or n > 100:
#             raise ValueError("Outside bounds of 1-100")
#
#     return sum(nums) / len(nums)


# * Run using > 'python -m doctest -v file_name.py'
# ^^ Returns vv
# 1 items passed all tests:
#    3 tests in notes.bounded_avg
# 3 tests in 9 items.
# 3 passed and 0 failed.
# Test passed.

# bounded_avg([10,50,110])

### Standard library modules
import math

print(math.ceil(10.7))  # 11

from statistics import mean, median  # import select modules from library

print(mean([2, 3, 4, 5, 6, 7]))  # 4.5
print(median([2, 3, 4, 5, 6, 7, 8]))  # 5

from random import choice as pick_a_thing  # rename module

print(pick_a_thing([1, 2, 3, 4, 5]))  # Picks random num from selection

# Calendar library returns a calendar class
import calendar

cal = calendar.TextCalendar()

print(cal.prmonth(2020, 12))  # prints vvv

#   December 2020
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31


# import turtle
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.pen()
# turtle.bgcolor('black')
# for x in range(360):
#     t.pencolor(colors[x %6])
#     t.width(x/100+1)
#     t.forward(x)
#     t.left(59)

# Import file from computer
import helpers


def make_person(name, favColor):
    return {
        'name': name,
        'favColor': favColor,
        'birth_year': helpers.get_rand_year(),
        'birth_month': helpers.get_rand_month()
    }


print(make_person('tommy', 'purple'))  # {'name': 'tommy', 'favColor': 'purple', 'birth_year': 2019, 'birth_month': 'F'}

# pip install forex-python
from forex_python.bitcoin import BtcConverter

b = BtcConverter()
print(b.get_latest_price('USD'))

# Run all prompts through GitBash

# create virtual environment >>> be inside proper folder
# >>> Command line: 'python -m venv venv' >>> Activate with: . venv/Scripts/activate

# In Pycharm >>> settings >>> interpreter >>> Activate venv >>> Automatically activates
# To reactivate >>> cd into venv/Scripts >>> activate.bat

from faker import Faker

fake = Faker()

for x in range(3):
    print(fake.name())

# Open & Edit files
# file = open('text.txt', 'r')
# for line in file:
#     print(line)
#
# file.seek(0)  # move 'cursor' back to first char.
# all_text = file.read()
# file.close()
#
# file2 = open('writeMe.txt', 'w')
# file2.write("This text goes into writeMe.txt")
# file2.close()
#
# file3 = open('writeMe.txt', 'a')  # a = append to file
# file3.write('\nThis goes on the second line of writeMe.txt')

#########  OOP (a class)  #############
# vvv Counter is a 'class' and it comes with predefined methods

from collections import Counter

my_counter = Counter("OOPMPA LOOMPA")
print(my_counter)  # Counter({'O': 4, 'P': 3, 'M': 2, 'A': 2, ' ': 1, 'L': 1})
print(my_counter.most_common())  # [('O', 4), ('P', 3), ('M', 2), ('A', 2), (' ', 1), ('L', 1)]


# To get/set object attribute >>> o.name
# To call method: o.method()
# to retrieve value from dict: o['key']
from math import sqrt

class RightTriangle:
    """
    A class used to represent a right triangle

    Attributes
    -----------------
    a: int
      length of side a
    b: int
      length of side b
    """
    def __init__(self, a, b): #automatically called
        self.a = a
        self.b = b
        print('called')

    # method called simply by printing variable instantiated w/ class (ie: print(t))
    # Repr is for developers & str is for everyone else
    def __repr__(self):
        return f"RightTriangle (a={self.a}, b={self.b})"

    def __str__(self):
        return self.describe()

    # create class method
    @classmethod
    def random(cls):
        """Class method which returns Triangle w/ random sides""" #class docstring
        return cls(234, 508) #creates triangle with side-a: 234 & side-b: 508

    def get_hypotenuse(self):
        return sqrt(self.a**2 + self.b**2)

    def get_area(self):
        return self.a*self.b /2

    def describe(self):
        return f"I am a triangle with sides: {self.a} & {self.b}"

t = RightTriangle(3,4) #called
# print(t.get_hypotenuse()) #5.0

t2=RightTriangle.random()  #called
print(t2.a, t2.b) #234 508

#Class Inheritance
class ColoredTriangle(RightTriangle):
    def __init__(self, a, b, color):
        #get parent class's init
        super().__init__(a, b)
        self.color = color

    # pull data from parent class using super()
    def describe(self):
        return super().describe() + f" I am {self.color}"

t3 = ColoredTriangle(3,4,'Red')
print(t3.color)


print(t3)


