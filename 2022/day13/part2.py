pi = [line.strip() for line in open('input.in').readlines() if line != '\n']

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, list) and isinstance(b, list):
        for i, j in zip(a, b):
            c = compare(i, j)
            if c != 0:
                return c
        else: return len(a) - len(b)
    elif isinstance(a, int):
        return compare([a], b)
    else:
        return compare(a, [b])

l = [eval(line) for line in pi]
l.append([[2]])
l.append([[6]])

import functools
l.sort(key=functools.cmp_to_key(compare))

print( (l.index([[2]])+1) * (l.index([[6]])+1))
    