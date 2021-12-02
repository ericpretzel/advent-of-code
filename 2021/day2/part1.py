puzzle_input = open('input.in').readlines()

vertical = 0
horizontal = 0

for line in puzzle_input:
    line = line.split(" ")
    command = line[0]
    num = int(line[1])
    if command == 'up':
        vertical -= num
    elif command == 'down':
        vertical += num
    elif command == 'forward':
        horizontal += num

print("answer:", vertical*horizontal)