VISUAL = True

with open("example", "r") as file:
    lines = [line.strip() for line in file.readlines()]


def print_map(xlim, ylim, source, rocks, sands):
    for y in range(ylim[0], ylim[1] + 1):
        line = []
        for x in range(xlim[0], xlim[1] + 1):
            point = (x, y)
            if point in sands:
                line.append('o')
            elif point in rocks:
                line.append('#')
            elif point == source:
                line.append('+')
            else:
                line.append('.')
        print("".join(line))


source = (500, 0)
rocks = set()
for formation in lines:
    points = [(int(x), int(y)) for x, y in (point.split(',') for point in formation.split(" -> "))]

    # Add rock formations
    for i in range(len(points) - 1):
        a = points[i + 1]
        b = points[i]
        if a[0] != b[0]:
            # Horizontal line
            y = a[1]
            if a[0] > b[0]:
                for x in range(b[0], a[0] + 1):
                    rocks.add((x, y))
            else:
                for x in range(a[0], b[0] + 1):
                    rocks.add((x, y))
        else:
            # Vertical line
            x = a[0]
            if a[1] > b[1]:
                for y in range(b[1], a[1] + 1):
                    rocks.add((x, y))
            else:
                for y in range(a[1], b[1] + 1):
                    rocks.add((x, y))


def move_sand(sand):
    below = (sand[0], sand[1] + 1)
    if below not in rocks and below not in sands:
        return below
    left = (sand[0] - 1, sand[1] + 1)
    if left not in rocks and left not in sands:
        return left
    right = (sand[0] + 1, sand[1] + 1)
    if right not in rocks and right not in sands:
        return right
    return None


xx = [rock[0] for rock in rocks] + [source[0]]
yy = [rock[1] for rock in rocks] + [source[1]]
xlim = min(xx) - 1, max(xx) + 1
ylim = min(yy) - 1, max(yy) + 1

abyss = False
sands = set()
while True:
    if VISUAL:
        print_map(xlim, ylim, source, rocks, sands)
        input()
    sand = source
    while True:
        if sand[1] > ylim[1]:
            abyss = True
            break
        if new := move_sand(sand):
            sand = new
        else:
            break
    if not abyss:
        sands.add(sand)
    else:
        break


print("Answer Level 1:", len(sands))

# Add floor formation
for dx in range(-ylim[1] - 1, ylim[1] + 2):
    rocks.add((source[0] + dx, ylim[1] + 1))

xx = [rock[0] for rock in rocks] + [source[0]]
yy = [rock[1] for rock in rocks] + [source[1]]
xlim = min(xx) - 1, max(xx) + 1
ylim = min(yy) - 1, max(yy) + 1

sands = set()
while True:
    if VISUAL:
        print_map(xlim, ylim, source, rocks, sands)
        input()
    sand = source
    while True:
        if new := move_sand(sand):
            sand = new
        else:
            break
    sands.add(sand)
    if sand == source:
        break


print("Answer Level 2:", len(sands))
