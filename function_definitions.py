import functions

function_definitions = []

unary_operations = ["SIN", "COS", "TAN"]
binary_operations = ["ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "POW"]

class FunctionDefiner:
    def __init__(self, identifiers, function, token_type, token_value):
        self.identifiers = identifiers
        self.function = function
        self.type = token_type
        self.value = token_value

def newFunction(identifiers, function, token_type, token_value = None):
    new_function = FunctionDefiner(identifiers, function, token_type, token_value)
    function_definitions.append(new_function)

# Unary operations
newFunction(["sin"], functions.sin, "SIN")
newFunction(["cos"], functions.cos, "COS")
newFunction(["tan"], functions.tan, "TAN")
newFunction(["cosec"], functions.cosec, "COSEC")
newFunction(["sec"], functions.sec, "SEC")
newFunction(["cot"], functions.cot, "COT")
newFunction(["sqrt"], functions.sqrt, "SQRT")

# Binary operations
newFunction(["^"], functions.pow, "POW")
newFunction(["/", "by"], functions.divide, "DIVIDE")
newFunction(["*", "times"], functions.multiply, "MULTIPLY")
newFunction(["+", "plus", "and"], functions.add, "ADD")
newFunction(["-", "minus"], functions.subtract, "SUBTRACT")

# Special functions
newFunction(["print", "say"], None, "PRINT")
newFunction(["=", "isEqualTo", "is"], None, "ASSIGN")