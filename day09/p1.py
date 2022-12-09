# set these to whatever value, works best with sample
x, y = 4, 0
a, b = 4, 0


visited = set()

# starting position
visited.add((a,b))


# set these grid size whatever value, works best with sample
# def print_grid():
#     global x, y, a, b, grid
#     for i in range(5):
#         for j in range(6):
#             if (i,j) == (x,y):
#                 print("H", end="")
#             elif (i, j) == (a,b):
#                 print("T",end="")
#             else:
#                 print(".",end="")
#         print("")
#     print("")
    
# def print_tail():
#     global visited
#     for i in range(5):
#         for j in range(6):
#             if (i,j) in visited:
#                 print("#", end="")
#             else:
#                 print(".",end="")
#         print("")
#     print("")


def move(dir):
    global x, y, a, b, visited

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
    if abs(a-x) >1 or abs(b-y) > 1:
        if dir in ["U", "D"]:
            b = y
            a = (a-1) if dir == "U" else (a+1)
        elif dir in ["R", "L"]:
            a = x
            b = (b-1) if dir == "L" else (b+1)
        
        visited.add((a, b))

    # debug on sample
    # print_grid()
    return x, y, a, b



with open('in.txt', 'r') as f:
    for line in f.readlines():
        dir, unit = line.strip().split()
        unit = int(unit)

        # debug on sample
        # print("==", dir, unit, "==")
        for _ in range(unit):
            x, y, a, b = move(dir)


# debug on sample
# print_tail()
# print(visited)

print(len(visited))
