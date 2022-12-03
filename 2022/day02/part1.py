puzzle_input = [line.strip() for line in open('input.in').readlines()]


d1 = {'X': 1, 'Y': 2, 'Z': 3}
d2 = {'X': 'A', 'Y': 'B', 'Z': 'C'}

def calc_win(opp, me):
    if opp == me: return 3
    if opp == 'A':
        return 0 if me == 'C' else 6
    if opp == 'B':
        return 0 if me == 'A' else 6
    return 0 if me == 'B' else 6

s = 0
for line in puzzle_input:
    opp, me = line.split(' ')
    s += calc_win(opp, d2[me]) + d1[me]
print(s)