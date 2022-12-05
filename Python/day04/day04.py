with open("input", "r") as file:
    lines = file.readlines()

value = 0
for pair in lines:
    elfs = pair.split(",")
    a = [int(x) for x in elfs[0].split("-")]
    b = [int(x) for x in elfs[1].split("-")]

    if (b[0] <= a[0] <= b[1] and b[0] <= a[1] <= b[1] or
        a[0] <= b[0] <= a[1] and a[0] <= b[1] <= a[1]):
        value += 1

print("Answer Level 1:", value)

value = 0
for pair in lines:
    elfs = pair.split(",")
    a = [int(x) for x in elfs[0].split("-")]
    b = [int(x) for x in elfs[1].split("-")]

    if (b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1] or
        a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]):
        value += 1

print("Answer Level 2:", value)