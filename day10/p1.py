instructions = []
with open('in.txt', 'r') as f:
    for line in f.readlines():
        if line.startswith('noop'):
            instructions.append(0)
        else:
            instructions.append(int(line.strip().split()[1]))

cycle = 0
ins = 0
X = 1
start = 0
ans = 0

for cycle in range(2, 222):

    if instructions[ins] == 0:
        ins +=1
    else:
        start +=1
        if start == 2:
            X+=instructions[ins]
            ins +=1
            start = 0

    if cycle in [20, 60, 100, 140, 180, 220]:
        print(cycle, X)
        ans += (cycle*X)


    if ins == len(instructions):
        break

print(ans)