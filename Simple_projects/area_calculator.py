""" 
Area calculator for various shapes(py3)
Ask user to input a shape which can then be calculated
"""

print ("Area calculator is running...")

# Takes input from user and makes all lower case
read_zero = input("Enter name of shape: ")
shape = read_zero.lower()

# Function to determine what shape has been inputted and which function to use for calculation
def area():
    if shape == "square":
        square_area()
    elif shape == "triangle":
        triangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print ("Invalid shape")

# Function that calculates area of a square given length and height
def square_area():
        length = input("Enter length: ")
        height = input("Enter height: ")
        if (len(length) > 0) and (len(height) > 0):
            if (length.isnumeric() and height.isnumeric()):
                print ("Calculating square area")
                area = float(length) * float(height)
                print ("Square area is: " + str(area))
            else:
                print ("Length and/or height is not a number!")
        else:
            print ("Length and/or height has no value!") 

# Function that calculates area of a triangle given its length and height
def triangle_area():
        length = input("Enter length: ")
        height = input("Enter height: ")
        if length.isnumeric() and height.isnumeric():
            print ("Calculating triangle area")
            area = float(length) * float(height) * 0.5
            print ("Triangle area is: " + str(area))
        else:
            print ("Length and/or height is not a number!")

# Function that calculates the area fo a circle given its radius
def circle_area():
        radius = float(input("Enter radius: "))
        pi = 3.14

        print ("Calculating circle area")
        area = pi * radius**2 
        print ("Circle area is: " + str(area))

# Calls area function    
area()