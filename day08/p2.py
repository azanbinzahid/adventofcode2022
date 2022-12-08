grid = []
with open('in.txt', 'r') as f:
    for line in f.readlines():
        row = map(int, line.strip())
        grid.append(list(row))

rows = len(grid)
cols = len(grid[0])
count = 0
scenic_score = -1
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

            score = 1
            up = up[::-1]
            left = left[::-1]
            for arr in [up, left, down, right]:
                s = 0
                for i in arr:
                    if rc > i:
                        s+=1
                    elif rc <= i:
                        s+=1
                        break
                    else:
                        break
                
                if s > 0:
                    score *= s
                
            # print(rc, score)
            scenic_score = max(scenic_score, score)

print(scenic_score)
