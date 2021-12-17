f = open('input', 'r')
data = list(map(int, f.read().split(',')))

res = [sum([abs(pos - cur) for pos in data]) for cur in range(min(data), max(data)+1)]

print(f"part 1: {min(res)}")

res = [sum([sum(range(abs(pos - cur)+1)) for pos in data]) for cur in range(min(data), max(data)+1)]
print(f"part 2: {min(res)}")
