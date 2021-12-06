# Advent of code Day 5 - Python

class Day5:
    def __init__(self):
        f = open('input', 'r')
        # split lines, then split by arrow for [string loc1, string loc2] then split each loc
        self.data = [list(map(lambda x: list(map(int, x.split(','))), line.split(' -> '))) for line in f.read().splitlines()]
        self.seen = dict()

    def run(self):
        for line in self.data:
            x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
            # horizontal
            if x1 == x2:
                for yy in range(min(y1, y2), max(y1, y2) + 1):
                    self.seen[(x1, yy)] = self.seen.get((x1, yy), 0) + 1
            # vertical
            elif y1 == y2:
                for xx in range(min(x1, x2), max(x1, x2) + 1):
                    self.seen[(xx, y1)] = self.seen.get((xx, y1), 0) + 1
            # diagonal
            elif abs(x1 - x2) == abs(y1 - y2):
                xs = iter(range(x1, x2 + 1 if x2 > x1 else x2 - 1, 1 if x2 > x1 else -1))
                ys = iter(range(y1, y2 + 1 if y2 > y1 else y2 - 1, 1 if y2 > y1 else -1))
                for _ in range(abs(x1 - x2) + 1):
                    pos = (next(xs), next(ys))
                    self.seen[pos] = self.seen.get(pos, 0) + 1
            else:
                raise Exception("not implemented?")
        ret = []
        for key, val in self.seen.items():
            if val > 1: ret.append(key)
        return len(ret)

if __name__ == '__main__':
    print(Day5().run())

"""
Initial thought for part 1 is
Map of coordinates seen
key - tuple of x, y
val - times seen
"""
