from token import Token
from variables import vars
from function_definitions import function_definitions, unary_operations, binary_operations

class Evaluator:
    def __init__(self, stack, depth = 0, echo = False, debug = False, log = False):
        self.stack = stack
        self.depth = depth
        self.echo = echo
        self.debug = debug
        self.log = log
        self.evaluate()

    def replaceKnownVars(self):
        position = 0
        while position < len(self.stack):
            if self.stack[position].type == "NAME":
                name = self.stack[position].value

                if position + 1 >= len(self.stack) or self.stack[position + 1].type != "ASSIGN":
                    for variable in vars.stack:
                        if variable.name == name:
                            number_token = Token("NUMBER", variable.value)
                            self.stack[position] = number_token
                            break
            position += 1

    def getOpenParen(self, position):
        current_position = position
        while current_position < len(self.stack):
            if self.stack[current_position].type == "SYNTAX" and self.stack[current_position].value == "LPAREN":
                return current_position
        return -1

    def getClosingParen(self, position):
        num_opened = 0
        current_position = position
        while current_position < len(self.stack):
            if self.stack[current_position].type == "SYNTAX":
                if self.stack[current_position].value == "LPAREN":
                    num_opened += 1
                elif self.stack[current_position].value == "RPAREN":
                    num_opened -= 1
                    if num_opened == 0:
                        return current_position
            current_position += 1
        return -1

    def somethingRemains(self):
        for item in self.stack:
            if item.type == "NUMBER" or item.type == "STRING":
                return True
        return False

    def printRemaining(self):
        for item in self.stack:
            if item.value is not None:
                print(item.value)
            else:
                print(item.type)

    def getRemainingEntity(self):
        remaining_entities = []

        for item in self.stack:
            if item.type == "NUMBER" or item.type == "STRING":
                remaining_entities.append(item.value)

        if len(remaining_entities) == 1:
            return remaining_entities[0]

    def evaluate(self):

        if self.debug:
            vars.printStack()
            print(self)

        if self.log and vars.getNumVars() > 0:
            vars.writeToLogs()

        # Substitute vars
        self.replaceKnownVars()

        # Evaluate expressions inside brackets
        for position, item in enumerate(self.stack):
            if item.type == "SYNTAX" and item.value == "LPAREN":
                start_position = position
                end_position = self.getClosingParen(position)
                child_evaluator = Evaluator(self.stack[start_position + 1: end_position], self.depth + 1)
                result = child_evaluator.getRemainingEntity()
                self.stack[start_position] = Token("NUMBER", result)
                
                num_delete = end_position - start_position
                while num_delete > 0:
                    self.stack.pop(start_position + 1)
                    num_delete -= 1

                if self.debug:
                    print(self)

                if self.log:
                    logs = open("logs.txt", "a")
                    logs.write(self.__str__() + "\n")
                    logs.close
        
        # Carry out unary operations
        for operation in function_definitions:
            for position, item in enumerate(self.stack):
                if item.type == operation.type:
                    if operation.type in unary_operations:
                        if self.stack[position + 1].type == "SUBTRACT":
                            negated_number_token = Token("NUMBER", -self.stack[position + 2].value)
                            self.stack[position + 1] = negated_number_token
                            self.stack.pop(position + 2)

                        right_number = self.stack[position + 1].value
                        result = operation.function(right_number)

                        new_token = Token("NUMBER", result)
                        self.stack[position] = new_token
                        self.stack.pop(position + 1)

                        if self.debug:
                            print(self)

                        if self.log:
                            logs = open("logs.txt", "a")
                            logs.write(self.__str__() + "\n")
                            logs.close

        # Carry out binary operations
        for operation in function_definitions:
            for position, item in enumerate(self.stack):
                if item.type == operation.type:
                    if operation.type in binary_operations:
                        left_number = self.stack[position - 1].value
                        right_number = self.stack[position + 1].value
                        result = operation.function(left_number, right_number)

                        new_token = Token("NUMBER", result)
                        self.stack[position] = new_token
                        self.stack.pop(position + 1)
                        self.stack.pop(position - 1)
                
                        if self.debug:
                            print(self)

                        if self.log:
                            logs = open("logs.txt", "a")
                            logs.write(self.__str__() + "\n")
                            logs.close

        # Carry out assignments
        for position, item in enumerate(self.stack):
            if item.type == "ASSIGN":
                left_variable = self.stack[position - 1].value
                right_number = self.stack[position + 1].value
                vars.add(left_variable, right_number)

                new_token = Token("NUMBER", right_number)
                self.stack[position] = new_token
                self.stack.pop(position + 1)
                self.stack.pop(position - 1)

                if self.debug:
                    print(self)

                if self.log:
                    logs = open("logs.txt", "a")
                    logs.write(self.__str__() + "\n")
                    logs.close

        # Print anything
        for position, item in enumerate(self.stack):
            if item.type == "PRINT":
                right_entity = self.stack[position + 1].value
                print(right_entity)
                self.stack.pop(position + 1)
                self.stack.pop(position)
        
        if self.echo and self.somethingRemains():
            self.printRemaining()

    def printResult(self):
        print(f"RESULT: {self.getRemainingNumber()}")

    def __str__(self):
        output_string = f"INTERPRETER STACK (depth {self.depth}): "
        for token in self.stack:
            output_string += token.getString() + " "
        return output_string

