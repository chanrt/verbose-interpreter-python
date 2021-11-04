import sys, datetime
import helpers
from lexical_analyser import Analyser
from evaluator import Evaluator

if __name__ == "__main__":
    filename = sys.argv[1]
    file = open(filename, "r")
    string = file.read()
    lines = string.split("\n")

    logs = open("logs.txt", "w")
    now = datetime.datetime.now()
    logs.write(f"Logs of running {filename} at {now.strftime('%d/%m/%Y %H:%M:%S')}\n")
    logs.close()

    current_line = 0

    while current_line < len(lines):
        line = lines[current_line]
        current_line += 1

        while helpers.isExpectingMore(line):
            line += lines[current_line] + ";"
            current_line += 1

        analyser = Analyser(line, debug = False, log = True)
        evaluator = Evaluator(analyser.line_stack, echo = False, debug = False, log = True)

    file.close()