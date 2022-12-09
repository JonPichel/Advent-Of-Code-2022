with open("input", "r") as file:
    lines = file.readlines()

def print_grid(
        visited: set[tuple[int, int]],
        knots: list[tuple[int, int]]
) -> None:
    pp = list(visited) + knots
    pp = list(zip(*pp))
    limits_x = min(pp[0]), max(pp[0])
    limits_y = min(pp[1]), max(pp[1])

    tail = len(knots) - 1
    for j in range(limits_y[1], limits_y[0] - 1, -1):
        for i in range(limits_x[0], limits_x[1] + 1):
            try:
                n = knots.index((i, j))
                if n == 0:
                    print("H", end="")
                elif n == tail:
                    print("T", end="")
                else:
                    print(n, end="")
                continue
            except ValueError:
                pass
            if i == 0 and j == 0:
                print("s", end="")
            elif (i, j) in visited:
                print("#", end="")
            else:
                print(".", end="")
        print()

def move_tail(head, tail):
    head_neighs = {
        (head[0] + 1, head[1] + 1),
        (head[0] + 1, head[1]),
        (head[0] + 1, head[1] - 1),
        (head[0], head[1] + 1),
        (head[0], head[1]),
        (head[0], head[1] - 1),
        (head[0] - 1, head[1] + 1),
        (head[0] - 1, head[1]),
        (head[0] - 1, head[1] - 1),
    }

    if tuple(tail) not in head_neighs:
        # Move tail
        distance = (head[0] - tail[0], head[1] - tail[1])
        match distance:
            # Same row
            case (dx, 0):
                if dx > 0:
                    tail[0] += 1
                else:
                    tail[0] -= 1
            # Same col
            case (0, dy):
                if dy > 0:
                    tail[1] += 1
                else:
                    tail[1] -= 1
            # Otherwise
            case (dx, dy):
                if dx > 0:
                    tail[0] += 1
                else:
                    tail[0] -= 1
                if dy > 0:
                    tail[1] += 1
                else:
                    tail[1] -= 1

head = [0, 0]
tail = [0, 0]
debug = False
visited = {tuple(tail)}
for move in lines:
    words = move.split()
    direction = words[0]
    num_moves = int(words[1])
    match direction:
        case "U":
            delta = (0, 1)
        case "R":
            delta = (1, 0)
        case "D":
            delta = (0, -1)
        case "L":
            delta = (-1, 0)
        case other:
            raise ValueError

    for _ in range(num_moves):
        head[0] += delta[0]
        head[1] += delta[1]

        move_tail(head, tail)
        visited.add(tuple(tail))
        if debug:
            print_grid(visited, [tuple(knot) for knot in (head, tail)])
            input()

print("Answer Level 1:", len(visited))

NUM_KNOTS = 10
knots = [[0, 0] for _ in range(NUM_KNOTS)]
debug = False
visited = {tuple(knots[0])}
for move in lines:
    words = move.split()
    direction = words[0]
    num_moves = int(words[1])
    match direction:
        case "U":
            delta = (0, 1)
        case "R":
            delta = (1, 0)
        case "D":
            delta = (0, -1)
        case "L":
            delta = (-1, 0)
        case other:
            raise ValueError

    for _ in range(num_moves):
        head = knots[0]
        head[0] += delta[0]
        head[1] += delta[1]

        for i in range(1, NUM_KNOTS):
            head = knots[i - 1]
            tail = knots[i]
            move_tail(head, tail)
        visited.add(tuple(tail))
        if debug:
            print_grid(visited, [tuple(knot) for knot in knots])
            input()

print("Answer Level 2:", len(visited))