l = [line.strip() for line in open('testinput.in').readlines()]

import re

p = re.compile(r'(\d+) (red|green|blue)')

s = 0
for line in l:
    b = False
    max_red = 0
    max_green = 0
    max_blue = 0
    for token in line.split(';'):
        for a in p.finditer(token):
            amt = int(a.group(1))
            color = a.group(2)
            if color == 'red':
                max_red = max(max_red, amt)
            elif color == 'green':
                max_green = max(max_green, amt)
            elif color == 'blue':
                max_blue = max(max_blue, amt)
    print(max_red * max_green * max_blue)
    s += max_red * max_green * max_blue

print(s)

