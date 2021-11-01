from token import Token
from function_definitions import function_definitions

numbers = "0123456789"
allowed_var_chars = "_0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
alphabets = "_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
operators = "+-*/%=^!"
syntax = "()"

class Analyser:
    def __init__(self, input_string, debug = False, log = False):
        self.input_string = input_string
        self.position = 0
        self.line_stack = []
        self.debug = debug
        self.log = log
        self.analyse()

    def analyse(self):
        while self.position < len(self.input_string):
            character = self.input_string[self.position]

            if character in numbers:
                self.insertNumber()
                self.position -= 1
            elif character == "'" or character == '"':
                self.insertString(character)
            elif character in alphabets:
                self.insertName()
                self.position -= 1
            elif character in operators:
                self.insertOperator()
            elif character in syntax:
                self.insertSyntax()
            
            self.position += 1
        
        if self.debug:
            print(self)

        if self.log:
            logs = open("logs.txt", "a")
            logs.write(self.__str__() + "\n")
            logs.close()

    def insertNumber(self):
        number_string = ""
        num_dots = 0

        while self.position < len(self.input_string) and self.input_string[self.position] in numbers + ".":
            if self.input_string[self.position] == ".":
                num_dots += 1
            
            if num_dots > 1:
                break

            number_string += self.input_string[self.position]
            self.position += 1

        if num_dots == 0:
            value = int(number_string)
        else:
            value = float(number_string)

        number_token = Token("NUMBER", value)
        self.line_stack.append(number_token)

    def insertString(self, beginner):
        string = ""
        self.position += 1

        while self.position < len(self.input_string) and self.input_string[self.position] != beginner:
            string += self.input_string[self.position]
            self.position += 1
        
        string_token = Token("STRING", string)
        self.line_stack.append(string_token)

    def insertName(self):
        name_string = ""

        while self.position < len(self.input_string) and self.input_string[self.position] in allowed_var_chars:
            name_string += self.input_string[self.position]
            self.position += 1

        token_resolved = False

        # see if name matches a function
        for function in function_definitions:
            if name_string in function.identifiers:
                function_token = Token(function.type, function.value)
                self.line_stack.append(function_token)
                token_resolved = True
        
        if not token_resolved:
            name_token = Token("NAME", name_string)
            self.line_stack.append(name_token)

    def insertOperator(self):
        character = self.input_string[self.position]

        for function in function_definitions:
            if character in function.identifiers:
                operator_token = Token(function.type, function.value)
                self.line_stack.append(operator_token)

    def insertSyntax(self):
        character = self.input_string[self.position]
        token_value = None

        if character == "(":
            token_value = "LPAREN"
        elif character == ")":
            token_value = "RPAREN"

        symbol_token = Token("SYNTAX", token_value)
        self.line_stack.append(symbol_token)

    def __str__(self):
        output_string = "LINE STACK: "
        for token in self.line_stack:
            output_string += token.getString() + " "
        return output_string 



