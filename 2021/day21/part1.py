with open('input.in') as f:
    line = f.readline().strip()
    p1 = int(line[line.rindex(' ')+1:])
    line = f.readline().strip()
    p2 = int(line[line.rindex(' ')+1:])

die = 0
score1 = 0
score2 = 0
rolls = 0
while score1 < 1000 and score2 < 1000:
    roll = (die*3+6)%10
    if rolls%2 == 0:
        p1 += roll
        if p1 > 10:
            p1 -= 10
        score1 += p1
    else:
        p2 += roll
        if p2 > 10:
            p2 -= 10
        score2 += p2
    die = (die+3)%10
    rolls += 1

print('result:', rolls*3*min(score1,score2))