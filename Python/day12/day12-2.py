with open("input", "r") as file:
    grid = [[ord(c) for c in line.strip()] for line in file.readlines()]

rows = len(grid)
cols = len(grid[0])

# Transform the grid to a more manageable format
ends = []
for j in range(rows):
    for i in range(cols):
        c = grid[j][i]
        if c == ord("S") or c == ord("a"):
            grid[j][i] = 0
            ends.append((i, j))
        elif ord("a") < c <= ord("z"):
            grid[j][i] = c - ord("a")
        elif c == ord("E"):
            # This is our start point now
            start = (i, j)
            grid[j][i] = 25
        else:
            raise ValueError

from dataclasses import dataclass

@dataclass
class Node:
    neighbors: list
    visited: bool = False
    target: bool = False

# Generate the graph
graph = {}
for j in range(rows):
    for i in range(cols):
        h = grid[j][i]
        neighbors = []
        for nj, ni in ((j, i - 1), (j, i + 1), (j - 1, i), (j + 1, i)):
            # Check which points you could have come from
            if 0 <= ni < cols and 0 <= nj < rows:
                if grid[nj][ni] >= h - 1:
                    neighbors.append((ni, nj))
        if h == 0:
            graph[(i, j)] = Node(neighbors, target=True)
        else:
            graph[(i, j)] = Node(neighbors)

frontier = {start}
distance = 0
found = False
while not found:
    new_frontier = set()
    for node in frontier:
        node = graph[node]
        for neigh in node.neighbors:
            if graph[neigh].target:
                found = True
                break
            if not graph[neigh].visited:
                new_frontier.add(neigh)
        if found:
            break
        node.visited = True
    distance += 1
    frontier = new_frontier

print("Answer Level 2:", distance)
