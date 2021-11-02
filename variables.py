class Variables:
    def __init__(self):
        self.stack = []
        self.num_default_vars = 0

    def printStack(self):
        output_string = "VARIABLE STACK: "
        for variable in self.stack:
            output_string += variable.getString() + ", "
        print(output_string)

    def add(self, name, value):
        self.removeAny(name)
        new_variable = Variable(name, value)
        self.stack.append(new_variable)

    def removeAny(self, name):
        for index, variable in enumerate(self.stack):
            if variable.name == name:
                self.stack.pop(index)

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
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getString(self):
        return f"{self.name}:{self.value}"