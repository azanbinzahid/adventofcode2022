stacks = {}
with open('in.txt', 'r') as f:

    for line in f.readlines():
        # start reading in chunks of 4 e.g. "[X] "
        crates = list(map(''.join, zip(*[iter(line)]*4)))

        # if it is empty line or the labels from crate stacks, do nothing
        if crates == [] or crates[0] == ' 1  ':
            continue
        
        # if its not a move statement, then it is a crate in the stack
        elif crates[0] != 'move':
            for i, crate in enumerate(crates):
                i = i+1
                crate = crate.strip().strip("]").strip("[")

                # skip if no crate in stack
                if crate == "":
                    pass
                else:
                    stacks.setdefault(i, []).insert(0, crate)

        else:
            # we know we will get three ints in this line. Use regex for better readability
            move, frm, to = [int(s) for s in line.split() if s.isdigit()]

            # move crates
            for m in range(move):
                crate = stacks[frm].pop()
                stacks[to].append(crate)

# sort the stacks based on the key (can also be handled while building stacks)
stacks = sorted(stacks.items(), key=lambda x: x[0])
ans = "".join([x[-1] for _, x in stacks])
print(ans)