import functools

def clean(a):
    return eval(a)

def compare(a, b):
    if type(a) == type(1) and type(b) == type(1):
        return 0 if a == b else -11 if a < b else 1

    elif type(a) == type([]) and type(b) == type([]):
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            chk = compare(a[i], b[i])
            if chk == 0:
                i +=1
                j +=1
            else:
                return chk

        if i == len(a) and j == len(b):
            return 0
        else:
            return -1 if i == len(a) else 1

    else:
        if type(a) == type([]):
            return compare(a, [b])
        else:
            return compare([a], b)


with open('in.txt', 'r') as f:
    all = []
    lines =  f.readlines() + ["", "[[2]]", "[[6]]"]
    index = 0
    ans = 0
    for i in range(0, len(lines), 3):
        index +=1
        a = lines[i].strip()
        b = lines[i+1].strip()

        a = clean(a)
        b = clean(b)
        all.extend([a, b])    

    all.sort(key=functools.cmp_to_key(compare))
    for j, signal in enumerate(all, 1):
        if signal == [[2]]:
            x = j
        if signal == [[6]]:
            print(x * j)
            break
# print(ans)