from collections import deque

with open("input", "r") as file:
    line = file.readline().strip()

value = 0
buffer = deque(line[:4])
for char in line:
    if len(set(buffer)) == 4:
        break
    buffer.popleft()
    buffer.append(char)
    value += 1

print("Answer Level 1:", value)

value = 0
buffer = deque(line[:14])
for char in line:
    if len(set(buffer)) == 14:
        break
    buffer.popleft()
    buffer.append(char)
    value += 1

print("Answer Level 2:", value)
