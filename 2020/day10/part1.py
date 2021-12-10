# include outlet
puzzle_input = [0] + sorted([int(s.strip()) for s in open('input.in')])
one = 0
three = 1 # because of adapter
for i in range(1, len(puzzle_input)):
    diff = puzzle_input[i] - puzzle_input[i-1]
    if diff == 3:
        three += 1
    elif diff == 1: 
        one += 1

print("result:", one*three)