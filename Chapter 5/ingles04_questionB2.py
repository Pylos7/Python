""" Nestor Ingles Jr
    CSC 121 001
    Lesson 04 Lab - Ingles04_questionB2
"""

import math # imports math library
import random # imports random library

upper_limit = 100 # controls number of random integers to test
even_numbers = 0 # starts the count for even numbers
odd_numbers = 0 # odd number count


# for loop generates and test whether a number is either odd or even
# this loop also keeps track of the numbers
for x in range(0, upper_limit):
    number = random.randint (1, upper_limit)
    if number % 2 == 0:
        even_numbers = even_numbers + 1
    else:
        odd_numbers = odd_numbers + 1

# this print statement showcases the even numbers vs odd numbers
print("Even numbers: ", even_numbers, "\nOdd numbers: ", odd_numbers) # prints even numbers vs. odd numbers


"""
import math
import random

def rand_even_vs_odd(upper_limit):
    for x in range(0, upper_limit):
        number = random.randint (1, 100)
        if number % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return ("Even numbers: ", even, "\nOdd numbers: ", odd)

def main():
    upper_limit = 100
    even = 0
    odd = 0
    
# Call the main function
main()
"""
