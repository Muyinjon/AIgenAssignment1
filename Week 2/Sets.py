'''Sets:
Basic Creation: Create a set of colors: "red", "green", "blue".
Adding Elements: Add "yellow" to the set.
Removing Elements: Remove "red" from the set.
Union: Find the union of two sets.
Intersection: Find the common elements of two sets.
Difference: Identify the difference between two sets.
Subset Checking: Check if {"red", "green"} is a subset of {"red", "green", "blue"}.
Set to List: Convert a set into a list.
List to Set: Convert a list into a set.a
Set Comprehension: Create a set of numbers divisible by 3 from 1 to 15 using set comprehension.
'''
def line():
    print('---------------------------------------------------------')

colors = {'red', 'green','blue' }
print(colors)
line()

colors.add('yellow')
print(colors)
line()

colors.remove('red')
print(colors)
line()

s1 = {'apple','banana','peach','grape','rice','tea'}
s2 = {'apple','pineapple','grape','ham','rice'}
unionset = s1.union(s2)
print(unionset)
line()

intersectset = s1.intersection(s2)
print(intersectset)
line()

differenceset = s1.difference(s2)
print(differenceset)
line()

testset = {1,6,8,9,4,5,3,68,55}
subset = {8,6,3,68}
print(testset)
print(subset)
check = False
if(all(x in testset for x in subset)):
    check=True

if check is True:
    print("subset is in test the test")
else:
    print("subset is not in the test")

line()

settolist = list(testset)
print(settolist)
line()

listtoset = set(settolist)
print(listtoset)
line()

dividby3 = {x for x in range(1,16) if x % 3 == 0 }
print(dividby3)
