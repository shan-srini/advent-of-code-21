# Advent of code Day 6 - Python

class Day6:
    def __init__(self, data):
        self.fishes = data
        # similar to something I did for d5 with the seen dict
        # could actually also use collections.Counter for this purpose
        self.fish_count = {}
        for fish in self.fishes: 
            self.fish_count[fish] = self.fish_count.get(fish, 0) + 1

    def run(self, days):
        for _ in range(days): self.new_fishes()
        return sum(self.fish_count.values())

    def new_fishes(self):
        ret = {}
        for lifespan, count in self.fish_count.items():
            ret[lifespan - 1] = count
        # handle resetting fishes
        reset_fishes = ret.get(-1, 0)
        if -1 in ret: del ret[-1]
        ret[6] = ret.get(6, 0) + reset_fishes
        ret[8] = ret.get(8, 0) + reset_fishes
        self.fish_count = ret

    # def new_fishes(self):
    #     ret = list()
    #     for fish in self.fishes:
    #         if fish == 0:
    #             ret.extend([6, 8])
    #         else:
    #             ret.append(fish - 1)
    #     self.fishes = ret

if __name__ == '__main__':
    # this imports data twice but oh well
    f = open('input', 'r')
    fish_data = list(map(int, f.read().split(',')))
    print(f"part 1: {Day6(fish_data).run(days=80)}")
    print(f"part 2: {Day6(fish_data).run(days=256)}")

"""
Initial thought for part 1
brute force, loop in range(amount_of_days)
subtract 1 from each if not 0
replace with 6 and append to list if == 0
EDIT: This was quite obviously way too slow when trying on part 2 with 256
New approach is to use a dict which keeps track of the count
subtract 1 from the keys and then handle the new fishes appropriately
"""
