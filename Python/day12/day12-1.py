import time

VISUALIZE = False
DTIME = 1 / 30

with open("input", "r") as file:
    grid = [[ord(c) for c in line.strip()] for line in file.readlines()]

rows = len(grid)
cols = len(grid[0])

def print_map(visited, edges, rows, cols):
    for j in range(rows):
        string = []
        for i in range(cols):
            if (i, j) in visited:
                string.append("V")
            elif (i, j) in edges:
                string.append("E")
            else:
                string.append(".")
        print("".join(string))
    print("\n")

# Transform the grid to a more manageable format
for j in range(rows):
    for i in range(cols):
        c = grid[j][i]
        if ord("a") <= c <= ord("z"):
            grid[j][i] = c - ord("a")
        elif c == ord("S"):
            start = (i, j)
            grid[j][i] = 0
        elif c == ord("E"):
            end = (i, j)
            grid[j][i] = 25
        else:
            raise ValueError

# Generate the graph
graph = {}
for j in range(rows):
    for i in range(cols):
        h = grid[j][i]
        connections = []
        for nj, ni in ((j, i - 1), (j, i + 1), (j - 1, i), (j + 1, i)):
            # Check if neighbor is at most one level higher
            if 0 <= ni < cols and 0 <= nj < rows:
                if grid[nj][ni] <= h + 1:
                    connections.append((ni, nj))
        graph[(i, j)] = connections

# Breadth-first search
edges = {start}
visited = set()
found = False
steps = 0
next_frame = time.time() + DTIME
while not found:
    if (VISUALIZE):
        if (now := time.time()) < next_frame:
            continue
        next_frame = now + DTIME
        print_map(visited, edges, rows, cols)
    new_edges = set()
    for edge in edges:
        conns = graph[edge]
        if end in conns:
            found = True
            break
        for neigh in conns:
            if neigh not in visited:
                new_edges.add(neigh)
        visited.add(edge)
    steps += 1
    edges = new_edges

print("Answer Level 1:", steps)