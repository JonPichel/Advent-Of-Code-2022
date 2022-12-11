with open("input", "r") as file:
    lines = file.readlines()


class CPU:
    def __init__(self):
        self.counter = 0
        self.X = 1
        self.power = 0

    def tick(self):
        # Power logic (part 1)
        self.counter += 1
        if self.counter == 20 or (self.counter - 20) % 40 == 0:
            self.power += self.X * self.counter

    def draw(self):
        col = (self.counter - 1) % 40
        # Drawing logic (part 2)
        if self.X - 1 <= col <= self.X + 1:
            print('#', end="")
        else:
            print('.', end="")
        if col == 39:
            print()


cpu = CPU()
print("Screen for Level 2:")
for instruction in lines:
    words = instruction.split()

    match words[0]:
        case "addx":
            for _ in range(2):
                cpu.tick()
                cpu.draw()
            cpu.X += int(words[1])
        case "noop":
            cpu.tick()
            cpu.draw()
        case _:
            raise ValueError

print("\nAnswer Level 1:", cpu.power)