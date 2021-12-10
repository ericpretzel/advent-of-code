class Board:
    def __init__(self, nums):
        self.nums = nums
        self.count = 0

    def call_num(self, num):
        for row in self.nums:
            for col in row:
                if num == col[0]:
                    self.count += 1
                    col[1] = True
                    return True

    def bingo(self):
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
        if board.call_num(num):
            if board.bingo():
                print("winning score:", num*sum(board.unmarked_nums()))
                exit()