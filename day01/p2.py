elves = []
with open('in.txt', 'r') as f:
    cal = 0
    for line in f.readlines():
        if line == '\n':
            elves.append(cal)
            cal = 0
        else:
            cal += int(line)

print(sum(sorted(elves, reverse=True)[:3]))
