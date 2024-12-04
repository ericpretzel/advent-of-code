puzzle = [line.strip() for line in open("input.in").readlines()]

count = 0
for line in puzzle:
    r = list(map(int, line.split()))
    diffs = [r[i+1] - r[i] for i in range(0, len(r) - 1)]
    if all(0 < d <= 3 for d in diffs) or all(-3 <= d < 0 for d in diffs):
        count += 1

print(count)