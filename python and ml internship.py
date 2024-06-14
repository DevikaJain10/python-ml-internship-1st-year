# Assignment-1
# Write a program that takes two numbers as input and prints their sum.
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
sum = num1 + num2
print("the sum of " ,num1 , " and " ,num2, " is " ,sum)

# Write a python program that checks whether a given number is even or odd.
number=int(input("enter a number greater than 0: "))
if number % 2 == 0:
    print(number, "is Even.")
else:
    print(number, "is Odd.")

# Write a python program that calculates the factorial of a given number
fact=1
number=int(input("enter number: "))
if number == 0:
    print (1)
for num in range(1,number + 1):
    fact *= num
print (fact)

# Write a program that asks the user for their name and then prints a greeting message
name = input("enter your name: ")
print("hello, good morning ", name)

# Write a program that takes a string input from the user and writes it to a text file.
user_input = input("Please enter a string: ")
file_name = "output.txt"
with open(file_name, "w") as file:
    file.write(user_input)
print(f"The string has been written to {file_name}")

#  Write a program that reads the content of a text file and prints it to the console.
file_name = "output.txt"
try:
    with open(file_name, "r") as file:
        content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print(f"The file {file_name} does not exist.")

# Write a python program that takes a string as input and returns its length.
a=input("enter anything : ")
print(len(a))

# Write a python program that concatenates two strings and returns the result
string1 = input("Please enter the first string: ")
string2 = input("Please enter the second string: ")
result = string1 + string2
print(result)

# Write a python program that checks if a substring is present in a given string
main_string = input("Please enter the main string: ")
substring = input("Please enter the substring: ")
if substring in main_string:
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is not present in the main string.")

# Write a python program that converts a given string to uppercase.
a=input("enter any string: ")
b=a.upper()
print(b)

# Write a python program that generates the first n numbers in the Fibonacci sequence
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    if n == 1:
        return [0]
    return fib_sequence
n = int(input("Please enter the number of Fibonacci numbers to generate: "))
fib_sequence = generate_fibonacci(n)
print("Fibonacci sequence:", fib_sequence)

# Write a python program that calculates the sum of the digits of a given number
number=int(input("enter any positive number: "))
sum = 0
for digit in str(number):
    sum += int(digit)
print(sum)

#  Write a program that asks the user for their birth year and calculates their age.
from datetime import datetime
def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age
birth_year = int(input("Please enter your birth year: "))
age = calculate_age(birth_year)
print(f"You are {age} years old.")

# Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines
def read_lines_until_empty():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    return lines
lines = read_lines_until_empty()
print("\nAll lines entered:")
for line in lines:
    print(line)

# Write a program that reads data from a CSV file and prints it to the console.    
import csv
def read_csv_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data
file_name = "data.csv"
data = read_csv_file(file_name)
print("Data from CSV file:")
for row in data:
    print(row)

# '''16 Write a program in python that counts the frequency of each character in 
# a string.'''
def count_character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
input_string = "hello world"
frequency = count_character_frequency(input_string)
for char, count in frequency.items():
    print(f"'{char}': {count}")

# 17 Write a program in python that converts a given string to title case (first letter of each word capitalized).
def convert_to_title_case(input_string):
    title_case_string = input_string.title()
    return title_case_string
input_string = "hello world"
title_case_string = convert_to_title_case(input_string)
print(title_case_string)
 
# 18 Write a python program that checks if two strings are anagrams of each other.
def are_anagrams(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    return sorted(string1) == sorted(string2)
string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print("The strings are anagrams of each other.")
else:
    print("The strings are not anagrams of each other.")

# '''19  Write a python program that removes all punctuation from a given string.'''
import string
def remove_punctuation(input_string):
    translator = str.maketrans("", "", string.punctuation)
    clean_string = input_string.translate(translator)
    return clean_string
input_string = "Hello, World! How are you today?"
clean_string = remove_punctuation(input_string)
print(clean_string)

# 20. Write a python program that takes a list of numbers and returns their sum. 
def calculate_sum(numbers):
    return sum(numbers)
numbers = [1, 2, 3, 4, 5]
total_sum = calculate_sum(numbers)
print("Sum of the numbers:",total_sum)

# '''21 Write a python program that counts the occurrences of a specific element in a list. '''
def count_occurrences(input_list, element):
    return input_list.count(element)
my_list = [1, 2, 3, 4, 2, 2, 5, 6]
element_to_count = 2
occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} occurs {occurrences} times in the list.")

# '''22. Write a python program that returns the minimum and maximum values in a list of numbers. '''
def find_min_max(input_list):
    if len(input_list) == 0:
        return None, None
    min_value = min(input_list)
    max_value = max(input_list)
    return min_value, max_value
numbers = [1, 2, 3, 4, 5]
min_value, max_value = find_min_max(numbers)
print("Minimum value:", min_value)
print("Maximum value:", max_value)

# '''23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input. '''
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def main():
    print("Temperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius.")
    else:
        print("Invalid choice. Please enter either 1 or 2.")
    if __name__ == "_main_":
        main()

# '''24. Write a program that acts as a simple calculator. It should take two 
# numbers and an operator (+, -, *, /) as input and print the result. '''
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error!"

# '''25. Write a program that copies the contents of one text file to another. '''
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print("File copied successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
def main():
    source_file = input("Enter the name of the source file: ")
    destination_file = input("Enter the name of the destination file: ")
    copy_file(source_file, destination_file)
    if __name__ == "_main_":
        main()

# '''26. Write a program in python that checks if a string starts with a given prefix 
# or ends with a given suffix. '''
def starts_with_prefix(input_string, prefix):
    return input_string.startswith(prefix)
def ends_with_suffix(input_string, suffix):
    return input_string.endswith(suffix)
def main():
    input_string = input("Enter a string: ")
    prefix = input("Enter the prefix to check: ")
    suffix = input("Enter the suffix to check: ")

    if starts_with_prefix(input_string, prefix):
        print(f"The string '{input_string}' starts with the prefix '{prefix}'.")
    else:
        print(f"The string '{input_string}' does not start with the prefix '{prefix}'.")
    if ends_with_suffix(input_string, suffix):
        print(f"The string '{input_string}' ends with the suffix '{suffix}'.")
    else:
        print(f"The string '{input_string}' does not end with the suffix '{suffix}'.")
if __name__ == "_main_":
    main()

# '''27. Write a program in python that converts a string into a list of its characters.'''
def string_to_list(input_string):
    return list(input_string)
def main():
    input_string = input("Enter a string: ")
    characters_list = string_to_list(input_string)
    print("List of characters:", characters_list)
if __name__ == "_main_":
    main()


