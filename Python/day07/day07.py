from dataclasses import dataclass, field


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    path: str
    parent: str | None
    children: [str] = field(default_factory=list)
    files: [File] = field(default_factory=list)


with open("input", "r") as file:
    lines = file.readlines()

cwd = None
filesystem = {}
listing = False
for line in lines:
    words = line.split()

    if listing:
        match words[0]:
            case "$":
                listing = False
            case "dir":
                path = cwd + words[1] + "/"
                filesystem[cwd].children.append(path)
                filesystem[path] = Directory(path, cwd)
            case other:
                size = int(other)
                name = words[1]
                filesystem[cwd].files.append(File(name, size))

    if words[1] == "cd":
        match words[2]:
            case "/":
                filesystem["/"] = Directory("/", None)
                cwd = "/"
            case "..":
                cwd = filesystem[cwd].parent
            case other:
                cwd = filesystem[cwd + other + "/"].path
    elif words[1] == "ls":
        listing = True


def dir_size(path):
    directory = filesystem[path]
    total_size = sum([file.size for file in directory.files])
    for subdir in directory.children:
        total_size += dir_size(subdir)
    return total_size


print("Answer Level 1:", sum(x for x in (dir_size(dir) for dir in filesystem.keys()) if x < 100_000))


needed_space = 30_000_000 - (70_000_000 - dir_size("/"))

candidates = sorted(x for x in (dir_size(dir) for dir in filesystem.keys()) if x > needed_space)

print("Answer Level 2:", candidates[0])