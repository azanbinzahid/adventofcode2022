grid=[]
start = None
end = None
with open('in.txt', 'r') as f:
    for line in f.readlines():
        grid.append(list(line.strip()))

# find S and E, can be done while reading
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i,j)
            grid[i][j] = 'a'
        elif grid[i][j] == 'E':
            end = (i,j)
            grid[i][j] = 'z'


def is_valid(start, node):
    i, j = node
    x, y = start
    try:
        grid[i][j]
    except:
        return False
    
    return ord(grid[x][y]) - ord(grid[i][j]) >= -1

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
        if is_valid(node, n):
            valid.append(n)

    return valid


# start BFS, slow for actual input -- do smth else to faster traverse, A* may be?
def find_path_bfs(s, e, grid, visited):
    queue = [(s, [])]  # start point, empty path

    while len(queue) > 0:
        print(len(visited))
        node, path = queue.pop(0)
        path.append(node)
        visited.add(node)

        if node == e:
            return path

        adj_nodes = get_neighbors(node)
        for item in adj_nodes:
            if item not in visited:
                queue.append((item, path[:]))

    return None  # no path found

visited = set()
path = find_path_bfs(start, end, grid, visited)
print(len(path)-1)