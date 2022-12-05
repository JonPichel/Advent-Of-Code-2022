from collections import deque

with open("input", "r") as file:
    contents = []
    while not (line := file.readline()).startswith(" 1 "):
        contents.append(line)

    num_stacks = len(line.split())

    stacks = [deque() for _ in range(num_stacks)]

    for line in reversed(contents):
        for i in range(len(stacks)):
            c = line[1 + i * 4]
            if c != " ":
                stacks[i].append(line[1 + i * 4])

    file.readline()
    for line in file:
        words = line.split()
        num = int(words[1])
        src = int(words[3]) - 1
        dst = int(words[5]) - 1

        for _ in range(num):
            stacks[dst].append(stacks[src].pop())

print("Answer Level 1: ", end="")
for stack in stacks:
    print(stack[-1], end="")
print()

with open("input", "r") as file:
    contents = []
    while not (line := file.readline()).startswith(" 1 "):
        contents.append(line)

    num_stacks = len(line.split())

    stacks = [deque() for _ in range(num_stacks)]

    for line in reversed(contents):
        for i in range(len(stacks)):
            c = line[1 + i * 4]
            if c != " ":
                stacks[i].append(line[1 + i * 4])

    file.readline()
    for line in file:
        words = line.split()
        num = int(words[1])
        src = int(words[3]) - 1
        dst = int(words[5]) - 1

        tmp = deque()
        for _ in range(num):
            tmp.append(stacks[src].pop())

        for _ in range(num):
            stacks[dst].append(tmp.pop())

print("Answer Level 2: ", end="")
for stack in stacks:
    print(stack[-1], end="")
print()
