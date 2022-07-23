"""
Name: Nestor Ingles Jr
Course:  CSC - 121
Assignment:  Lesson 06: Lists and Tuples Sakai Lab
Program Name: Rainfall
"""
def main():
    rainfall = get_rainfall()
    # Calculating and printing Total yearly rainfall
    yearly_rainfall = get_total(rainfall)
    print("\nTolal Yeaarly Rainfall: ", yearly_rainfall)

    # Calculating and printing the average monthly rainfall
    amr = yearly_rainfall/12
    print("Average Monthly Rainfall: ", f"{amr:.2f}")

    print("The maximum rainfall was", max(rainfall), "inches in ", months(int(rainfall.index(max(rainfall)))-1))
    print("The minimum rainfall was", min(rainfall), "inches in ", months(int(rainfall.index(min(rainfall)))-1))

def get_total(value_list):
    # Create a variable to use as an accumulator.
    total = 0.0

    # Calculate the total of the list elements.
    for num in value_list:
        total += float(num)

    # Return the total.
    return total

def get_rainfall():
    # Create an empty list.
    rainfall = []


    num_months = 12

    # Create a variable to control the loop.
    count = 0

    # Get the rainfall ammounts from the user and add them to the list.
    while count < num_months:
        # Get a score and add it to the list.
        #rain = float(input("Enter rainfall for month #", count, ":"))
        rainfall.append(input("Enter Rainfall Inches: "))
        count += 1
    # Return the list.
    return rainfall

# This function takes an integer between 1 - 12 and spits out the respective month as a string.
def months(month):
    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    else:
        return "December"

# Call the main function.
main()
