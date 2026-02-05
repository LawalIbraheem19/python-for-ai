import math

def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points in 2D space.

    Args:
        point1 (tuple): A tuple representing the (x, y) coordinates of the first point.
        point2 (tuple): A tuple representing the (x, y) coordinates of the second point.
        """
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def random_choice(choices):
    """Select a random element from a list of choices.

    Args:
        choices (list): A list of elements to choose from.

    Returns:
        An element randomly selected from the choices list.
    """
    import random
    return random.choice(choices)

def factorial(n):
    """Calculate the factorial of a non-negative integer n.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


point1 = (104.9, 15)
point2 = (75, 23.5)

euclidee = calculate_distance(point1, point2)
print(f"The distance between point 1 and point 2 is {euclidee}")

# Select a random score from the lists of scores 
scores = [85, 90, 85, 92, 90]
choice = random_choice(scores)
print(f"{choice} was randomly selected from the pool")

# Built-in Functions

# Datetime Module 
import datetime

today = datetime.date.today()
print(today)

# Operating System
import os

current_dir = os.getcwd()
print(current_dir)

# JSON data
import json

person = {
    "Name" : "Ibraheem",
    "Age"  : 26,
    "Address" : {"Brazil" : "Passeio Floresta 205", "Nigeria" : "Afin-Iyanu Busstop, Eleyele"},
    "Nationality" : "Nigerian",
    "Course" : "Mechanical Engineering",
    "CPF" : 12754246193
} 
json_strings = json.dumps(person)