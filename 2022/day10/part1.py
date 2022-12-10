pi = [line.strip() for line in open('input.in').readlines()]


total = 0
c = 0
x = 1
def signal(x, c):
    s = [20, 60, 100, 140, 180, 220]
    if c in s:
        print(x , c)
        print(x*c)
        return x*c
    return 0
for line in pi:
    if line == 'noop':
        c += 1
        total += signal(x, c)
    else:
        c += 1
        total += signal(x, c)
        c += 1
        total += signal(x, c)
        amt = int(line.split(' ')[1])
        x += amt
print(total)