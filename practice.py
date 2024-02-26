#Midterm Practice

#Understanding the types of expressions
print(type(22.3))  # For a float
print(type(False))  # For a boolean
print(type(None))  # For NoneType
print(type(4*2))  # For an int resulting from multiplication
print(type(4/2))  # For a float resulting from division
print(type(3.0*1.0))  # For a float resulting from multiplication of floats
print(type(~3))  # For an int resulting from a bitwise NOT operation
print(type(3 | 2))  # For an int resulting from a bitwise OR operation
# print(type(3 | 2.0))  # This will result in an error as mentioned
print(type(print("xx")))  # For checking the type of print function's return value

print (5 + 2 - 9)
print (2 + 3 * 5)
print (- - 5)
speed = 120.4

prompt = "What is the speed of the car?"
speed = input(prompt)
int(speed) + 5

print(3+10^2/2)

import re


def is_valid_url(url):
    # Regex to check valid URL
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    # Pass the string in search
    # method of regex object.
    if re.search(regex, url):
        return True
    else:
        return False


# Test the function
test_urls = ["https://www.example.com", "ftp://example.com/file.txt", "not_a_url", "http://localhost:8000"]
url_check_results = {url: is_valid_url(url) for url in test_urls}
url_check_results

import random

# Initialize the list
random_numbers = []

# Generate 10 random numbers and append to the list
for i in range(10):
    random_numbers.append(random.randint(1, 180))

# Replace numbers greater than 80 with their corresponding negative value
random_numbers = [-num if num > 80 else num for num in random_numbers]

# Print the final list
print(random_numbers)

import datetime
import random

today = datetime.today{}
start_of_year = datetime.date{today.year, 1, 1}
day_of_year = {today - start_of_year}.days + 1
sun = 0
for i in range (day_of_year//10):
    sun +- random.randint(1, day_of_year//7)

print{sum}

def corpare(first, second):
    if first == second:
        print (f""{first} = {second}"")
    elif first > second:
        print(f"{first} is greater than {second}")
    elif first < second:
        print{f"{first} is smaller than {second}"}
    first = int(input("Input first number:!"))
    second = int(input("Input second number:!"))
    corpare(first,second)







