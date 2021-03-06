import math
import webbrowser

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

#####################
# Boolean functions #
#####################

def lesser(a, b):
    if a < b:
        return 1
    else:
        return 0

def greater(a, b):
    if a > b:
        return 1
    else:
        return 0

def lte(a, b):
    if a <= b:
        return 1
    else:
        return 0

def gte(a, b):
    if a >= b:
        return 1
    else:
        return 0

def equals(a, b):
    if a == b:
        return 1
    else:
        return 0

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

def google(a):
    search_term = str(a).replace(" ", "+")
    url = "https://www.google.com/search?q=" + search_term
    webbrowser.open(url)

def youtube(a):
    search_term = str(a).replace(" ", "+")
    url = "https://www.youtube.com/results?search_query=" + search_term
    webbrowser.open(url)

###################
# List operations #
###################

def mean(list):
    sum = 0
    for number in list:
        sum += number
    return sum / len(list)

def variance(list):
    avg = mean(list)
    sum = 0

    for number in list:
        sum += math.pow(avg - number, 2)

    return sum / len(list)

def sd(list):
    return math.sqrt(variance(list))

def lcm(list):
    current_num = max(list)

    while True:
        divide_all = True

        for num in list:
            if current_num % num != 0:
                divide_all = False
                break

        if divide_all == True:
            return current_num
        current_num += 1

def gcd(list):
    current_num = min(list)

    while current_num > 1:
        divide_all = True

        for num in list:
            if num % current_num != 0:
                divide_all = False
                break

        if divide_all == True:
            return current_num
        current_num -= 1

    return 1
        