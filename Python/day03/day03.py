from string import ascii_lowercase, ascii_uppercase
with open("input", "r") as file:
    lines = [x.strip() for x in file.readlines()]

value = 0
for rucksack in lines:
    mid = len(rucksack) // 2
    shared = list(set(rucksack[:mid]).intersection(set(rucksack[mid:])))
    assert len(shared) == 1

    match shared[0]:
        case lower if lower in ascii_lowercase:
            value += ord(lower) - ord('a') + 1
        case upper if upper in ascii_uppercase:
            value += ord(upper) - ord('A') + 27
        case _:
            raise ValueError("unexpected character")


print("Answer Level 1:", value)

value = 0
GROUPSIZE = 3
for i in range(0, len(lines), GROUPSIZE):
    group = lines[i:i + GROUPSIZE]
    badge = list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))
    assert len(badge) == 1

    match badge[0]:
        case lower if lower in ascii_lowercase:
            value += ord(lower) - ord('a') + 1
        case upper if upper in ascii_uppercase:
            value += ord(upper) - ord('A') + 27
        case _:
            raise ValueError("unexpected character")

print("Answer Level 2:", value)
