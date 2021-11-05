import library
placeholder_definitions = []

class PlaceholderDefiner:
    def __init__(self, identifiers, replacement):
        self.identifiers = identifiers
        self.replacement = replacement

def addPlaceholder(identifiers, replacement):
    new_placeholder = PlaceholderDefiner(identifiers, replacement)
    placeholder_definitions.append(new_placeholder)

# Null placeholders
addPlaceholder(["of ", "by ", "to ", "at ", "in "], "")

# Namesake placeholders
addPlaceholder(["until"], "while")
addPlaceholder(["else if"], "else_if")

# Arithmetic placeholders
addPlaceholder(["squared", "square"], "^ 2")
addPlaceholder(["cubed", "cube"], "^3 ")

# Testing placeholders
addPlaceholder(["is odd"], "% 2 == 1")
addPlaceholder(["is even"], "% 2 == 0")
addPlaceholder(["is positive"], "> 0")
addPlaceholder(["is negative"], "< 0")
addPlaceholder(["is non negative"], ">= 0")
addPlaceholder(["is non positive"], "<= 0")

# Boolean placeholders
addPlaceholder(["is lesser than", "lesser than"], "<")
addPlaceholder(["is greater than", "greater than"], ">")
addPlaceholder(["is lesser than or equal to", "lesser than or equal to"], "<=")
addPlaceholder(["is greater than or equal to", "greater than or equal to"], ">=")
addPlaceholder(["==", "is equal to"], "equals")

