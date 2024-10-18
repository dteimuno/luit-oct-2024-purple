import data_types # import other file incase we need it
import datadog # install missing libraries with pip install
import os  # provides a way to interact with the operating system
import glob  # helps to find all the file paths that match a pattern
import random  # random numbers and choices
import math  # provides mathematical functions
from datetime import datetime  # to work with dates and times

# Using random to generate a number between 0 and 10
number = random.randint(0, 10)
print(f"Random number: {number}")

# Using math to calculate the square root of the random number
sqrt_number = math.sqrt(number)
print(f"Square root of {number}: {sqrt_number}")

# Using datetime to print the current date and time
current_time = datetime.now()
print(f"Current date and time: {current_time}")

# Using os to list files in the current directory
print("Files in the current directory:")
for file_name in os.listdir('.'):
    print(file_name)

# Using glob to find all Python files in the current directory
print("\nPython files in the current directory:")
for file_name in glob.glob('*.py'):
    print(file_name)
