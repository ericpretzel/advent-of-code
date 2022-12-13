pi = [line.strip() for line in open('input.in').readlines()]

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

ordered = 0
p = 1
for i in range(0, len(pi), 3):
    a, b = map(eval, pi[i:i+2])
    if compare(a, b):
        ordered += p
    p += 1

print(ordered)
    