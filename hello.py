import os
# This is a simple Python script that prints a greeting message.
name = "Alice"
age = 30
print(f"Hello, {name} and age is {age}!")

# Basic Data Types in Python
integer = 10          # Integer
floating_point = 10.5     # Float
string = "Hello, World!"  # String
multine_line_string = """This is a
Multiline
String
"""
boolean = True        # Boolean
print(multine_line_string)

# Basic Arithmetic Operations
sum_result = integer + floating_point
print(f"Sum: {sum_result}")

exponent = floating_point ** integer  # Exponentiation
difference = floating_point - integer
print(f"Difference: {difference}")
product = floating_point * integer
print(f"Product: {product}")
quotient = floating_point / integer
print(f"Quotient: {quotient}")
floor_division = floating_point // integer  # Floor Division
print(f"Floor Division: {floor_division}")
modulus = floating_point % integer  # Modulus
print(f"Modulus: {modulus}")
print(f"Exponentiation: {exponent}")    
print(f"Integer: {integer}, Float: {floating_point}, String: {string}, Boolean: {boolean}")

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full Name: {full_name}")

# String Manipulation
sample_string = "*" * 10
print(full_name)
print(sample_string)


# Comparison Operators
age  = 18
is_age_18 = (age == 18)          # Equal to
is_not_age_18 = ( age != 18)     # Not equal to


can_drive = (age >= 18)          # Greater than or equal 
has_id = True
can_enter = can_drive and has_id  # Logical AND
can_access = can_drive or has_id   # Logical OR

# Assignment Operators
x = 5
x = x + 3 # Standard assignment
x += 3   # Addition assignment
x -= 2   # Subtraction assignment
x *= 4   # Multiplication assignment
x /= 2   # Division assignment

# String Case Conversion
original_string = "hello world"
upper_string = original_string.upper()  # Convert to uppercase
lower_string = original_string.lower()  # Convert to lowercase
title_string = original_string.title()  # Convert to title case 
print(f"Title Case: {title_string}")
print(f"Uppercase: {upper_string}") 
print(f"Lowercase: {lower_string}")


# String Manipulation Methods
message = " I love Python programming with OpenAI! "

trimmed_message = message.strip()  # Remove leading and trailing whitespace
replaced_message = trimmed_message.replace("OpenAI", "ChatGPT")  # Replace substring
split_message = replaced_message.split(" ")  # Split string into a list
casefolded_message = replaced_message.casefold()  # Case-insensitive comparison

# Check if something exists 
contains_love = "love" in message  # Check substring existence
print(contains_love)
print(message.startswith(" I love"))  # Check start of string
print(message.endswith("! "))        # Check end of string
print(f"Trimmed Message: '{trimmed_message}'")
print(f"Replaced Message: '{replaced_message}'")
print(f"Split Message: {split_message}")
print(f"Casefolded Message: '{casefolded_message}'")
print(f"Is age 18: {is_age_18}")
print(f"Is not age 18: {is_not_age_18}")
print(f"Can Drive: {can_drive}")
print(f"Can Enter: {can_enter}")
print(f"Can Access: {can_access}")
print(message.find("OpenAI"))  # Find substring index
print(message.count("o"))      # Count occurrences of substring


# If-Elif-Else Statements
score = 85
if score >= 90:
    grade = ("A - Excellent")
    print(grade)
elif score >= 80:
    grade = ("B - Good")
    print(grade)
elif score >= 70:
    grade = ("C - Average")
    print(grade)
elif score >= 60:
    grade = ("D - Below Average")
    print(grade)
else:
    grade = ("F - Fail")
    print(grade)


# Lists in Python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Access first element
print(fruits[-1]) # Access last element
fruits.append("date")  # Add element to the end
fruits.remove("banana")  # Remove element
fruits.insert(3, "kiwi")
print(fruits)

fruits.count("date")
fruits.index("kiwi")
fruits.sort()
fruits.reverse()
fruits

# Dictionary in Python
person = {
    "Name" : "Ibraheem",
    "Age"  : 26,
    "Address" : {"Brazil" : "Passeio Floresta 205", "Nigeria" : "Afin-Iyanu Busstop, Eleyele"},
    "Nationality" : "Nigerian",
    "Course" : "Mechanical Engineering",
    "CPF" : 12754246193
}

person["CPF"]
person["License"] = True
person["Address"]["Brazil"]

person["Address"].values()
person.update({"RN":"MEC250104"})
person

# Tupple in Python
point = (104.5, 19)
color = ("red", "green", "blue")

point[-2] 

# Set in Python
# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}

numbers.add(6)
numbers.remove(5)
numbers.remove(9)
numbers.discard(9)
numbers.add(5)
numbers
# Functions in Python
def greet():
    print("Hello!")
    print("Ehllo again!!")
    pass

greet()

def check_weather(temperature):
    if temperature == 25:
        print("The weather is normal")
    elif temperature > 25:
        print("The weather is hot!")
    else:
        print("The weather is cold")
    pass

check_weather(-3)

def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")
    pass

greet_user(last_name="Lawal", first_name="Ibraheem")

def calculate_tax(price, discount, tax_rate=0.05, print_receipt=False):
    tax = price * tax_rate
    if discount > 0:
        tax -= discount * tax_rate
        final_price = price - discount + tax
    else:
        final_price = price + tax
    
    print(f"Final Price: {final_price}")

calculate_tax(100, 50, print_receipt=True)


# Looping Constructs in Python
# For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# While Loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
# Looping through a dictionary
person = {
    "Name" : "Ibraheem",
    "Age"  : 26,
    "Address" : {"Brazil" : "Passeio Floresta 205", "Nigeria" : "Afin-Iyanu Busstop, Eleyele"},
    "Nationality" : "Nigerian",
    "Course" : "Mechanical Engineering",
    "CPF" : 12754246193
}
for key, value in person.items():
    print(f"{key}: {value}")
# Looping with range
for i in range(5):
    print(f"Number: {i}")
for i in range(1, 11, 2):
    print(f"Odd Number: {i}")
# List Comprehension
squares = [x**2 for x in range(10)]
print(squares)
# Set Comprehension
unique_squares = {x**2 for x in range(10)}
print(unique_squares)
# Dictionary Comprehension
square_dict = {x: x**2 for x in range(10)}
print(square_dict)

# Functions with Return Values
def simple_function():
    numbers = [1, 2, 3, 4, 5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number

first, last = simple_function()
print(f"First: {first}, Last: {last}")


try: 
    # Get current working directory
    file_directory = os.getcwd()
    text_files = []
    
    # os.listdir returns all names in the folder
    for filename in os.listdir(file_directory):
        # Change ".pdf" to ".txt" to find text files
        if filename.lower().endswith(".pdf"):
            full_path = os.path.join(file_directory, filename)
            
            # Ensure it's a file and not a directory
            if os.path.isfile(full_path):
                text_files.append(full_path)
    
    if not text_files:
        print("No PDF files found in this directory.")
    else:
        for file_path in text_files:
            print(file_path)

except FileNotFoundError:
    print("The requested directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
