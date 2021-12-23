with open('input.in') as f:
    line = f.readline().strip()
    p1 = int(line[line.rindex(' ')+1:])
    line = f.readline().strip()
    p2 = int(line[line.rindex(' ')+1:])

sums = []
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            sums.append(i+j+k)

memo = {}
def roll(p1, p2, s1, s2, turn):
    if (p1,p2,s1,s2,turn) in memo:
        return memo[(p1,p2,s1,s2,turn)]
    if s1 >= 21:
        return (1,0)
    if s2 >= 21:
        return (0,1)
    if turn: # player 1's turn
        w1, w2 = 0, 0
        for s in sums:
            p = p1 + s
            if p > 10: p -= 10
            wins = roll(p,p2,s1+p,s2,not turn)
            w1 += wins[0]
            w2 += wins[1]
        memo[(p1,p2,s1,s2,turn)] = (w1, w2)
        return (w1, w2)
    else: # player 2's turn
        w1, w2 = 0, 0
        for s in sums:
            p = p2 + s
            if p > 10: p -= 10
            wins = roll(p1,p,s1,s2+p,not turn)
            w1 += wins[0]
            w2 += wins[1]
        memo[(p1,p2,s1,s2,turn)] = (w1, w2)
        return (w1, w2)

print('greater:', max(roll(p1,p2,0,0,True)))