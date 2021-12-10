puzzle_input = [s.strip() for s in open('input.in').readlines()]

cols = []
for bit in puzzle_input[0]:
    cols.append([int(bit)])

for i in range(1, len(puzzle_input)):
    line = puzzle_input[i]
    for j in range(0, len(line)):
        cols[j].append(int(line[j]))

gamma=""
epsilon=""
most_common_bit = lambda col: round(float(sum(col)/len(col)))
for col in cols:
    bit = most_common_bit(col)
    gamma += str(bit)
    epsilon += str(1 ^ bit)

print("power consumption:", int(gamma,base=2)*int(epsilon,base=2))