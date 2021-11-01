class Variables:
    def __init__(self):
        self.stack = []

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

vars = Variables()

class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getString(self):
        return f"{self.name}:{self.value}"