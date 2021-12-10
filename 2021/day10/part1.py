puzzle_input = [s.strip() for s in open('input.in').readlines()]

chunk = {
    ')':'(',
    ']':'[',
    '}':'{',
    '>':'<'
}
points = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}

p = 0
for line in puzzle_input:
    begin = chunk.values()
    end = chunk.keys()
    stack = []
    for char in line:
        if char in begin:
            stack.append(char)
        elif char in end:
            check = stack.pop()
            if check != chunk[char]:
                p += points[char]
                break

print("points:", p)


