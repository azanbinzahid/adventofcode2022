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
print("#", end="")
for cycle in range(1, 240):
    sprit = ["."]*40

    if instructions[ins] == 0:
        ins +=1
    else:
        start +=1
        if start == 2:
            X+=instructions[ins]
            ins +=1
            start = 0

    sprit[X] = "#"
    if X+1<len(sprit):
        sprit[X+1] = "#"
    if X-1 >= 0:
        sprit[X-1] = "#"

    print(sprit[(cycle) % 40], end="")
    if cycle+1 in [40, 80, 120, 160, 200, 240]:
        print("")

    if ins == len(instructions):
        break