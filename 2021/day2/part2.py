puzzle_input = open('input.in').readlines()

aim = 0
horizontal = 0
depth = 0

for line in puzzle_input:
    line = line.split(" ")
    command = line[0]
    num = int(line[1])
    if command == 'up':
        aim -= num
    elif command == 'down':
        aim += num
    elif command == 'forward':
        horizontal += num
        depth += aim * num

print("answer:", depth*horizontal)