puzzle = [line.strip() for line in open('input.in').readlines()]

import re

p = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

s = 0
for line in puzzle:
    for match in p.finditer(line):
        a = int(match.group(1))
        b = int(match.group(2))
        s += a * b
print(s)