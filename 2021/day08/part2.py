puzzle_input = [s.strip() for s in open('input.in').readlines()]

position = {
    'a': {0, 2, 3, 5, 6, 7, 8, 9},
    'b': {0, 4, 5, 6, 8, 9},
    'c': {0, 1, 2, 3, 4, 7, 8, 9},
    'd': {2, 3, 4, 5, 6, 8, 9},
    'e': {0, 2, 6, 8},
    'f': {0, 1, 3, 4, 5, 6, 7, 8, 9},
    'g': {0, 2, 3, 5, 6, 8, 9}
}

signal_length = {
    2: {1},
    3: {7},
    4: {4},
    5: {2, 3, 5},
    6: {0, 6, 9},
    7: {8}
}

total = 0

for line in puzzle_input:
    line = line.split(" | ")

    possible = {}

    # generate possibilities
    for signal in line[0].split(" "):
        signal = set(signal)
        possible_nums = signal_length[len(signal)]

        for pos in position:
            if possible_nums.issubset(position[pos]):
                if possible.get(pos) is None: possible[pos] = signal
                else: possible[pos] = signal.intersection(possible[pos])

    # now good enough? lol
    while (sum([len(set) for set in possible.values()])) > 7:
        for v in filter(lambda s: len(s) == 1, possible.values()):
            pos = list(v)[0]
            for other_v in filter(lambda s: len(s) > 1, possible.values()):
                other_v.discard(pos)

    wire_mapping = {}

    for i in range(0, 10):
        letters = []
        for letter in position:
            if i in position[letter]:
                letters.append(letter)

        for j in range(len(letters)):
            letters[j] = list(possible[letters[j]])[0]

        word = ''.join(sorted(letters))
        wire_mapping[word] = i

    digits = ''
    for signal in line[1].split(" "):
        num = wire_mapping[''.join(sorted(signal))]
        digits += str(num)

    total += int(digits)

print("total:", total)
