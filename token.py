class Token:
    def __init__(self, type, value = None):
        self.type = type
        self.value = value

    def getString(self):
        if self.value is None:
            return f"{self.type}"
        else:
            return f"{self.type}:{self.value}"