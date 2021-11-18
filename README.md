# verbose-interpreter-python
 
 Verbose is intended to be a dynamically typed, completely stack-based and easily readable programming language.
 
 Run shell.py for interpreter mode.
 
 To run a program written in a file, enter "python verbose.py (filename)" in cmd
 
 program.txt contains a default program (shown below). Enter "python verbose.py program.txt" in cmd to see it's output
 
 ```
# A verbose program intended to showcase it's current features
# Type "python verbose.py program.txt" to run this program

say "Hello, World!" # Prints "Hello, World!"

# Prints firstName and lastName together
firstName is "Jane"
lastName is "Doe"
print "Full name: " + (firstName and lastName)

# Finds hypotenuse of a triangle
a = 3
b = 4
print "Hypotenuse = " + sqrt of (a square + b square)

# Proves a trignometric identity
angle = 20
print "sin^2 theta + cos^2 theta = " + (sin(angle)^2 + cos(angle)^2)

# Calculates and prints speed of light from predefined constants
print "Speed of light: " + 1 / sqrt($mu_0 * $epsilon_0)

# Calculates and prints mean
numbers are [1 2 3 4 5]
print "Mean: " + (mean of numbers)

# Prints if given number is prime or composite
num = 18
i = 1
num_factors = 0

while i < num {
    if num % i == 0 {
        increment num_factors
    }
    increment i
}

if num_factors > 1 {
    print "Composite"
} else {
    print "Prime"
}


 ```

 Current Features:
 1) Basic arithmetic, combinatorics, trigonometric, logarithmic, hyperbolic and descriptive functions
 2) Interpreter mode along with file compiler mode
 3) Variables can be assigned and referenced
 4) 2 types of data: numbers and strings
 5) Currently, parentheses are the only syntactical elements, used for specifying precedence of operations. The programming language isn't far from English
 6) Physical, chemical and mathematical constants are inbuilt, and can be referenced via the $ namespace (example: $c for speed of light)
 7) Commands in interpreter mode can be entered using the @ namespace (example: @vars for seeing all stored variables)
 8) A Line can be commenented out by entering # at the beginning
 9) File compiler mode generates logs inside the logs.txt file, containing the lexical, evaluator (at all depths) and variable stacks at various points in the program
 10) Arrays can be written and assigned to variables. Operations on arrays (like mean and lcm) have also been implemented. Single elements can be referenced by indexing (starts from 1 instead of 0), but elements obtained from indexing cannot be assigned yet
 11) Array functions such as prepend, append and insert have been implemented
 12) While loops have been implemented
 13) Conditionals have been successfully implemented
 
 Planned Features:
 1) for loops, both in Clang format and as an iterator of iterables
 2) Ability for the user to define functions
 3) Error reporting system. Currently, any errors will be shown from the python interpreter's viewpoint
