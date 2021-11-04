import helpers
from token import Token, autoMake
from variables import vars
from function_definitions import *

class Evaluator:
    def __init__(self, stack, depth = 0, echo = False, debug = False, log = False):
        self.stack = stack
        self.depth = depth
        self.echo = echo
        self.debug = debug
        self.log = log

        self.loop_control = False
        self.loop_limit = 10

        self.evaluate()

    def processUnaryOperations(self):
        for operation in function_definitions:
            for position, item in enumerate(self.stack):
                if item.type == operation.type and operation.type in unary_operations:
                    # Handle unary operations on negated numbers
                    if self.stack[position + 1].type == "SUBTRACT":
                        negated_number_token = Token("NUMBER", -self.stack[position + 2].value)
                        self.stack[position + 1] = negated_number_token
                        self.stack.pop(position + 2)

                    right_number = self.stack[position + 1].value
                    result = operation.function(right_number)

                    new_token = autoMake(result)
                    self.stack[position] = new_token
                    self.stack.pop(position + 1)

                    if self.debug:
                        print(self)

                    if self.log:
                        logs = open("logs.txt", "a")
                        logs.write(self.__str__() + "\n")
                        logs.close

    def processBinaryOperations(self):
        for operation in function_definitions:
            for position, item in enumerate(self.stack):
                if item.type == operation.type and operation.type in binary_operations:
                    left_entity = self.stack[position - 1].value
                    right_entity = self.stack[position + 1].value
                    result = operation.function(left_entity, right_entity)

                    new_token = autoMake(result)
                    self.stack[position] = new_token
                    self.stack.pop(position + 1)
                    self.stack.pop(position - 1)
                
                    if self.debug:
                        print(self)

                    if self.log:
                        logs = open("logs.txt", "a")
                        logs.write(self.__str__() + "\n")
                        logs.close
    
    def processBooleanOperations(self):
        for operation in function_definitions:
            for position, item in enumerate(self.stack):
                if item.type == operation.type and operation.type in boolean_operations:
                    left_entity = self.stack[position - 1].value
                    right_entity = self.stack[position + 1].value
                    result = operation.function(left_entity, right_entity)

                    new_token = autoMake(result)
                    self.stack[position] = new_token
                    self.stack.pop(position + 1)
                    self.stack.pop(position - 1)
                
                    if self.debug:
                        print(self)

                    if self.log:
                        logs = open("logs.txt", "a")
                        logs.write(self.__str__() + "\n")
                        logs.close

    def processListOperations(self):
        for operation in function_definitions:
            for position, item in enumerate(self.stack):
                if item.type == operation.type and operation.type in list_operations:
                    right_list = self.stack[position + 1]
                    list = []
                    for item in right_list.items:
                        list.append(item.value)
                    result = operation.function(list)

                    new_token = autoMake(result)
                    self.stack[position] = new_token
                    self.stack.pop(position + 1)

                    if self.debug:
                        print(self)

                    if self.log:
                        logs = open("logs.txt", "a")
                        logs.write(self.__str__() + "\n")
                        logs.close

    def processCompoundOperations(self):
        for operation in function_definitions:
            for position, item in enumerate(self.stack):
                if item.type == operation.type and operation.type in compound_functions:
                    if operation.type == "INCREMENT":
                        right_entity = self.stack[position + 1]
                        right_entity_value = vars.getVarValue(right_entity.value)
                        new_value = library.add(right_entity_value, 1)
                        vars.add(right_entity.value, new_value)

                        new_token = autoMake(new_value)
                        self.stack[position] = new_token
                        self.stack.pop(position + 1)

                    elif operation.type == "DECREMENT":
                        right_entity = self.stack[position + 1]
                        right_entity_value = vars.getVarValue(right_entity.value)
                        new_value = library.subtract(right_entity_value, 1)
                        vars.add(right_entity.value, new_value)

                        new_token = autoMake(new_value)
                        self.stack[position] = new_token
                        self.stack.pop(position + 1)

                    elif operation.type == "INCREASE":
                        target_entity = self.stack[position + 1]
                        target_entity_value = vars.getVarValue(target_entity.value)
                        info_entity = self.stack[position + 2]

                        if info_entity.type == "NUMBER":
                            info_entity_value = info_entity.value
                        elif info_entity == "NAME":
                            info_entity_value = vars.getVarValue(info_entity.value)

                        new_value = library.add(target_entity_value, info_entity_value)
                        vars.add(target_entity.value, new_value)

                        new_token = autoMake(new_value)
                        self.stack[position] = new_token
                        self.stack.pop(position + 2)
                        self.stack.pop(position + 1)

                    elif operation.type == "DECREASE":
                        target_entity = self.stack[position + 1]
                        target_entity_value = vars.getVarValue(target_entity.value)
                        info_entity = self.stack[position + 2]

                        if info_entity.type == "NUMBER":
                            info_entity_value = info_entity.value
                        elif info_entity == "NAME":
                            info_entity_value = vars.getVarValue(info_entity.value)

                        new_value = library.subtract(target_entity_value, info_entity_value)
                        vars.add(target_entity.value, new_value)

                        new_token = autoMake(new_value)
                        self.stack[position] = new_token
                        self.stack.pop(position + 2)
                        self.stack.pop(position + 1)

                    if self.debug:
                        print(self)

                    if self.log:
                        logs = open("logs.txt", "a")
                        logs.write(self.__str__() + "\n")
                        logs.close

    def makeAssignments(self):
        for position, item in enumerate(self.stack):
            if item.type == "ASSIGN":
                left_variable = self.stack[position - 1].value
                right_entity = self.stack[position + 1]
                vars.add(left_variable, right_entity.value, right_entity.items)

                if self.log:
                    vars.writeToLogs()

                new_token = Token(right_entity.type, right_entity.value, right_entity.items)
                self.stack[position] = new_token
                self.stack.pop(position + 1)
                self.stack.pop(position - 1)

                if self.debug:
                    print(self)

                if self.log:
                    logs = open("logs.txt", "a")
                    logs.write(self.__str__() + "\n")
                    logs.close

    def processParentheses(self):
        for position, item in enumerate(self.stack):
            if item.type == "SYNTAX" and item.value == "LPAREN":
                start_position = position
                end_position = self.getClosingParen(position)
                child_evaluator = Evaluator(self.stack[start_position + 1: end_position], self.depth + 1, self.echo, self.debug, self.log)
                result_token = child_evaluator.getRemainingEntity()
                self.stack[start_position] = Token(result_token.type, result_token.value, result_token.items)
                
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

    def printStatements(self):
        for position, item in enumerate(self.stack):
            if item.type == "PRINT":
                right_entity = self.stack[position + 1].value
                print(right_entity)
                self.stack.pop(position + 1)
                self.stack.pop(position)

    def replaceKnownVars(self):
        position = 0
        while position < len(self.stack):
            if self.stack[position].type == "NAME":
                name = self.stack[position].value

                if position + 1 >= len(self.stack) or self.stack[position + 1].type != "ASSIGN":
                    for variable in vars.stack:
                        if variable.name == name:
                            if variable.value is not None:
                                new_token = Token(Token.getTypeFromValue(variable.value), variable.value)
                                self.stack[position] = new_token
                                break
                            elif variable.items is not None:
                                new_token = Token("LIST", None, variable.items)
                                self.stack[position] = new_token
                                break
            position += 1

    def manageArrayIndices(self):
        position = 0
        while position + 1 < len(self.stack):
            if self.stack[position].type == "LIST" and self.stack[position + 1].type == "LIST":
                array_token = self.stack[position]
                subscript_token = self.stack[position + 1]
                index = -1
                
                if len(subscript_token.items) == 1 and subscript_token.items[0].type == "NUMBER":
                    index = subscript_token.items[0].value

                if index <= len(array_token.items):
                    element_token = array_token.items[index - 1]
                    self.stack[position] = element_token
                    self.stack.pop(position + 1)
                else:
                    # Out of array bounds
                    pass
            position += 1

    def handleConditionals(self):
        block_level = 0
        if self.ifBlockExists():
            condition_evaluator = Evaluator(self.stack[1].items.copy(), self.depth + 1, False, False, False)
            if condition_evaluator.getBoolResult() == True:
                block_statements = helpers.split_stack(self.stack[2].items.copy())
                for statement in block_statements:
                    statement_evaluator = Evaluator(statement, self.depth + 1, False, False, False)
                # block ends here
            else:
                while True:
                    block_level += 1
                    if self.elifBlockExists(block_level):
                        condition_evaluator = Evaluator(self.stack[3 * block_level + 1].items.copy(), self.depth + 1, False, False, False)
                        if condition_evaluator.getBoolResult() == True:
                            block_statements = helpers.split_stack(self.stack[3 * block_level + 2].items.copy())
                            for statement in block_statements:
                                statement_evaluator = Evaluator(statement, self.depth + 1, False, False, False)
                            # some condition has been satisfied, so quit
                            break
                    elif self.elseBlockExists(block_level):
                        block_statements = helpers.split_stack(self.stack[3 * block_level + 1].items.copy())
                        for statement in block_statements:
                            statement_evaluator = Evaluator(statement, self.depth + 1, False, False, False)
                        # last conditional block has been executed, so quit
                        break
                    else:
                        # no more conditonals blocks
                        break

    def handleLoops(self):
        times = 0
        if len(self.stack) > 2 and self.stack[0].value == "while" and self.stack[1].type == "CONDITION" and self.stack[2].type == "BLOCK":
            while True:
                if self.loop_control and times >= self.loop_limit:
                    break

                condition_evaluator = Evaluator(self.stack[1].items.copy(), self.depth + 1, False, False, False)
                if condition_evaluator.getBoolResult() == True:
                    block_statements = helpers.split_stack(self.stack[2].items.copy())
                    for statement in block_statements:
                        statement_evaluator = Evaluator(statement, self.depth + 1, False, False, False)
                    times += 1
                else:
                    break

    def runGrouper(self):
        for position, index in enumerate(self.stack):
            if self.stack[position].type == "ASSIGN":
                if self.stack[position - 1].type == "LESSER":
                    self.stack[position - 1].type = "LTE"
                    self.stack.pop(position)
                elif self.stack[position - 1].type == "GREATER":
                    self.stack[position - 1].type = "GTE"
                    self.stack.pop(position)
            elif self.stack[position].type == "CONDITION":
                if self.stack[position - 1].type == "NAME" and self.stack[position - 1].value == "else":
                    self.stack.pop(position)

    # key function
    def evaluate(self):
        self.runGrouper()
        self.processCompoundOperations()
        self.replaceKnownVars()
        self.manageArrayIndices()

        if self.debug:
            print(self)

        self.processParentheses()
        self.handleConditionals()
        self.handleLoops()
        self.processUnaryOperations()
        self.processBinaryOperations()
        self.processBooleanOperations()
        self.processListOperations()
        self.makeAssignments()
        self.printStatements()
        
        if self.echo and self.somethingRemains() and self.depth == 0:
            self.printRemaining()

    # Helper functions from here on
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
                remaining_entities.append(item)

        if len(remaining_entities) == 0:
            return None
        elif len(remaining_entities) == 1:
            return remaining_entities[0]

    def getBoolResult(self):
        remaining_entity = self.getRemainingEntity()

        if remaining_entity is None:
            return False
        if remaining_entity.type == "NUMBER":
            if remaining_entity.value == 0:
                return False
            else:
                return True

    def ifBlockExists(self):
        return len(self.stack) > 2 and self.stack[0].value == "if" and self.stack[1].type == "CONDITION" and self.stack[2].type == "BLOCK"

    def elifBlockExists(self, block_level):
        return len(self.stack) > 3 * block_level + 2 and self.stack[3 * block_level].value == "else_if" and self.stack[3 * block_level + 1].type == "CONDITION" and self.stack[3 * block_level + 2].type == "BLOCK"

    def elseBlockExists(self, block_level):
        return len(self.stack) > 3 * block_level + 1 and self.stack[3 * block_level].value == "else" and self.stack[3 * block_level + 1].type == "BLOCK"

    def __str__(self):
        output_string = f"EVALUATOR STACK (depth {self.depth}): "
        for token in self.stack:
            output_string += token.getString() + " "
        return output_string

