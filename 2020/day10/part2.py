puzzle_input = sorted([int(s.strip()) for s in open('input.in')])

target = puzzle_input[len(puzzle_input)-1]
memo = {target:1}

def num_paths(val):
    if memo.get(val):
        return memo.get(val)
    next = list(filter(lambda n: n-val in [3,2,1], puzzle_input))
    paths = sum([num_paths(n) for n in next])
    memo[val] = paths
    return paths

print("num paths:", num_paths(0))