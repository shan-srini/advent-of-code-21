# Advent of code Day 4 - Python

RIGHT = 'right'
LEFT = 'left'
DOWN = 'down'
UP = 'up'

class Day3:
    def __init__(self):
        f = open('input', 'r')
        data = [l for l in f.read().splitlines()]
        self.moves = data.pop(0).split(',')
        self.boards = []
        self.initialize_boards(data)
        
    def initialize_boards(self, data):
        # prepare data for parsing
        del data[0]
        data.append(None)

        board_data = []
        for l in data:
            if not l: 
                self.boards.append(Board(board_data))
                board_data = []
                continue
            row_parsed = ([x for x in l.split(' ') if x])
            board_data.append(row_parsed)
        # for b in self.boards: print(b.board)

    def play_to_win(self):
        for move in self.moves:
            for board in self.boards:
                board.mark(move)
                if board.check_win():
                    return board.score(move)
        raise Exception("No one won?")

    def play_to_lose(self):
        # I'm trying to think of clever things here but can't oh well!
        ret = { *self.boards }
        for move in self.moves:
            for board in ret:
                board.mark(move)
            if len(ret) == 1 and ret[-1].check_win():
                return ret[-1].score(move)
            ret = list(filter(lambda x: not x.check_win(), ret))
        raise Exception("No one lost?")
            
class Board:
    def __init__(self, board):
        self.board = board
        # O(1) moves at sake of space
        self.access = dict()
        self.init_data()

    def init_data(self):
        self.board = [list(map(Piece, row)) for row in self.board]
        for rr, row in enumerate(self.board):
            self.init_row_neighbors(row, rr)
            # throw pieces in a dict for O(1) moves
            for p in row: self.access[p.val] = p

    def init_row_neighbors(self, row, row_num):
        # only check up and left
        for ii, piece in enumerate(row):
            if ii > 0:
                piece.set_direction(LEFT, row[ii-1])
                piece.surround[LEFT].set_direction(RIGHT, piece)
            if row_num > 0:
                piece.set_direction(UP, self.board[row_num - 1][ii])
                piece.surround[UP].set_direction(DOWN, piece)
    
    def mark(self, val):
        if val in self.access:
            self.access[val].mark()

    def check_win(self):
        # check vertical
        hor = any([self.board[0][ii].check_direction(DOWN) for ii in range(len(self.board))])
        ver = any([self.board[ii][0].check_direction(RIGHT) for ii in range(len(self.board))])
        return hor or ver

    def score(self, final_val):
        return self.sum_unmarked() * int(final_val)

    def sum_unmarked(self):
        return sum([int(p.val) for row in self.board for p in row if not p.marked])

    def __repr__(self):
        return '\n'.join(map(str, self.board))

class Piece:
    def __init__(self, val):
        self.val = val
        self.marked = False
        self.surround = { RIGHT: None, LEFT: None, DOWN: None, UP: None }

    def set_direction(self, direction, piece):
        self.surround[direction] = piece

    def mark(self):
        self.marked = True

    def check_direction(self, direction):
        if not self.marked: return False
        if self.surround[direction]:
            return self.surround[direction].check_direction(direction)
        else:
            return True

    def __repr__(self):
        return f"{self.val} - {self.marked}"

if __name__ == '__main__':
    runner = Day3()
    print(f"Part 1: {runner.play_to_win()}")
    print(f"Part 2: {runner.play_to_lose()}")
