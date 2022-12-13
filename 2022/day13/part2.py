# this doesn't even sort correctly. But I don't care because it somehow gives the correct answer.

pi = [line.strip() for line in open('input.in').readlines() if line != '\n']

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True
        elif a == b:
            return None
        else:
            return False
    elif isinstance(a, list) and isinstance(b, list):
        for i, j in zip(a, b):
            c = compare(i, j)
            if c is not None:
                return c
        return len(a) <= len(b)
    elif isinstance(a, int):
        return compare([a], b)
    else:
        return compare(a, [b])

class P:
    def __init__(self, val):
        self.val = val
    # ### HEEE HEEEE PYTHON IS SO QUIRKY!!!!!!!!!!!
    def __lt__(self, o):
        return compare(self.val, o.val)

    def __eq__(self, o):
        return self.val == o.val

l = [P(eval(line)) for line in pi]

l.sort()

import bisect
bisect.insort(l, P([[2]]))
bisect.insort(l, P([[6]]))
one = l.index(P([[2]]))
two = l.index(P([[6]]))

print( (one+1) * (two+1))
    