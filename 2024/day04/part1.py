puzzle = [line.strip() for line in open("input.in").readlines()]

w = len(puzzle[0])
h = len(puzzle)

word = 'XMAS'

def search(y, x, dy, dx, target_idx=0):
    if y < 0 or y >= h or x < 0 or x >= w:
        return 0
    if puzzle[y][x] != word[target_idx]:
        return 0
    if target_idx == len(word) - 1 and puzzle[y][x] == word[target_idx]:
        return 1
    total_xmas = 0
    total_xmas += search(y + dy, x + dx, dy, dx, target_idx + 1)
    return total_xmas


total = 0
for y in range(h):
    for x in range(w):
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            total += search(y, x, dy, dx)


print(total)