'''Basic Creation: Create a tuple with 5 student names.
Accessing Elements: Extract the third student's name from the tuple.
Indexing: Find the index of a student's name in the tuple.
Tuple to List: Convert a tuple into a list.
List to Tuple: Convert a list into a tuple.
Tuple Unpacking: Given a tuple (x, y, z), unpack its values into three variables.
'''

def line():
    return print("---------------------------------------------------------------------------------")
line()

students = ('Jon','Bek','Rex','Alex','Zeki')
print(students[3])

line()
print(students.index('Rex'))

line()
tupletolist = list(students)
print(tupletolist)

line()

listtotuple = tuple(tupletolist)
print(listtotuple)

line()

tuple1 = (1,33,54)
x,y,z = tuple1

print(x)
print(y)
print(z)

line()


