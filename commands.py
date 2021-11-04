from variables import vars

def about():
    print("\nVerbose is intended to be a dynamically typed, completely stack-based and easily readable programming language")
    print("Developed by: chanrt | Fork me at GitHub!")
    print("Version: alpha\n")

class Command:
    def __init__(self, identifiers, function):
        self.identifiers = identifiers
        self.function = function

class Commands:
    def __init__(self):
        self.definitions = []

    def add(self, string, function):
        new_command = Command(string, function)
        self.definitions.append(new_command)

    def check(self, string):
        for command in self.definitions:
            if string in command.identifiers:
                return True
        return False

    def execute(self, string):
        for command in self.definitions:
            if string in command.identifiers:
                command.function()

CommandManager = Commands()

CommandManager.add(["@quit", "@exit"], quit)
CommandManager.add(["@vars"], vars.printStack)
CommandManager.add(["@about"], about)




