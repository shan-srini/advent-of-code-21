from collections import Counter

SIGNAL = 'signal'
VALUE = 'value'

class Day8:
    def __init__(self):
        f = open('input', 'r')
        lines = [l.split('|') for l in f.read().splitlines()]
        self.data = list()
        for l in lines:
            self.data.append({
                SIGNAL: list(filter(self.part1, [Counter(c) for ii, c in enumerate(l[0].strip().split(' '))])),
                VALUE: [Counter(c) for c in l[1].strip().split(' ')]
            })

    def run(self):
        ret = 0
        for dat in self.data:
            #print(dat[VALUE])
            #print(dat[SIGNAL]
            for x in dat[VALUE]:
                if x in dat[SIGNAL]: ret += 1
        return ret
     
    def part1(self, x):
        """ check unique digit sequence just brute pt1? """
        return len(x) in {2, 3, 4, 7}

if __name__=='__main__':
    print(Day8().run())
