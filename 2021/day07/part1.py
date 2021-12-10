puzzle_input = open('input.in').readline().strip()

locations = sorted(list(map(int, puzzle_input.split(","))))
median = locations[int(len(locations)/2)]
fuel_spent = sum([abs(pos - median) for pos in locations])
print("fuel_spent:", fuel_spent)