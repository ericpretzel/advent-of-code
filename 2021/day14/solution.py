rules = {}
with open('input.in') as f:
    template = f.readline().strip()
    f.readline() # empty line
    puzzle_input = [s.strip().split(" -> ") for s in f.readlines()]
    for line in puzzle_input:
        rules[(line[0][0], line[0][1])] = line[1][0]

letter_count = {}
for letter in template: # get the starting letters
    letter_count[letter] = letter_count.get(letter, 0) + 1

def insert(pairs, depth):
    if depth > 0:
        new_pairs = {}
        for pair in pairs:
            num = pairs[pair]
            letter = rules[pair]
            pair1 = (pair[0], letter)
            pair2 = (letter, pair[1])
            new_pairs[pair1] = new_pairs.get(pair1, 0) + num
            new_pairs[pair2] = new_pairs.get(pair2, 0) + num
            letter_count[letter] = letter_count.get(letter, 0) + num
        insert(new_pairs, depth-1)

for i in range(len(template)-1):
    pair = (template[i], template[i+1])
    insert({pair: 1}, depth=40) # change depth to 10 for part1

print("result:", max(letter_count.values()) - min(letter_count.values()))