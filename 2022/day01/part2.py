puzzle_input = open('input.in').readlines()

answer = 0
curr = 0

elves = []
for line in puzzle_input:
    line = line.strip()
    if line == "":
        elves.append(curr)
        curr = 0
        continue
    curr += int(line)

print(sum(sorted(elves)[-3:]))