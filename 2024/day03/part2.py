puzzle = [line.strip() for line in open('input.in').readlines()]

import re

p = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
do = re.compile(r'do\(\)')
dont = re.compile(r"don't\(\)")

s = 0
dummy = type('', (), {})()
dummy.start = lambda: 999999999

enabled = True

for line in puzzle:
    pos = 0
    while pos < len(line):
        mul = p.search(line, pos) or dummy
        do_it = do.search(line, pos) or dummy
        dont_do = dont.search(line, pos) or dummy

        print(mul.start(), do_it.start(), dont_do.start())

        if mul.start() < do_it.start() and mul.start() < dont_do.start():
            a = int(mul.group(1))
            b = int(mul.group(2))
            if enabled:
                s += a * b
            pos = mul.end()
        elif do_it.start() < mul.start() and do_it.start() < dont_do.start():
            enabled = True
            pos = do_it.end()
        elif dont_do.start() < mul.start() and dont_do.start() < do_it.start():
            enabled = False
            pos = dont_do.end()
        else:
            break

print(s)