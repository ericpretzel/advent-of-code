puzzle_input = open('input.in').readline().strip()

fish = list(map(int, puzzle_input.split(",")))

fish_count = {}
for i in range(0, 9): fish_count[i] = 0

num_days = 256 # change to 80 for part 1

for f in fish:
    fish_count[f] += 1

for i in range(num_days):
    # give birth
    birthed = fish_count[0]
    # shift everything down
    for j in range(1, len(fish_count.values())):
        fish_count[j-1] = fish_count[j]
    fish_count[8] = birthed
    fish_count[6] += birthed

print("fish:", sum(fish_count.values()))



