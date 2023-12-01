l = [line.strip() for line in open('day01.in').readlines()]
total=0
for a in l:
    num = ''
    for c in a:
        if c.isdigit(): 
            num += c
            break
        
    for c in reversed(a):
        if c.isdigit():
            num += c
            break
    total += int(num)

print(total)

