buffer = ""
with open('in.txt', 'r') as f:

    for line in f.readlines():
        buffer = line
        break
    
    i = 0
    j = 4
    while j!=len(buffer):
        if len(set(buffer[i:j])) == 4:
            print(j)
            break
        else:
            i += 1
            j += 1

