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
 - [ ] Create a method called ```generate_pi_given_error(delta)``` that takes in a floating point number and calculates the estimate of pi that requires 
the least amount of “pixels” to be within the defined delta value of pi. The number of pixels generated should also be returned (as a second 
return value).

### Part 5: Implementing the Solution
- [ ] If you implement your solution in a .py file then create a simple menu that allows a user running this script to interact with the functionality
described above. If you are using a Jupyter notebook then have one of the cells at the bottom of the notebook contain the input parameters to 
the script.


### Part 6: Submission Guidelines
- [ ] Submit your implementation file to Canvas to be graded.


### Other Guidelines
- [ ] Make sure your code is readable - it should follow the PEP 8 Style guide. Specifically, you should have docstrings on your methods and methods 
and variables should follow the lowercase_with_underscores naming convention.