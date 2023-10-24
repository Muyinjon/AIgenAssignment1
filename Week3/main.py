# 1.Write a function that takes a filename as its argument. The function should read the content of the file
# and write it back to the file in reverse order. If the file does not exist, print a custom error message.
# 2.Write a function that takes a filename as its argument. The function should read the file and return the
# number of lines in the file. If the file does not exist, it should return an appropriate error message.
# 3.Write a function that reads content from a file and prints it. If the file does not exist, print a custom
# error message. Ensure that the file is closed properly in all scenarios.
# 4.Write a function that takes a list and an index as its arguments. The function should return the
# element at the specified index. If the index is out of range, return a custom error message. If the
# provided index isn't an integer, inform the user of the invalid input.
#
# Create a file with student names and their scores
with open('students_scores.txt', 'w') as file:
    file.write('Alice, 90, 85, 78\n')
    file.write('Bob, 78, 92, 80, 88\n')
    file.write('Charlie, 88, 90, 93\n')
    file.write('David, 80, 82, 84, 86, 88\n')


import os
students = {}

with open('students_scores.txt', 'rt') as f:
    for line in f:
        data = line.strip().split(', ')
        studentname = data[0]
        scores = [int(score) for score in data[1:]]
        students[studentname] = scores

    for student, scores in students.items():
        average_score = sum(scores) / len(scores)
        print(f"{student}'s average score: {average_score:.2f}")





# 1. Function to read the content of a file and write it back in reverse order
def reverse_file_content(filename):
    try:
        with open(filename,'r') as file:
            content = file.readline()
        with open(filename,'w') as file:
            file.writelines(reversed(content))
    except FileNotFoundError:
        print('No File')


# 2. Function to count the number of lines in a file
def countnuminfile(filename):
    try:
        with open(filename, 'r') as file:
            count =  sum(1 for line in file)
        return count
    except FileNotFoundError:
        print('No File')


# 3. Function to read and print content from a file
def readfile(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print('No File')


# 4. Function to get an element from a list by index





# Example usage of these functions
filename = 'students_scores.txt'

# Test the reverse_file_content function
reverse_file_content(filename)

# Test the count_lines function
count = countnuminfile(filename)
print(f"Number of lines in the file: {count}")

# Test the read_and_print_file_content function
readfile(filename)





