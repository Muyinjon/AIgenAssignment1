'''Dictionaries:
Basic Creation: Create a dictionary to store a book's title, author, and publication year.
Accessing Elements: Extract the author's name from the dictionary.
Updating: Update the publication year to 2022.
Adding Elements: Add a list of chapters to the book dictionary.
Deletion: Remove the publication year from the dictionary.
Looping: Loop through the dictionary and print all the keys.
Looping through Values: Loop and print all the values in the dictionary.
Dictionary Comprehension: Create a dictionary with numbers (1 to 5) as keys and their squares as values.
Merge Dictionaries: Merge two dictionaries into one.
Deep Copy: Create a deep copy of a dictionary using the copy module.
'''
def line():
    print("------------------------")
    print(book)

book= {"book's title" : "rich dad, poor dad", "author":"Robert Kiyosaki" , "publication year": 1997}
print(book["author"])

book["publication year"] = 2022
line()

book["chapters"] = "chapter 1: The rich don't work for money.", "Chapter 5: The rich invent money."
line()

del book["publication year"]

line()


for key in book:
    print(key)

line()

for value in book.values():
    print(value)

line()
for key, value in book.items():
    print(f"{key}:{value}")

line()

dict1 = {1:1,2:2**2,3:3**2,4:4**2,5:5**2}
dict2 = {1:1,2:2,3:3,4:4,5:5}


