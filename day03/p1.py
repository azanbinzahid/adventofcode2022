


priority = 0
with open('in.txt', 'r') as f:
    for line in f.readlines():
        a, b = line[:len(line)//2], line[len(line)//2:]
        a = set([_ for _ in a])
        b = set([_ for _ in b])
        ab = a.intersection(b)
        s = [ord(_) - (64-26 if _ <= 'Z' else 96) for _ in ab]
        priority += sum(s)

print(priority)