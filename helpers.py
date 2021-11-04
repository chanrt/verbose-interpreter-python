def split_stack(line_stack):
    statements = []
    new_statement = []

    position = 0
    while position < len(line_stack) :
        if not (line_stack[position].type == "SYNTAX" and line_stack[position].value == "PERIOD"):
            new_statement.append(line_stack[position])
        else:
            statements.append(new_statement)
            new_statement = []
        position += 1
            
    if len(new_statement) > 0:
        statements.append(new_statement)
    return statements

def isExpectingMore(input_string):
    num_paren_open = 0
    num_square_open = 0
    num_braces_open = 0
    num_single_quotes = 0
    num_double_quotes = 0

    for character in input_string:
        if character == "(":
            num_paren_open += 1
        elif character == ")":
            num_paren_open -= 1
        elif character == "[":
            num_square_open += 1
        elif character == "]":
            num_square_open -= 1
        elif character == "{":
            num_braces_open += 1
        elif character == "}":
            num_braces_open -= 1
        elif character == "'":
            num_single_quotes += 1
        elif character == '"':
            num_double_quotes += 1
        elif character == "#":
            break

    if num_paren_open == 0 and num_square_open == 0 and num_braces_open == 0 and num_single_quotes % 2 == 0 and num_double_quotes % 2 == 0:
        return False
    else:
        return True