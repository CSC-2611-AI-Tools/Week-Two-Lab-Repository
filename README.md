# Theory
The area under the curve is equal to π/4 since the area of a unit circle is π x r2 = π x 12 = π. 
In this assignment, you will create your own quarter of a unit circle using a character to represent each pixel. 
A space indicates a pixel out of the circle and a * indicates a pixel inside the circle. For example:

```
+-----------+
| ***       |
| *****     |
| *******   |
| *******   |
| ********  |
| ********  |
| ********* |
| ********* |
| ********* |
+-----------+
```

The area in the quarter circle is equal to the ratio of the area in the quarter circle to the area of the square. 
The area of the square is 1 x 1 = 1, and the area under the curve is π/4 since it is a quarter of the unit circle.

The area can be approximated by counting the number of pixels. The above figure represents a 9 x 9 image. There are a
total of 81 pixels in the image and 65 of them are in the quarter circle. Therefore, we can estimate π as: 4 x 65 / 81 = 3.20

We can determine if a pixel is in the unit circle (and therefore should be displayed as an asterisk instead of a space) by 
calculating its distance from the center of the circle (the bottom left corner of the image). For example, the pixel shown 
in the following "image" as O is seven pixels above and four pixels to the right of the center of the circle.

```
+-----------+
| ***       |
| ****O     |
| *******   |
| *******   |
| ********  |
| ********  |
| ********* |
| ********* |
| ********* |
+-----------+
```

To determine if that pixel falls inside the circle, we can use the Pythagorean theorem:
- distance = squareRoot(x2 + y2)

We use a radius of 8.5 pixels since we want the distance to the center of the pixel, so if the distance to **O** is 8.5 or less, the pixel is inside the unit circle. Here we have:
- distance = squareRoot(42 + 72) = squareRoot(16 + 49) = squareRoot(65) = 8.06.

## Instructions

### Part 1: Submit in ```.ipynb``` or ```.py```
- [ ] Submit .ipynb or .py files. Make sure the file name contains your FULL NAME.

### Part 2: Creating the ```generate_pi_estimate(width, draw)```
- [ ]  Create a method ```generate_pi_estimate(width, draw)``` that takes in two parameters:
  - [ ] An integer that defines the width and height (in “pixels”) of the quarter circle you will use to estimate the value of pi with.
  - [ ] A boolean value that says whether the unit circle (with the corresponding bounding box shown above) is displayed.

### Part 3: Creating the ```draw_unit_circle(width)``` method
- [ ]  Create a method called ```draw_unit_circle(width)``` that takes in a single parameter (an integer representing the height and width of the 
- quarter circle to be drawn). This method should draw a unit circle with a corresponding bounding box for the given input size (e.g., if “9” 
- is passed into this method, the unit circle above should be drawn).

### Part 4: Creating the ```generate_pi_given_error(delta)``` method
Create a method called ```generate_pi_given_error(delta)``` that takes in a floating point number and calculates the estimate of pi that requires 
the least amount of “pixels” to be within the defined delta value of pi. The number of pixels generated should also be returned (as a second 
return value).

### Part 5: Implementing the Solution
If you implement your solution in a .py file then create a simple menu that allows a user running this script to interact with the functionality
described above. If you are using a Jupyter notebook then have one of the cells at the bottom of the notebook contain the input parameters to 
the script.


### Part 6: Submission Guidelines
Submit your implementation file to Canvas to be graded.


### Other Guidelines
Make sure your code is readable - it should follow the PEP 8 Style guide. Specifically, you should have docstrings on your methods and methods 
and variables should follow the lowercase_with_underscores naming convention.