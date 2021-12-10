puzzle_input = [int(s.strip()) for s in open('input.in').readlines()]

num = 556543474 # from part 1

front = 0
back = 1
window_sum = sum(puzzle_input[front:back+1])

while window_sum != num and back > front:
    if window_sum > num:
        # shrink window
        window_sum -= puzzle_input[front]
        front += 1
    elif window_sum < num:
        # extend window
        back += 1
        window_sum += puzzle_input[back]


print("weakness:", min(puzzle_input[front:back+1])\
    + max(puzzle_input[front:back+1]))