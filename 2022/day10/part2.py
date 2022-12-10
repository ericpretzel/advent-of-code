pi = [line.strip() for line in open('input.in').readlines()]

c = 0
x = 1
def draw(x, c):
    if c % 40 == 0: print()
    if c%40 in [x-1, x, x+1]:
        print('#', end='')
    else:
        print('.', end='')
    
for line in pi:
    if line == 'noop':
        draw(x, c)
        c += 1
    else:
        draw(x, c)
        c += 1
        draw(x, c)
        c += 1
        amt = int(line.split(' ')[1])
        x += amt

"""
my output:
###..####.#..#.####..##..###..####.####.
#..#.#....#.#.....#.#..#.#..#.#....#....
#..#.###..##.....#..#....#..#.###..###..
###..#....#.#...#...#....###..#....#....
#.#..#....#.#..#....#..#.#....#....#....
#..#.#....#..#.####..##..#....####.#....

(RFKZCPEF)
"""