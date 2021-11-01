import sys
from lexical_analyser import Analyser
from evaluator import Evaluator

if __name__ == "__main__":
    filename = sys.argv[1]
    file = open(filename, "r")
    string = file.read()
    lines = string.split("\n")

    for line in lines:
        analyser = Analyser(line, debug = True)
        evaluator = Evaluator(analyser.line_stack, echo = False, debug = True)

    file.close()