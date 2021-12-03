# Day 1 advent of code - python

f = open('input', 'r')
data = [l for l in f.read().splitlines()]

class Day2:
    def part_one():
        # loc = horizontal, depth
        loc = [0, 0]
        for ll in data:
            cmd, delt = Day2.parse(ll)
            if cmd == 'forward':
                loc[0] += delt
            elif cmd == 'down':
                loc[1] += delt
            elif cmd == 'up':
                loc[1] -= delt
        return loc[0] * loc[1]

    def part_two():
        state = { 'hor': 0, 'dep': 0, 'aim': 0 }
        for ll in data:
            cmd, delt = Day2.parse(ll)
            if cmd == 'forward':
                state['hor'] += delt
                state['dep'] += state['aim'] * delt
            elif cmd == 'down':
                state['aim'] += delt
            elif cmd == 'up':
                state['aim'] -= delt
        return state['hor'] * state['dep']

    def parse(line):
        cmd, delt = line.split(' ')
        return cmd, int(delt)

if __name__ == '__main__':
    print(f"part one {Day2.part_one()}")
    print(f"part two {Day2.part_two()}")
