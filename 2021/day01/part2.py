puzzle_input = open('input.in').readlines()

three_sum = []

increase_count = 0

for i in range(0, len(puzzle_input)-2):
    a = int(puzzle_input[i])
    b = int(puzzle_input[i+1])
    c = int(puzzle_input[i+2])
    three_sum.append(a+b+c)

for i in range (1, len(three_sum)):
    if three_sum[i-1] < three_sum[i]:
        increase_count += 1

print("increase_count:", increase_count)