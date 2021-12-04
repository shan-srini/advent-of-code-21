# Day 1 advent of code - python

f = open('input', 'r')
data = [int(n) for n in f.read().splitlines()]

def part_one():
    ret = 0
    prev = None
    for ii in range(len(data) - 1):
        if data[ii] < data[ii+1]: ret += 1
    return ret

def part_two():
    prev = None
    ret = 0
    for ii in range(len(data) - 2):
        cur = data[ii] + data[ii+1] + data[ii+2]
        if prev and cur > prev: ret += 1
        prev = cur
    return ret

if __name__ == '__main__':
    print(f"part 1. {part_one()}")
    print(f"part 2. {part_two()}")
