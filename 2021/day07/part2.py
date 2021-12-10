puzzle_input = open('input.in').readline().strip()

cumulative_sum = lambda n: int((n*(n+1)/2))

locations = sorted(list(map(int, puzzle_input.split(","))))

fuel_spent = 9120731287634712586390178346975671235786912047856478265476238
for loc in range(locations[len(locations)-1]+1): 
    fuel_spent = min(fuel_spent, sum([cumulative_sum(abs(l - loc)) for l in locations]))


print("fuel_spent:", fuel_spent)