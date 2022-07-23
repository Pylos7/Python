"""
Name: Nestor Ingles Jr
Course:  CSC - 121
Assignment:  Lesson 2 Lab - Question 2
"""

# Getting colors from user
p1 = input("Enter primary color:")
p2 = input("Enter primary color:")

# Testing for color combinations
if (p1 == "red" and p2 == "blue") or (p1 == "blue" and p2 == "red"):
    print("When you mix red and blue, you get purple.")

elif (p1 == "blue" and p2 == "yellow") or (p1 == "yellow" and p2 == "blue"):
    print("When you mix blue and yellow, you get green.")

elif (p1 == "yellow" and p2 == "red") or (p1 == "red" and p2 == "yellow"):
    print("When you mix yellow and red, you get orange.")

else: print("You didn't input two primary colors.")
