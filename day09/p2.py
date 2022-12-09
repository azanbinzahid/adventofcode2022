# set these to whatever value, works best with sample
x, y = 4, 0
ta, tb = [4]*9, [0]*9


visited = set()

# starting position
visited.add((ta[-1],tb[-1]))           


# set these grid size whatever value, works best with sample
# def print_grid():
#     global x, y, ta, tb
#     grid = [ ["."]*6 for i in range(5)]
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if (i,j) == (x,y):
#                 grid[i][j] = "H"
#             else:
#                 for k in range(8):
#                     if (i, j) == (ta[k],tb[k]):
#                         grid[i][j] = k+1
#                         break

#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             print(grid[i][j], end="")
#         print("")
#     print("")
        

def move(dir):
    global x, y, visited, ta, tb

    # move Head
    if dir == "U":
        x-=1
    elif dir == "D":
        x+=1
    elif dir == "L":
        y-=1
    elif dir == "R":
        y+=1


    # move Tail if head not adjecent
    if abs(ta[0]-x) >1:
        ta[0] = ta[0]+1 if ta[0] < x else ta[0]-1
        tb[0] = y
    elif abs(tb[0]-y) > 1:
        tb[0] = tb[0]+1 if tb[0]<y else tb[0]-1
        ta[0] = x

    for i in range(1, len(ta)):
        a, b = ta[i-1], tb[i-1]
        if abs(ta[i]-a) >1:
            ta[i] = ta[i]+1 if ta[i] < a else ta[i]-1
            if tb[i] != b:
                tb[i] = tb[i]+1 if tb[i]<b else tb[i]-1

            # tb[i] = b
        elif abs(tb[i]-b) > 1:
            tb[i] = tb[i]+1 if tb[i]<b else tb[i]-1
            if ta[i] !=a:
                ta[i] = ta[i]+1 if ta[i] < a else ta[i]-1

    visited.add((ta[-1], tb[-1]))
    # print_grid()


with open('in.txt', 'r') as f:
    for line in f.readlines():
        dir, unit = line.strip().split()
        unit = int(unit)

        print("==", dir, unit, "==")
        for _ in range(unit):
            move(dir)
            
print(len(visited))
