from token import Token
from function_definitions import function_definitions
from constants import constant_definitions
from placeholder import placeholder_definitions

numbers = "0123456789"
allowed_var_chars = "_0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
alphabets = "_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
special_chars = "$"
operators = "+-*/%=^~√∛<>"
syntax = "();"

class Analyser:
    def __init__(self, input_string, debug = False, log = False):
        self.input_string = input_string
        self.position = 0
        self.line_stack = []
        self.debug = debug
        self.log = log
        self.analyse()

    def analyse(self):
        if len(self.input_string) == 0:
            logs = open("logs.txt", "a")
            logs.write(self.__str__() + "\n")
            logs.close()
        if len(self.input_string) > 0 and self.input_string[0] == "#":
            self.input_string = ""

        self.checkForPlaceholders()

        while self.position < len(self.input_string):
            character = self.input_string[self.position]

            if character in numbers:
                self.insertNumber()
                self.position -= 1
            elif character == "'" or character == '"':
                self.insertString(character)
            elif character in alphabets + special_chars:
                self.insertName()
                self.position -= 1
            elif character in operators:
                self.insertOperator()
            elif character in syntax:
                self.insertSyntax()
            elif character == "[":
                self.insertList()
            elif character == "{":
                self.insertBlock()
            elif character == "#":
                self.input_string == ""
            
            self.position += 1
        
        if self.debug and len(self.input_string) > 0:
            print(self)

        if self.log and len(self.input_string) > 0:
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

        while self.position < len(self.input_string) and self.input_string[self.position] in allowed_var_chars + special_chars:
            name_string += self.input_string[self.position]
            self.position += 1

        if self.checkForFunctions(name_string):
            pass
        elif self.checkForConstants(name_string):
            pass
        else:
            name_token = Token("NAME", name_string)
            self.line_stack.append(name_token)

            if name_token.value == "while" or name_token.value == "if" or name_token.value == "else_if" or name_token.value == "else":
                self.insertCondition()

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
        elif character == ";":
            token_value = "PERIOD"

        symbol_token = Token("SYNTAX", token_value)
        self.line_stack.append(symbol_token) 

    def insertList(self):
        start_position = self.position
        stop_position = self.getClosingSquareBracket(self.position)

        child_analyser = Analyser(self.input_string[start_position + 1: stop_position], False, False)
        items_stack = child_analyser.line_stack

        new_list = Token("LIST", items = items_stack)
        self.line_stack.append(new_list)  
        self.position = stop_position 

    def insertCondition(self):
        start_position = self.position
        stop_position = self.getOpeningBrace(start_position)   

        child_analyser = Analyser(self.input_string[start_position + 1: stop_position], False, False)
        condition_items = child_analyser.line_stack

        new_condition = Token("CONDITION", items = condition_items)
        self.line_stack.append(new_condition)
        self.position = stop_position

    def insertBlock(self):
        start_position = self.position
        stop_position = self.getClosingBrace(self.position)

        child_analyser = Analyser(self.input_string[start_position + 1: stop_position], False, False)
        block_items = child_analyser.line_stack

        new_block = Token("BLOCK", items = block_items)
        self.line_stack.append(new_block)
        self.position = stop_position

    def checkForFunctions(self, name_string):
        for function in function_definitions:
            if name_string in function.identifiers:
                function_token = Token(function.type, function.value)
                self.line_stack.append(function_token)
                return True
        return False

    def checkForConstants(self, name_string):
        for constant in constant_definitions:
            if name_string in constant.identifiers:
                constant_token = Token("NUMBER", constant.value)
                self.line_stack.append(constant_token)
                return True
        return False

    def checkForPlaceholders(self):
        for placeholder in placeholder_definitions:
            for identifier in placeholder.identifiers:
                self.input_string = self.input_string.replace(identifier, placeholder.replacement)

    def getClosingSquareBracket(self, position):
        num_opened = 0
        current_position = position
        while current_position < len(self.input_string):
            if self.input_string[current_position] == "[":
                num_opened += 1
            elif self.input_string[current_position] == "]":
                num_opened -= 1
            if num_opened == 0:
                return current_position
            current_position += 1
        return -1

    def getOpeningBrace(self, position):
        current_position = position
        while current_position < len(self.input_string):
            if self.input_string[current_position] == "{":
                return current_position
            current_position += 1
        return -1

    def getClosingBrace(self, position):
        num_opened = 0
        current_position = position
        while current_position < len(self.input_string):
            if self.input_string[current_position] == "{":
                num_opened += 1
            elif self.input_string[current_position] == "}":
                num_opened -= 1
            if num_opened == 0:
                return current_position
            current_position += 1
        return -1

    def __str__(self):
        if len(self.line_stack) > 0:
            output_string = "LEXICAL STACK: "
            for token in self.line_stack:
                output_string += token.getString() + " "
            return output_string 
        else:
            # without this, we get empty LEXICAL STACK for blank lines
            return ""



