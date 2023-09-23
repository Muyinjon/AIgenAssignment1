# 1) Create a string made of the first, middle and last character
# Write a program to create a new string made of an input string’s first, middle, and last character.
#
# Given:
#
# str1 = "James"
# Expected Output:
#
# Jms

assignment1= "James"
print(assignment1[::2]) #Jms

# 2) Create a string made of the middle three characters
# Write a program to create a new string made of the middle three characters of an input string.
#
# Given: case 1 str1 = "JhonDipPeta", Expected Output:: Dip
# case 2 str2 = "JaSonAy" ,Expected Output:Ay

assignment2_1 = "JhonDipPeta"
assignment2_2 = "JaSonAy"
print(assignment2_1[4:7]) #Dip
print(assignment2_2[5::]) #Ay


# 3) Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
#
# Given:
#
# s1 = "Ault"
#
# s2 = "Kelly"
# Expected Output: AuKellylt

assignment3_1 = "Ault"
assignment3_2 = "Kelly"
assignment3_3 = assignment3_1[0:2] + assignment3_2 + assignment3_1[3:]
print(assignment3_3) #AuKellylt

# 4) Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last
# characters.
#
# Given:
#
# s1 = "America"
# s2 = "Japan"
# Expected Output:
#
# AJrpan

assignment4_1 = "America"
assignment4_2 = "Japan"

def assessment4(word1,word2):
    middle1 = len(word1)//2
    middle2 = len(word2)//2
    beg1 = word1[0:1]
    beg2= word2[0:1]
    end1= word1[len(word1)-1::]
    end2= word2[len(word2)-1::]
    mid1 = word1[middle1:middle1+1:]
    mid2 = word2[middle2:middle2+1:]
    return print(beg1+beg2+mid1+mid2+end1+end2)
assessment4(assignment4_1,assignment4_2)


# 5) Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters
# of a string so that all lowercase letters should come first.
#
# Given:
#
# str1 = PyNaTive
# Expected Output:
#
# yaivePNT

assignment5 = "PyNaTive"
lowerletter = ""
upperletter = ""
for i in assignment5:
    if i.islower():
        lowerletter += i
    else:
        upperletter += i

assignment5final= lowerletter + upperletter
print(assignment5final)

# 6) Count all letters, digits, and special symbols from a given string
# Given:
#
# str1 = "P@#yn26at^&i5ve"
#
# Expected Outcome:
#
# Total counts of chars, digits, and symbols
#
# Chars = 8
# Digits = 3
# Symbol = 4

assignment6 = "P@#yn26at^&i5ve"
charletter = 0
digitsletter = 0
symbolsletter = 0

for i in assignment6:
    if i.isalpha():
        charletter += 1
    elif i.isdigit():
        digitsletter += 1
    else:
        symbolsletter += 1

print("Chars :",  charletter,  "\n Digits: ", digitsletter,  "\n Symbols: ", symbolsletter)

'''7) Create a mixed String using the following rules
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last
char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the
result.

Given:

s1 = "Abc"
s2 = "Xyz"
Expected Output:

AzbycX'''


assignment7_1 = "Abc"
assignment7_2 = "Xyz"

def assignment7def1(a1,a2):
    mixing_string=""
    lena1,lena2 = len(a1),len(a2)
    maxa = max(lena1,lena2)
    for i in range(maxa):
        if i < lena1:
            mixing_string += a1[i]
        if i < lena2:
            mixing_string += a2[lena1 - i - 1]
    return mixing_string
assignment7_3= assignment7def1(assignment7_1,assignment7_2)
print("Mix string: ", assignment7_3)


'''8) String characters balance Test

Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the
characters in the s1 are present in s2. The character’s position doesn’t matter.

Given:

Case 1:

s1 = "Yn"
s2 = "PYnative"
Expected Output:

True'''

assignment8_1 = "Yn"
assignment8_2 = "PYnative"
balance = True
for i in assignment8_1:
    if i not in assignment8_2:
        balance = False
        break
if balance:
    print(True)
else:print(False)


assignment8_1 = "Ynf"
assignment8_2 = "PYnative"
balance = True
for i in assignment8_1:
    if i not in assignment8_2:
        balance = False
        break
if balance:
    print(True)
else:print(False)

'''
Create a string made of the first, middle and last character
Write a program to create a new string made of an input string’s first, middle, and last character.

Given:

str1 = "James"

Expected Output:

Jms'''

assignment9 = "James"
def a9def(x):
    firstletter = x[:1]
    midletter = x[len(x)//2:len(x)//2 +1]
    lastletter = x[-1]
    allletter = firstletter + midletter + lastletter
    return print(allletter)
a9def(assignment9)


'''10) Create a string made of the middle three characters
Write a program to create a new string made of the middle three characters of an input string.

Given:

Case 1

str1 = "JhonDipPeta"
Output
Dip
Case 2
str2 = "JaSonAy"
Output
Son'''

assignment10_1 = "JhonDipPeta"
assignment10_2 = "JaSonAy"
def a10def(x):
    midletter = len(x)//2
    return print(x[midletter -1: midletter +2:])
a10def(assignment10_1)
a10def(assignment10_2)


'''11) Append new string in the middle of a given string
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

Given:

s1 = "Ault"
s2 = "Kelly"
Expected Output:'''

assignment11_1 = "Ault"
assignment11_2 = "Kelly"
def a11def(a1,a2):
    midlen = len(a1)//2
    a3 = a1[:midlen] + a2 + a1[midlen:]
    return a3
print(a11def(assignment11_1,assignment11_2))

'''12) Create a new string made of the first, middle, and last characters of each input string
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last
characters.
Given:
s1 = "America"
s2 = "Japan"
Expected Output:'''

a12_1 = "America"
a12_2 = "Japan"

###CHATGPT
def create_new_string(s1, s2):
    # Determine the first, middle, and last characters of each input string
    s1_first = s1[0]
    s1_middle = s1[len(s1) // 2] if len(s1) % 2 == 1 else ''
    s1_last = s1[-1]

    s2_first = s2[0]
    s2_middle = s2[len(s2) // 2] if len(s2) % 2 == 1 else ''
    s2_last = s2[-1]

    # Concatenate the first, middle, and last characters to form the new string
    new_string = s1_first + s2_first + s1_middle + s2_middle + s1_last + s2_last

    return new_string


# Given strings
s1 = "America"
s2 = "Japan"


# Create the new string
new_string = create_new_string(s1, s2)
print("Output:", new_string)  # Output: AJrpan





'''13) Arrange string characters such that lowercase letters should come first
Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters
of a string so that all lowercase letters should come first.

Given:

str1 = PyNaTive
Expected Output:

yaivePNT'''

lo = ""
up = ""
a13 = "PyNaTive"
for i in a13:
    if i.islower():
        lo += i
    else:
        up += i

print(lo+up)

#14 is on 6
#15 is on 7
#16 is on 8



"""17) Find all occurrences of a substring in a given string by ignoring the case
Write a program to find all occurrences of “USA” in a given string ignoring the case.

Given:

str1 = "Welcome to USA. usa awesome, isn't it?"
Expected Outcome:

The USA count is: 2
"""

a17 = "Welcome to USA. usa awesome, isn't it?"
a17 = a17.lower()
def a17def(x):
    i = 0
    words = x.split()
    for word in words:
        if "usa" in word:
            i += 1
    print("USA count:", i)
a17def(a17)

'''18) Calculate the sum and average of the digits present in a string 
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all  other characters. 
Given: 
str1 = "PYnative29@#8496" 
Expected Outcome: 
Sum is: 38 Average is 6.333333333333333'''

import statistics as stat
a18list=[]
a18 = "PYnative29@#8496"
for i in a18:
    if i.isdigit():
        a18list += i
    else: continue
a18list = [int(x) for x in a18list]

print("Sum is ", sum(a18list) ,"Average is", stat.mean(a18list))

'''19) Write a program to count occurrences of all characters within a string 
Given: 
str1 = "Apple" 
Expected Outcome:
{'A': 1, 'p': 2, 'l': 1, 'e': 1} 
'''

a19="Apple"
a19dict = {}
a19num=0
for i in a19:
   if i in a19dict:
       a19dict[i] += 1
   else:
       a19dict[i] = 1

print(a19dict)

"""20) Write a Python program to count the number of strings where the string length is 2 or more and the first and  last character are same from a given list of strings.  
Sample List : ['abc', 'xyz', 'aba', '1221'] 
Expected Result : 2 
"""

a20result = 0
a20 = ['abc', 'xyz', 'aba', '1221']
for i in a20:
    if len(i) >=2:
        if i[0:1] == i[-1:]:
             a20result += 1
        else:continue
    else:continue
print("Expected Result:", a20result)


"""21) Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit,  and print out the converted temperature. 
Take the sentence: 
Python is incredible. I love it!. 
Store each word in a separate variable, then print out the sentence on one line using print function. 
"""

a21_Celsius = int(input("Enter the temp:" ))
a21convert = (a21_Celsius * (9/5)) + 32
print(a21convert)

word1 = "Python"
word2 = "is"
word3 = "incredible"
word4 = "I"
word5 = "love"
word6 = "it!"
print(word1, word2, word3, word4, word5, word6)


'''22) First, assign your name into name variable, your last name into last_name variable and your age into age  variable. Then print on the screen the following text: 
Mick Jagger is 71 years old 
Of course name, last name and age have to contain your information.
'''

a22first = "Muyinjon"
a22last = "Turobov"
a22age = 23
print(f"{a22first} {a22last} is {a22age} years old" )





