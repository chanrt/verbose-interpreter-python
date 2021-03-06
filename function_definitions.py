import library

function_definitions = []

unary_operations = []
binary_operations = []
boolean_operations = []
list_operations = []
compound_functions = []

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

def newBooleanFunction(identifiers, function, token_type, token_value = None):
    new_function = FunctionDefiner(identifiers, function, token_type, token_value)
    function_definitions.append(new_function)
    boolean_operations.append(token_type)

def newListFunction(identifiers, function, token_type, token_value = None):
    new_function = FunctionDefiner(identifiers, function, token_type, token_value)
    function_definitions.append(new_function)
    list_operations.append(token_type)

def newSpecialFunction(identifiers, function, token_type, token_value = None):
    new_function = FunctionDefiner(identifiers, function, token_type, token_value)
    function_definitions.append(new_function)

def newCompoundFunction(identifiers, function, token_type, token_value = None):
    new_function = FunctionDefiner(identifiers, function, token_type, token_value)
    compound_functions.append(token_type)
    function_definitions.append(new_function)

####################
# Unary operations #
####################

# Reciprocal
newUnaryFunction(["~", "reci"], library.reci, "RECI")

# Factorial
newUnaryFunction(["fact", "factorial"], library.fact, "FACT")

# Trigonometric
newUnaryFunction(["sin"], library.sin, "SIN")
newUnaryFunction(["cos"], library.cos, "COS")
newUnaryFunction(["tan"], library.tan, "TAN")
newUnaryFunction(["cosec", "csc"], library.cosec, "COSEC")
newUnaryFunction(["sec"], library.sec, "SEC")
newUnaryFunction(["cot"], library.cot, "COT")

# Inverse trigonometric
newUnaryFunction(["arcsin", "sininv"], library.arcsin, "ARCSIN")
newUnaryFunction(["arccos", "cosinv"], library.arccos, "ARCCOS")
newUnaryFunction(["arctan", "taninv"], library.arctan, "ARCTAN")

# Hyperbolic
newUnaryFunction(["sinh"], library.sinh, "SINH")
newUnaryFunction(["cosh"], library.cosh, "COSH")
newUnaryFunction(["tanh"], library.tanh, "TANH")

# Roots
newUnaryFunction(["sqrt", "???"], library.sqrt, "SQRT")
newUnaryFunction(["cbrt", "???"], library.cbrt, "CBRT")

# Logarithmic and exponential
newUnaryFunction(["ln", "log_e"], library.ln, "LN")
newUnaryFunction(["log", "log_10"], library.log, "LOG")
newUnaryFunction(["exp"], library.exp, "EXP")

# Step functions
newUnaryFunction(["floor", "gif"], library.floor, "FLOOR")
newUnaryFunction(["ceil", "ceiling"], library.ceil, "CEIL")
newUnaryFunction(["sign", "signum"], library.sign, "SIGN")

# Descriptive functions
newUnaryFunction(["abs", "magn"], library.abs, "ABS")
newUnaryFunction(["frac", "fractional"], library.frac, "FRAC")

# Internet functions
newUnaryFunction(["google"], library.google, "GOOGLE")
newUnaryFunction(["youtube"], library.youtube, "YOUTUBE")

#####################
# Binary operations #
#####################

# Basic Arithmetic
newBinaryFunction(["^", "power"], library.pow, "POW")
newBinaryFunction(["/", "by"], library.divide, "DIVIDE")
newBinaryFunction(["*", "times"], library.multiply, "MULTIPLY")
newBinaryFunction(["+", "plus", "and"], library.add, "ADD")
newBinaryFunction(["-", "minus"], library.subtract, "SUBTRACT")
newBinaryFunction(["%", "mod"], library.mod, "MOD")

# Combinatorics
newBinaryFunction(["P", "permutes"], library.perm, "PERM")
newBinaryFunction(["C", "choose"], library.comb, "COMB")

######################
# Boolean operations #
######################

newBinaryFunction(["<="], library.lte, "LTE")
newBinaryFunction([">="], library.lte, "GTE")
newBinaryFunction(["<"], library.lesser, "LESSER")
newBinaryFunction([">"], library.greater, "GREATER")
newBinaryFunction(["equals"], library.equals, "EQUALS")

##################
# List functions #
##################

newListFunction(["mean", "avg", "average"], library.mean, "MEAN")
newListFunction(["sd", "std_dev"], library.sd, "SD")
newListFunction(["variance"], library.variance, "VARIANCE")
newListFunction(["lcm"], library.lcm, "LCM")
newListFunction(["gcd", "hcf"], library.gcd, "GCD")

#####################
# Special functions #
#####################

newSpecialFunction(["print", "say", "display"], None, "PRINT")
newSpecialFunction(["=", "isEqualTo", "is", "are"], None, "ASSIGN")

######################
# Compound functions #
######################

newCompoundFunction(["increment"], None, "INCREMENT")
newCompoundFunction(["decrement"], None, "DECREMENT")
newCompoundFunction(["increase"], None, "INCREASE")
newCompoundFunction(["decrease"], None, "DECREASE")

newCompoundFunction(["append"], None, "APPEND")
newCompoundFunction(["prepend"], None, "PREPEND")
newCompoundFunction(["insert"], None, "INSERT")