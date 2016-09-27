def balanced_brackets(s):
    """Return True if the brackets in string `s` are balanced"""
    stack = []
    left_brackets = ['(', '[', '{']
    right_brackets = [')', ']', '}']
    brackets = left_brackets + right_brackets
    matching_bracket = {'(': ')', '[': ']', '{': '}'}
    for char in s:
        if char not in brackets:
            continue
        bracket = char
        if bracket in left_brackets:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            potential_matching_bracket = stack.pop()
            if matching_bracket[potential_matching_bracket] != bracket:
                return False
    return len(stack) == 0
