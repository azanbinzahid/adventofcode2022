overlap = 0
with open('in.txt', 'r') as f:
    for line in f.readlines():
        a, b = line.strip().split(",")
        ax, ay = map(int, a.split("-"))
        bx, by = map(int, b.split("-"))
        
        if ax>bx:
            ax, bx, ay, by = bx, ax, by, ay

        if (ay>=bx):
            overlap+=1

print(overlap)