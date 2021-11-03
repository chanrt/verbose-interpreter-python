import library
placeholder_definitions = []

class PlaceholderDefiner:
    def __init__(self, identifiers, replacement):
        self.identifiers = identifiers
        self.replacement = replacement

def addPlaceholder(identifiers, replacement):
    new_placeholder = PlaceholderDefiner(identifiers, replacement)
    placeholder_definitions.append(new_placeholder)

addPlaceholder(["of"], "")
addPlaceholder(["squared", "square"], "^ 2")
addPlaceholder(["cubed", "cube"], "^3 ")
addPlaceholder(["is lesser than"], "<")
addPlaceholder(["is greater than"], ">")
addPlaceholder(["==", "is equal to"], "equals")