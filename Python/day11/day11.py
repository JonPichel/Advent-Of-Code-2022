from dataclasses import dataclass
from typing import Callable


@dataclass
class Monkey:
    items: [int]
    operation: Callable[[int], int]
    condition: (int, int, int)
    activity: int = 0

    def copy(self):
        return Monkey(self.items.copy(), self.operation, self.condition)


def print_monkeys(monkeys):
    for i, m in enumerate(monkeys):
        print(f"Monkey {i}: {m.items}")


with open("input", "r") as file:
    monkeys: [Monkey] = []
    while file.readline():
        items = [int(x.strip()) for x in file.readline().split(':')[1].split(',')]
        string = file.readline().split('=')[1].strip()
        match string[4]:
            case '*':
                b = string.split()[-1]
                if b != "old":
                    operation = lambda x, n=int(b): x * n
                else:
                    operation = lambda x: x * x
            case '+':
                b = string.split()[-1]
                if b != "old":
                    operation = lambda x, n=int(b): x + n
                else:
                    operation = lambda x: x + x
            case _:
                raise ValueError
        condition = []
        for _ in range(3):
            condition.append(int(file.readline().split()[-1]))
        monkeys.append(Monkey(items, operation, tuple(condition)))
        file.readline()

backup = []
for m in monkeys:
    backup.append(m.copy())

for _ in range(20):
    for i in range(len(monkeys)):
        m = monkeys[i]
        while m.items:
            m.activity += 1
            item = m.items.pop()
            item = m.operation(item) // 3
            if item % m.condition[0] == 0:
                monkeys[m.condition[1]].items.append(item)
            else:
                monkeys[m.condition[2]].items.append(item)

most_active = sorted([m.activity for m in monkeys], reverse=True)
print("Answer Level 1:", most_active[0] * most_active[1])

monkeys = backup
modulo = 1
for m in monkeys:
    modulo *= m.condition[0]

for _ in range(10_000):
    for i in range(len(monkeys)):
        m = monkeys[i]
        while m.items:
            m.activity += 1
            item = m.items.pop()
            item = m.operation(item) % modulo
            if item % m.condition[0] == 0:
                monkeys[m.condition[1]].items.append(item)
            else:
                monkeys[m.condition[2]].items.append(item)

most_active = sorted([m.activity for m in monkeys], reverse=True)
print("Answer Level 2:", most_active[0] * most_active[1])
