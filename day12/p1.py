grid=[]
start = None
end = None
with open('in.txt', 'r') as f:
    for line in f.readlines():
        line = list(line.strip())
        
        # get start and end while reading
        if 'S' or 'E' in line:
            for i, c in enumerate(line):
                if c == 'S':
                    start = len(grid), i
                    line[i] = 'a'
                elif c == 'E':
                    end = len(grid), i
                    line[i] = 'z'

        grid.append(line)

print(grid, start, end)

def is_valid(frm, to):
    i, j = frm
    x, y = to

    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        return ord(grid[i][j]) - ord(grid[x][y]) >= -1

    return False

def get_neighbors(node):
    i, j = node
    neighbors = [
        (i-1, j),
        (i+1, j),
        (i, j+1),
        (i, j-1),
    ]

    valid = []
    for n in neighbors:
        if is_valid(frm=node, to=n):
            valid.append(n)

    return valid

def find_path_bfs(s, e):
    queue = [(s, [])]
    visited = set()

    while len(queue) > 0:
        # print(len(queue))
        node, path = queue.pop(0)
        path.append(node)

        if node == e:
            return path

        for item in get_neighbors(node):
            if item not in visited:
                visited.add(item)
                queue.append((item, path[:]))


    return None  # no path found

path = find_path_bfs(start, end)
print(path)
print(len(path)-1)