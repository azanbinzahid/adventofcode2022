


priority = 0
with open('in.txt', 'r') as f:
    a, b, count = [], [], 0
    for line in f.readlines():
        count += 1
        if count <= 3:
            a.append(line.strip())
        elif count <= 6:
            b.append(line.strip())  
            if count == 6:
                a = set.intersection(set(a[0]), set(a[1]), set(a[2]))
                b = set.intersection(set(b[0]), set(b[1]), set(b[2]))
                ab = list(a) + list(b)
                s = [ord(_) - (64-26 if _ <= 'Z' else 96) for _ in ab]
                priority += sum(s)
                a, b, count = [], [], 0

print(priority)