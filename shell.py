from lexical_analyser import Analyser
from evaluator import Evaluator

if __name__ == "__main__":

    debug_status = False
    
    while True:
        input_string = input("> ")
        
        if input_string == "quit()":
            break
        else:
            analyser = Analyser(input_string, debug = debug_status)
            evaluator = Evaluator(analyser.line_stack, echo = True, debug = debug_status)

        
