class Board:
    def __init__(self, nums):
        self.nums = nums
        self.count = -1
        self.is_bingo = False

    def call_num(self, num):
        if self.is_bingo: return
        self.count += 1
        for row in self.nums:
            for col in row:
                if num == col[0]:
                    col[1] = True
                    self.is_bingo = self.bingo()

    def bingo(self):
        if self.is_bingo: return True
        check = lambda line: len(list(filter(lambda num: not num[1], line))) == 0
        for i in range(0, 5):
            row = self.nums[i]
            if check(row):
                return True
            col = [self.nums[j][i] for j in range(0, 5)]
            if (check(col)):
                return True
    
    def unmarked_nums(self):
        unmarked = []
        for row in self.nums:
            for col in row:
                if not col[1]: unmarked.append(col[0])
        return unmarked

with open('input.in') as f:
    winning_numbers = [int(s) for s in f.readline().strip().split(",")]
    boards = []
    while f.readline() != "":
        board = []
        for i in range(0, 5):
            line = f.readline()
            row = [[int(s), False] for s in list(filter(None, line.strip().split(" ")))]
            board.append(row)
        boards.append(Board(board))


for num in winning_numbers:
    for board in boards:
        board.call_num(num)

max_count = -1
max_board = None
for board in boards:
    if board.count > max_count:
        max_count = board.count
        max_board = board

print("last winner:", winning_numbers[max_count] * sum(max_board.unmarked_nums()))