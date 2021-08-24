

def check(brackets):

    stack = []

    for idx, bracket in enumerate(brackets, start=1):
        if bracket in '()[]{}':
            if bracket in '([{':
                stack.append((bracket, idx))
            else:
                if len(stack) == 0:
                    return idx

                sb = stack[-1][0] + bracket
                if sb in ['()', '[]', '{}']:
                    stack.pop()
                else:
                    return idx

    print(brackets, stack)
    return stack.pop()[1] if stack else 0


assert check("{{{[][][]") == 3
assert check("([](){([])})") == 0
assert check("()[]}") == 5
assert check("{{[()]]") == 7
assert check("{*{{}") == 3
assert check("[[*") == 2
assert check("{*}") == 0
assert check("{{") == 2
assert check("{}") == 0
assert check("") == 0
assert check("}") == 1
assert check("*{}") == 0
assert check("{{{**[][][]") == 3
