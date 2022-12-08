grid = []
with open('in.txt', 'r') as f:
    for line in f.readlines():
        row = map(int, line.strip())
        grid.append(list(row))

rows = len(grid)
cols = len(grid[0])
count = 0
for r in range(rows):
    for c in range(cols):
        if r == 0 or r == rows-1:
            count += 1
        elif c == 0 or c == cols-1:
            count += 1
        else:
            rc = grid[r][c]
            right = grid[r][c+1:]
            left = grid[r][:c]

            col = [row[c] for row in grid]
            up = col[:r]
            down = col[r+1:]
            # print(r, c, rc, right, left, up, down)            
            if any([rc > max(x) for x in [left, right, up, down]]):
                count += 1
                # print("inside", r, c, rc)

print(count)
