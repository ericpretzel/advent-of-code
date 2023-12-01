import re

l = [line.strip() for line in open('day01.in').readlines()]
total = 0
p1 = re.compile(r'(\d|one|two|three|four|five|six|seven|eight|nine)')
p2 = re.compile(r'.*(\d|one|two|three|four|five|six|seven|eight|nine).*$')
for line in l:
    a = ''
    first = p1.search(line).group(1)
    last = p2.search(line).group(1)
    try:
        a += str(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].index(first))
    except: 
        a += first
    try: 
        a += str(('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine').index(last))
    except: 
        a += last
    
    total += int(a)

print(total)
