puzzle_input = open('input.in').readlines()

answer = 0
curr = 0
for line in puzzle_input:
    line = line.strip()
    if line == "":
        curr = 0
        continue
    curr += int(line)
    answer = max(answer, curr)

print(answer)