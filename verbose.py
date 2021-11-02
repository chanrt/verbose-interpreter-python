import sys, datetime
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

    for line in lines:
        analyser = Analyser(line, debug = False, log = True)
        evaluator = Evaluator(analyser.line_stack, echo = False, debug = False, log = True)

    file.close()