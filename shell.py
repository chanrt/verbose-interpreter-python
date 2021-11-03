from commands import CommandManager
import library
from lexical_analyser import Analyser
from evaluator import Evaluator

if __name__ == "__main__":

    debug_status = True
    
    print("--> Verbose Interpreter <--\n")
    print("Repository at https://github.com/chanrt/verbose-interpreter-python")
    print("Enter @quit to exit, or just close the window\n")

    while True:
        input_string = input("> ")
        
        if CommandManager.check(input_string):
            CommandManager.execute(input_string)
        else:
            analyser = Analyser(input_string, debug = debug_status)
            line_stack = analyser.line_stack

            statements = library.split_stack(line_stack)

            for statement in statements:
                evaluator = Evaluator(statement, echo = True, debug = debug_status)

        
