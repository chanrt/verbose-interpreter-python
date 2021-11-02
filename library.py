import math

####################
# Binary functions #
####################

def add(a, b):
    if isinstance(a, str) and (isinstance(b, int) or isinstance(b, float)):
        b = str(b)
    elif (isinstance(a, int) or isinstance(a, float)) and isinstance(b, str):
        a = str(a)
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def mod(a, b):
    return a % b

def pow(a, b):
    return math.pow(a, b)

def perm(a, b):
    return math.factorial(a) / math.factorial(a - b)

def comb(a, b):
    return math.factorial(a) / (math.factorial(b) * math.factorial(a - b))

###################
# Unary functions #
###################

def negate(a):
    return -a

def reci(a):
    return 1/a

def fact(a):
    return math.factorial(a)

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(a):
    return math.tan(a)

def cosec(a):
    return 1 / math.sin(a)

def sec(a):
    return 1 / math.cos(a)

def cot(a):
    return 1 / tan(a)

def arcsin(a):
    return math.asin(a)

def arccos(a):
    return math.acos(a)

def arctan(a):
    return math.atan(a)

def sinh(a):
    return math.sinh(a)

def cosh(a):
    return math.cosh(a)

def tanh(a):
    return math.tanh(a)

def sqrt(a):
    return math.sqrt(a)

def cbrt(a):
    return math.pow(a, 1/3)

def ln(a):
    return math.log(a)

def log(a):
    return math.log(a, 10)

def exp(a):
    return math.exp(a)

def floor(a):
    return math.floor(a)

def ceil(a):
    return math.ceil(a)

def sign(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0

def abs(a):
    return math.fabs(a)

def frac(a):
    return a - math.floor(a)

# List operations

def mean(list):
    sum = 0
    for number in list:
        sum += number
    return sum / len(list)