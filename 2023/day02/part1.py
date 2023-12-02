l = [line.strip() for line in open('input.in').readlines()]

import re

p = re.compile(r'(\d+) (red|green|blue)')

s = 0
i = 1
for line in l:
    b = False
    for token in line.split(';'):
        for a in p.finditer(token):
            amt = int(a.group(1))
            color = a.group(2)
            if color == 'red' and amt > 12:
                b = True
                break
            elif color == 'green' and amt > 13:
                b = True
                break
            elif color == 'blue' and amt > 14:
                b = True
                break
    if not b: s += i
            
    i += 1

print(s)

