'''Basic Creation: Create a tuple with 5 student names.
Accessing Elements: Extract the third student's name from the tuple.
Indexing: Find the index of a student's name in the tuple.
Tuple to List: Convert a tuple into a list.
List to Tuple: Convert a list into a tuple.
Tuple Unpacking: Given a tuple (x, y, z), unpack its values into three variables.
'''
import math

def line():
    return print("---------------------------------------------------------------------------------")
line()

students = ('jon','bek','rex','alex','zeki')
print(students[3])

line()

tupletolist = list(students)
print(tupletolist)

line()

listtotuple = tuple(tupletolist)
print(listtotuple)

line()
print()

a = math.factorial(4)
print(a)
