# enjoy the one liner
print("count:", sum([len(list(filter(lambda n:len(n) in [2,3,4,7],l.split(" ")))) for l in [s.strip().split(" | ")[1] for s in open('input.in').readlines()]]))
