from enum import Enum
class Ordering:
    RIGHT = -1
    WRONG = 0
    CONTINUE = 1

def compare(a, b):
    ta = type(a)
    tb = type(b)

    if ta == int and tb == int:
        if a < b:
            return Ordering.RIGHT
        elif a == b:
            return Ordering.CONTINUE
        else:
            return Ordering.WRONG
    else:
        if ta != list:
            a = [a]
        elif tb != list:
            b = [b]
        for ia, ib in zip(a, b):
            match compare(ia, ib):
                case Ordering.RIGHT:
                    return Ordering.RIGHT
                case Ordering.WRONG:
                    return Ordering.WRONG
        if len(a) != len(b):
            if len(a) < len(b):
                return Ordering.RIGHT
            return Ordering.WRONG
        return Ordering.CONTINUE


def convert(line):
    # Base case
    if line[0] != "[":
        return int(line)

    # Empty list
    if len(line) == 2:
        return []

    brackets = 0
    idx_start = 1
    x = []
    for i in range(1, len(line) - 1):
        if line[i] == "," and not brackets:
            x.append(convert(line[idx_start:i]))
            idx_start = i+1
        if line[i] == "[":
            brackets += 1
        elif line[i] == "]":
            brackets -= 1
    x.append(convert(line[idx_start:-1]))
    return x


with open("input", "r") as file:
    value = 0
    idx = 1
    while True:
        a = convert(file.readline().strip())
        b = convert(file.readline().strip())
        match compare(a, b):
            case Ordering.RIGHT | Ordering.CONTINUE:
                # print(idx)
                value += idx
        idx += 1
        if not file.readline():
            break

    print("Answer Level 1:", value)

with open("input", "r") as file:
    packets = [convert(line.strip()) for line in file.readlines() if line != "\n"]
packets.extend([[[2]], [[6]]])

from functools import cmp_to_key
packets.sort(key=cmp_to_key(compare))

key = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
print("Answer Level 2:", key)