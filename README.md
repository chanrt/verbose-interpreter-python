# verbose-interpreter-python
 
 Verbose is intended to be a dynamically typed, completely stack-based and easily readable programming language.
 
 Run shell.py for interpreter mode.
 
 To run a program written in a file, enter "python verbose.py <filename>" in cmd
 
 program.txt contains a default program. Enter "python verbose.py program.txt" in cmd to see it's output

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
 
 Planned Features:
 1) Arrays, loops and conditionals will be implemented (preferably in that order) for this language to have semblance of Turing completeness
 2) Ability for the user to define functions
 3) Error reporting system. Currently, any errors will be shown from the python interpreter's viewpoint
