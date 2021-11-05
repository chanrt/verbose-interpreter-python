class Variables:
    def __init__(self):
        self.stack = []
        self.num_default_vars = 0

    def printStack(self):
        output_string = "VARIABLE STACK: "
        for variable in self.stack:
            output_string += variable.getString() + ", "
        print(output_string)

    def add(self, name, value, items = None):
        self.removeAny(name)
        new_variable = Variable(name, value, items)
        self.stack.append(new_variable)

    def appendItemToList(self, list_name, item):
        for variable in self.stack:
            if variable.name == list_name:
                variable.items.append(item)

    def removeAny(self, name):
        for index, variable in enumerate(self.stack):
            if variable.name == name:
                self.stack.pop(index)

    def getVarValue(self, name):
        for variable in self.stack:
            if variable.name == name:
                return variable.value
        return None

    def getVarItems(self, name):
        for variable in self.stack:
            if variable.name == name:
                return variable.items
        return None

    def getType(self, name):
        for variable in self.stack:
            if variable.name == name:
                if variable.value is not None:
                    if isinstance(variable.value, int) or isinstance(variable.value, float):
                        return "NUMBER"
                    elif isinstance(variable.value, str):
                        return "STRING"
                elif variable.items is not None:
                    return "LIST"

    def getNumVars(self):
        return len(self.stack) - self.num_default_vars

    def writeToLogs(self):
        logs = open("logs.txt", "a")
        output_string = "VARIABLE STACK: "
        for variable in self.stack:
            output_string += variable.getString() + ", "
        logs.write(output_string + "\n")
        logs.close()

vars = Variables()

class Variable:
    def __init__(self, name, value, items):
        self.name = name
        self.value = value
        self.items = items

    def getString(self):
        if self.value is not None:
            return f"{self.name}:{self.value}"
        else:
            output_string = f"{self.name} with items: "
            for item in self.items:
                output_string += f"{item.type}:{item.value}, "
            return output_string