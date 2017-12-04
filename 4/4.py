with open("input.txt") as f:
	passphrases = [[word for word in line.rstrip().split()] for line in f]

def part1():
	result = 0
	for passphrase in passphrases:
		pass_set = set(passphrase)
		if len(passphrase) == len(pass_set):
			result += 1
	return result

print(part1())

def part2():
	result = 0
	for passphrase in passphrases:
		temp = [''.join(sorted(word)) for word in passphrase]
		pass_set = set(temp)
		if len(pass_set) == len(temp):
			result += 1
	return result

print(part2())