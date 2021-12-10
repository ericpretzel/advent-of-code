puzzle_input = [s.strip() for s in open('input.in').readlines()]


begin = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'
}
end = {
    ')':'(',
    ']':'[',
    '}':'{',
    '>':'<'
}
points = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}

scores = []
for line in puzzle_input:
    stack = []
    incomplete = True
    for char in line:
        if char in begin:
            stack.append(char)
        elif char in end:
            check = stack.pop()
            if check != end[char]: # invalid
                incomplete = False
                break
    if incomplete:
        p = 0
        for char in reversed(stack):
            p *= 5
            p += points[begin[char]]
        scores.append(p)

print("points:", sorted(scores)[len(scores)//2])


