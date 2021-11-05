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

                    right_entity_value = self.getValue(position + 1)
                    result = operation.function(right_entity_value)

                    new_token = autoMake(result)
                    self.stack[position] = new_token
                    self.clearGarbage(position + 1)

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
                    left_entity_value, right_entity_value = self.getValue(position - 1), self.getValue(position + 1)
                    result = operation.function(left_entity_value, right_entity_value)

                    new_token = autoMake(result)
                    self.stack[position] = new_token
                    self.clearGarbage(position - 1, position + 1)
                
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
                    left_entity_value, right_entity_value = self.getValue(position - 1), self.getValue(position + 1)
                    result = operation.function(left_entity_value, right_entity_value)

                    new_token = autoMake(result)
                    self.stack[position] = new_token
                    self.clearGarbage(position - 1, position + 1)
                
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
                    right_entity_items = self.getValue(position + 1)
                    list = []
                    for item in right_entity_items:
                        list.append(item.value)
                    result = operation.function(list)

                    new_token = autoMake(result)
                    self.stack[position] = new_token
                    self.clearGarbage(position + 1)

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
                        self.clearGarbage(position + 1)

                    elif operation.type == "DECREMENT":
                        right_entity = self.stack[position + 1]
                        right_entity_value = vars.getVarValue(right_entity.value)
                        new_value = library.subtract(right_entity_value, 1)
                        vars.add(right_entity.value, new_value)

                        new_token = autoMake(new_value)
                        self.stack[position] = new_token
                        self.clearGarbage(position + 1)

                    elif operation.type == "INCREASE":
                        target_entity = self.stack[position + 1]
                        target_entity_value = vars.getVarValue(target_entity.value)
                        info_entity_value = self.getValue(position + 2)

                        new_value = library.add(target_entity_value, info_entity_value)
                        vars.add(target_entity.value, new_value)

                        new_token = autoMake(new_value)
                        self.stack[position] = new_token
                        self.clearGarbage(position + 1, position + 2)

                    elif operation.type == "DECREASE":
                        target_entity = self.stack[position + 1]
                        target_entity_value = vars.getVarValue(target_entity.value)
                        info_entity_value - self.getValue(position + 2)

                        new_value = library.subtract(target_entity_value, info_entity_value)
                        vars.add(target_entity.value, new_value)

                        new_token = autoMake(new_value)
                        self.stack[position] = new_token
                        self.clearGarbage(position + 1, position + 2)

                    elif operation.type == "APPEND":
                        target_entity = self.stack[position + 2]
                        target_entity_items = vars.getVarItems(target_entity.value)

                        source_entity = self.stack[position + 1]
                        new_item_token = autoMake(source_entity.value)
                        target_entity_items.append(new_item_token)
                        vars.add(target_entity.value, None, target_entity_items)

                        new_token = autoMake(target_entity_items)
                        self.stack[position] = new_token
                        self.clearGarbage(position + 1, position + 2)

                    elif operation.type == "PREPEND":
                        target_entity = self.stack[position + 2]
                        target_entity_items = vars.getVarItems(target_entity.value)

                        source_entity = self.stack[position + 1]
                        new_item_token = autoMake(source_entity.value)
                        target_entity_items.insert(0, new_item_token)
                        vars.add(target_entity.value, None, target_entity_items)

                        new_token = autoMake(target_entity_items)
                        self.stack[position] = new_token
                        self.clearGarbage(position + 1, position + 2)

                    elif operation.type == "INSERT":
                        target_entity = self.stack[position + 3], 
                        target_entity_items = vars.getVarItems(target_entity.value)

                        source_entity_value = self.getValue(position + 1)
                        new_item_token = autoMake(source_entity_value)
                        position_entity_value = self.getValue(position + 2)

                        target_entity_items.insert(position_entity_value - 1, new_item_token)
                        vars.add(target_entity.value, None, target_entity_items)

                        new_token = autoMake(target_entity_items)
                        self.stack[position] = new_token
                        self.clearGarbage(position + 1, position + 2, position + 3)

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
                right_entity_value = self.getValue(position + 1)

                if isinstance(right_entity_value, int) or isinstance(right_entity_value, float) or isinstance(right_entity_value, str):
                    vars.add(left_variable, right_entity_value, None)
                    new_token = autoMake(right_entity_value)
                elif isinstance(right_entity_value, list):
                    vars.add(left_variable, None, right_entity_value)
                    new_token = autoMake(right_entity_value)

                self.stack[position] = new_token
                self.clearGarbage(position - 1, position + 1)

                if self.debug:
                    print(self)

                if self.log:
                    logs = open("logs.txt", "a")
                    logs.write(self.__str__() + "\n")
                    logs.close
                    vars.writeToLogs()

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
                    self.clearGarbage(position + 1)
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
                self.clearGarbage(position, position + 1)

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
            if isinstance(self.getValue(position), list) and self.stack[position + 1].type == "LIST":
                source_list = self.getValue(position)
                subscript_value = self.getValue(position + 1)
                index = -1
                
                if len(subscript_value) == 1 and subscript_value[0].type == "NUMBER":
                    index = subscript_value[0].value

                if index <= len(source_list):
                    element_token = source_list[index - 1]
                    self.stack[position] = element_token
                    self.clearGarbage(position + 1)
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
                    self.clearGarbage(position)
                elif self.stack[position - 1].type == "GREATER":
                    self.stack[position - 1].type = "GTE"
                    self.clearGarbage(position)
            elif self.stack[position].type == "CONDITION":
                if self.stack[position - 1].type == "NAME" and self.stack[position - 1].value == "else":
                    self.clearGarbage(position)

    # key function
    def evaluate(self):
        self.runGrouper()
        self.processCompoundOperations()
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
            if item.type == "NUMBER" or item.type == "STRING" or item.type == "LIST" or item.type == "NAME":
                return True
        return False

    def printRemaining(self):
        for position, item in enumerate(self.stack):
            if item.type == "NAME":
                print(self.getValue(position))
            elif item.type == "NUMBER" or item.type == "STRING":
                print(item.value)
            elif item.type == "LIST":
                output_string = "["
                for element in item.items:
                    output_string += str(element.value) + " "
                output_string += "\b]"
                print(output_string)
            else:
                print(item.type)

    def getRemainingEntity(self):
        remaining_entities = []

        for position, item in enumerate(self.stack):
            if item.type == "NUMBER" or item.type == "STRING" or item.type == "LIST":
                remaining_entities.append(item)
            elif item.type == "NAME":
                remaining_entities.append(autoMake(self.getValue(position)))

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

    def clearGarbage(self, *positions):
        sorted_positions = sorted(positions, reverse = True)
        for position in sorted_positions:
            self.stack.pop(position)

    def getValue(self, position):
        entity = self.stack[position]

        if entity.type == "NUMBER" or entity.type == "STRING":
            return entity.value
        elif entity.type == "LIST":
            return entity.items
        elif entity.type == "NAME":
            type = vars.getType(entity.value)
            if type == "NUMBER" or type == "STRING":
                return vars.getVarValue(entity.value)
            elif type == "LIST":
                return vars.getVarItems(entity.value)

    def __str__(self):
        output_string = f"EVALUATOR STACK (depth {self.depth}): "
        for token in self.stack:
            output_string += token.getString() + " "
        return output_string

