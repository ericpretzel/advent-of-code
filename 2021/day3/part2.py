puzzle_input = [s.strip() for s in open('input.in').readlines()]

def evaluate(nums, greater, pos=0):
    print(nums)
    if len(nums) == 1:
        return nums[0]
    zeros = list(filter(lambda n: n[pos] == '0', nums))
    ones = list(filter(lambda n: n[pos] == '1', nums))
    if len(ones) > len(zeros):
        return evaluate(ones, greater, pos+1) if greater else evaluate(zeros, greater, pos+1)
    elif len(ones) == len(zeros):
        return evaluate(ones, greater, pos+1) if greater else evaluate(zeros, greater, pos+1)
    return evaluate(zeros, greater, pos+1) if greater else evaluate(ones, greater, pos+1)

oxygen_rating = evaluate(puzzle_input, greater=True)
co2_rating = evaluate(puzzle_input, greater=False)

print(oxygen_rating, co2_rating)

print("life support rating:", int(oxygen_rating, base=2)*int(co2_rating, base=2))
