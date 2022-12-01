with open("input", "r") as file:
    lines = file.readlines()

elf_calories = []
calories = 0
for line in lines:
    if line == '\n':
        elf_calories.append(calories)
        calories = 0
        continue
    calories += int(line)

print("Answer Level 1:", max(elf_calories))
print("Answer Level 2:", sum(sorted(elf_calories, reverse=True)[:3]))
