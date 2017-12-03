import itertools

with open('input.txt') as f:
    lines = [[int(n) for n in line.split()] for line in f]

part1 = sum(max(line) - min(line) for line in lines)
print(part1)

part2 = sum(b//a for line in lines for a,b in itertools.combinations(sorted(line),2) if b%a==0)
print(part2)

