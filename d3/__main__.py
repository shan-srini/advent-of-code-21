# Day 1 advent of code - python

f = open('input', 'r')
data = [l for l in f.read().splitlines()]

class Day3:
    def part_one():
        '''
        Went with my first instinct...
        Thought it might be a bit inefficient so I quickly profiled
        O(n*m) where n is len(data) and m is len(data[0])
        '''
        # assume non empty, assume all nums are same length
        tracker = [0 for _ in range(len(data[0]))]
        for ll in data:
            cur_num = [-1 if x == '0' else 1 for x in ll]
            tracker = [sum(nums) for nums in zip(cur_num, tracker)] 
        # convert to string of binary repr to calc gamma
        tracker = ['1' if x > 0 else '0' for x in tracker]
        gamma = int(''.join(tracker), 2)
        # flip bits for epsilon... TODO: Bitwise XOR?
        tracker = ['1' if x == '0' else '0' for x in tracker]
        epsilon = int(''.join(tracker), 2)
        return gamma * epsilon

    def part_two():
        oxygen = Day3.ls_rating(lambda len1, len0: len1 >= len0)
        co2 = Day3.ls_rating(lambda len1, len0: len1 < len0)
        return int(oxygen, 2) * int(co2, 2)
        
    def ls_rating(eval_len1_vs_len0):
        kept = data
        for ii in range(len(data[0])):
            if len(kept) == 1: break
            tracker = {0: [], 1: []}
            for bin_num in kept:
                if bin_num[ii] == '0': tracker[0].append(bin_num)
                elif bin_num[ii] == '1': tracker[1].append(bin_num)
                length_0 = len(tracker[0])
                length_1 = len(tracker[1])
                if eval_len1_vs_len0(length_1, length_0):
                    kept = tracker[1]
                else:
                    kept = tracker[0]
        return kept[0]

if __name__ == '__main__':
    print(f"Day 3 part 1: {Day3.part_one()}")
    print(f"Day 3 part 2: {Day3.part_two()}")
