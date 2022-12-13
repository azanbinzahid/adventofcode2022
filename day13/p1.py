def clean(a):
    return eval(a)

def compare(a, b):
    if type(a) == type(1) and type(b) == type(1):
        return None if a == b else a < b

    elif type(a) == type([]) and type(b) == type([]):
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            chk = compare(a[i], b[i])
            if chk == None:
                i +=1
                j +=1
            else:
                return chk

        if i == len(a) and j == len(b):
            return None
        else:
            return i == len(a)

    else:
        if type(a) == type([]):
            return compare(a, [b])
        else:
            return compare([a], b)


with open('in.txt', 'r') as f:
    lines =  f.readlines()
    index = 0
    ans = 0
    for i in range(0, len(lines), 3):
        index +=1
        a = lines[i].strip()
        b = lines[i+1].strip()

        a = clean(a)
        b = clean(b)
        ans += index if compare(a, b) else 0

print(ans)