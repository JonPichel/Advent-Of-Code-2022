with open("input", "r") as file:
    lines = file.readlines()

norm = {"X": "A", "Y": "B", "Z": "C"}
values = {"A": 1, "B": 2, "C": 3}

score = 0
for match in lines:
    options = match.strip().split(" ")
    you = options[0]
    me = norm[options[1]]

    if you == me:
        score += 3
    elif (you == "A" and me == "B" or
            you == "B" and me == "C" or
            you == "C" and me == "A"):
        score += 6
    score += values[me]

print("Answer Level 1:", score)

score = 0
for match in lines:
    options = match.strip().split(" ")
    you = options[0]

    match options[1]:
        case "X":
            me = chr((ord(you) - ord("A") - 1) % 3 + ord("A"))
        case "Y":
            me = you
            score += 3
        case "Z":
            me = chr((ord(you) - ord("A") + 1) % 3 + ord("A"))
            score += 6
    score += values[me]

print("Answer Level 2:", score)
