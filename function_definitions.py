import functions

function_definitions = []

unary_operations = []
binary_operations = []

class FunctionDefiner:
    def __init__(self, identifiers, function, token_type, token_value):
        self.identifiers = identifiers
        self.function = function
        self.type = token_type
        self.value = token_value

def newUnaryFunction(identifiers, function, token_type, token_value = None):
    new_function = FunctionDefiner(identifiers, function, token_type, token_value)
    function_definitions.append(new_function)
    unary_operations.append(token_type)

def newBinaryFunction(identifiers, function, token_type, token_value = None):
    new_function = FunctionDefiner(identifiers, function, token_type, token_value)
    function_definitions.append(new_function)
    binary_operations.append(token_type)

def newSpecialFunction(identifiers, function, token_type, token_value = None):
    new_function = FunctionDefiner(identifiers, function, token_type, token_value)
    function_definitions.append(new_function)

####################
# Unary operations #
####################

# Reciprocal
newUnaryFunction(["~", "reci"], functions.reci, "RECI")

# Factorial
newUnaryFunction(["fact", "factorial"], functions.fact, "FACT")

# Trigonometric
newUnaryFunction(["sin"], functions.sin, "SIN")
newUnaryFunction(["cos"], functions.cos, "COS")
newUnaryFunction(["tan"], functions.tan, "TAN")
newUnaryFunction(["cosec", "csc"], functions.cosec, "COSEC")
newUnaryFunction(["sec"], functions.sec, "SEC")
newUnaryFunction(["cot"], functions.cot, "COT")

# Inverse trigonometric
newUnaryFunction(["arcsin", "sininv"], functions.arcsin, "ARCSIN")
newUnaryFunction(["arccos", "cosinv"], functions.arccos, "ARCCOS")
newUnaryFunction(["arctan", "taninv"], functions.arctan, "ARCTAN")

# Hyperbolic
newUnaryFunction(["sinh"], functions.sinh, "SINH")
newUnaryFunction(["cosh"], functions.cosh, "COSH")
newUnaryFunction(["tanh"], functions.tanh, "TANH")

# Roots
newUnaryFunction(["sqrt", "√"], functions.sqrt, "SQRT")
newUnaryFunction(["cbrt", "∛"], functions.cbrt, "CBRT")

# Logarithmic and exponential
newUnaryFunction(["ln", "log_e"], functions.ln, "LN")
newUnaryFunction(["log", "log_10"], functions.log, "LOG")
newUnaryFunction(["exp"], functions.exp, "EXP")

# Step functions
newUnaryFunction(["floor", "gif"], functions.floor, "FLOOR")
newUnaryFunction(["ceil", "ceiling"], functions.ceil, "CEIL")
newUnaryFunction(["sign", "signum"], functions.sign, "SIGN")

# Descriptive functions
newUnaryFunction(["abs", "magn"], functions.abs, "ABS")
newUnaryFunction(["frac", "fractional"], functions.frac, "FRAC")

#####################
# Binary operations #
#####################

# Basic Arithmetic
newBinaryFunction(["^", "power"], functions.pow, "POW")
newBinaryFunction(["/", "by"], functions.divide, "DIVIDE")
newBinaryFunction(["*", "times"], functions.multiply, "MULTIPLY")
newBinaryFunction(["+", "plus", "and"], functions.add, "ADD")
newBinaryFunction(["-", "minus"], functions.subtract, "SUBTRACT")
newBinaryFunction(["%", "mod"], functions.mod, "MOD")

# Combinatorics
newBinaryFunction(["P", "permutes"], functions.perm, "PERM")
newBinaryFunction(["C", "choose"], functions.comb, "COMB")

#####################
# Special functions #
#####################

newSpecialFunction(["print", "say"], None, "PRINT")
newSpecialFunction(["=", "isEqualTo", "is"], None, "ASSIGN")