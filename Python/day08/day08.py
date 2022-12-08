with open("input", "r") as file:
    grid = [[int(c) for c in line.strip()] for line in file.readlines()]

rows = len(grid)
cols = len(grid[0])

value = rows * cols
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        height = grid[i][j]
        hidden = True
        # Test top
        for k in range(i):
            if grid[k][j] >= height:
                break
        else:
            hidden = False
        # Test right
        for k in range(cols - 1, j, -1):
            if grid[i][k] >= height:
                break
        else:
            hidden = False
        # Test bottom
        for k in range(rows - 1, i, -1):
            if grid[k][j] >= height:
                break
        else:
            hidden = False
        # Test left
        for k in range(j):
            if grid[i][k] >= height:
                break
        else:
            hidden = False
        if hidden:
            value -= 1

print("Answer Level 1:", value)

highest = 0
# Trees around the edges will have a scenic score of 0 always
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        height = grid[i][j]
        score = 1
        # Test top
        value = 0
        for k in range(i - 1, -1, -1):
            value += 1
            if grid[k][j] >= height:
                break
        score *= value
        # Test right
        value = 0
        for k in range(j + 1, cols):
            value += 1
            if grid[i][k] >= height:
                break
        score *= value
        # Test bottom
        value = 0
        for k in range(i + 1, rows):
            value += 1
            if grid[k][j] >= height:
                break
        score *= value
        # Test left
        value = 0
        for k in range(j - 1, -1, -1):
            value += 1
            if grid[i][k] >= height:
                break
        score *= value
        if score > highest:
            highest = score

print("Answer Level 2:", highest)
