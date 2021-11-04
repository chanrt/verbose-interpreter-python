class Token:
    def __init__(self, type, value = None, items = None):
        self.type = type
        self.value = value
        self.items = items

    def getString(self):
        if self.value is None and self.items is None:
            return f"{self.type}"
        elif self.items is None:
            return f"{self.type}:{self.value}"
        else:
            output_string = f"{self.type} with items: "
            for item in self.items:
                output_string += item.getString() + ", "
            return output_string

    def getTypeFromToken(token):
        if isinstance(token.value, int) or isinstance(token.value, float):
            return "NUMBER"
        elif isinstance(token.value, str):
            return "STRING"
        elif token.value is None and token.items is not None:
            return "LIST"

    def getTypeFromValue(value):
        if isinstance(value, int) or isinstance(value, float):
            return "NUMBER"
        elif isinstance(value, str):
            return "STRING"

def autoMake(value):
    type = Token.getTypeFromValue(value)
    return Token(type, value)