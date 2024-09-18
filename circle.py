# importing the math package
import math

# global variable for counting the stars
star_count = 0

# global variable for width of the circle
circle_width = 0

"""
    Parameter one: integer that defines width and height of the quarter circle used to estimate value of pi
    Parameter two: boolean value that says whether the unit circle is displayed
    Method should calculate and return an estimate for pi
    If passed in boolean value is true, the method should call the third method
"""


def generate_pi_estimate(width, draw):
    # boolean check for passed in value
    # if true, calls the draw_unit_circle method
    if draw:
        draw_unit_circle(width)

    # calculating the value of pi
    pi = math.pi * width * width
    return pi


"""
    This method takes in a single parameter, where integer represents the height & width of circle to be drawn
    The method should draw a unit circle within a bounding box for the given input size
"""


def draw_unit_circle(width):
    global circle_width
    global star_count

    circle_width = width

    # calculating the distance
    max_pixel_distance = width - 0.5

    # printing top side of the box
    print("+", "-" * (width + 2), "+")

    # for looping the y-position in reversed manner
    for y_position in reversed(range(0, width)):

        # printing the left vertical bar
        print("|", end="")

        # for looping the x-position
        for x_position in range(0, width):
            distance = math.sqrt(x_position ** 2 + y_position ** 2)

            # if within bounds, print *
            if distance < max_pixel_distance:
                star_count = star_count + 1
                print("*", end="")

            # outside bounds, print " "
            else:
                print(" ", end="")
        print("    |")

    # printing bottom side of the box
    print("+", "-" * (width + 2), "+")


"""
    Method that take in a floating point number and calculates the estimate of pi that requires 
    the least amount of pixels to be within the defined delta value of pi
    The number of pixels generated should be returned as a second return value
    
"""


def generate_pi_given_error(delta):
    width_set = int(input("Please set width of your circle: "))

    pi_estimate = 4 * (star_count / width_set ** 2)
    print(pi_estimate)
    print(delta)
    pi_error = pi_estimate - delta

    return pi_error


user_input = int(input("What would you like to do?"
                       "1. Generate a pi estimate of the circle you're trying to draw? \n"
                       "2. Generate a drawing of the unit circle? \n"
                       "3. Generate a given error for the pi estimate? \n"
                       "Please enter 1, 2 or 3 only: "
                       ""))
if user_input == 1:
    set_width = int(input("Set the width of your circle: "))
    set_boolean = input("Would you like to draw the circle (y/n): ")
    if set_boolean == "y":
        set_boolean = True
    elif set_boolean == "n":
        set_boolean = False
    print(generate_pi_estimate(set_width, set_boolean))
elif user_input == 2:
    set_width = int(input("Set the width of your circle: "))
    draw_unit_circle(set_width)
elif user_input == 3:
    set_delta = float(input("Set a delta value: "))
    print(generate_pi_given_error(set_delta))
