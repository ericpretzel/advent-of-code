puzzle_input = [line.strip() for line in open('input.in').readlines()]


d1 = {'A': 1, 'B': 2, 'C': 3}

win = {'A': 'C', 'B': 'A', 'C': 'B'}
lose = {'A': 'B', 'B': 'C', 'C': 'A'}
def calc_win(opp, me):
    if opp == me: return 3
    if opp == 'A':
        return 0 if me == 'C' else 6
    if opp == 'B':
        return 0 if me == 'A' else 6
    return 0 if me == 'B' else 6

s = 0
for line in puzzle_input:
    opp, res = line.split(' ')
    if res == 'X':
        me = win[opp]
    elif res == 'Y':
        me = opp
    else:
        me = lose[opp]
    s += calc_win(opp, me) + d1[me]
print(s)