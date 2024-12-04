puzzle = [line.strip() for line in open("input.in").readlines()]


def valid(r):
    diffs = [r[i+1] - r[i] for i in range(0, len(r) - 1)]
    if all(0 < d <= 3 for d in diffs) or all(-3 <= d < 0 for d in diffs):
        return True

count = 0
for line in puzzle:
    r = list(map(int, line.split()))
    for i in range(len(r)):
        check = [r[j] for j in range(len(r)) if j != i]
        if valid(check):
            count += 1
            break

print(count)