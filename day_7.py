class Tree:
    def __init__(self, _type, name, parent=None, size=0):
        self.name = name
        self.type = _type
        self.size = size
        self.parent = parent
        self.dirs = {} if self.type == "dir" else None

    def add_dir(self, name):
        if name not in self.dirs:
            self.dirs[name] = Tree("dir", name, self)

    def add_file(self, name, size):
        if name not in self.dirs:
            self.dirs[name] = Tree("file", name, self, size)
        else:
            assert self.dirs[name].size == size

    def calc_size_of_dirs(self):
        total = 0
        for v in self.dirs.values():
            if v.type == "dir":
                total += v.calc_size_of_dirs()
            self.size += v.size
        return total + self.size if self.size < 100000 else total


def func(tree: Tree, lines: list[str], i: int):
    line = lines[i]
    if line.startswith("$"):
        cmd = lines[i][2:]
        if cmd == "ls":
            func(tree, lines, i + 1)
        else:  # cd
            cmd, _dir = cmd.split()
            assert cmd == "cd"
            if _dir == "..":
                func(tree.parent, lines, i + 1)
            else:
                func(tree.dirs[_dir], lines, i + 1)
    else:
        size_or_type, name = line.split()
        if size_or_type == "dir":
            # print(f"add dir {name}")
            tree.add_dir(name)
        else:
            # print(f"add file {name}")
            tree.add_file(name, int(size_or_type))
        func(tree, lines, i + 1)


# {"/": ("dir", {"a": , })}


# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)

# def func(content: str) -> None:
#     lines = content.split("\n")
#     i = 0
#     ctx = {}
#     while i < len(lines):
#         line = lines[i]
#         if line.startswith("$"):
#             process_cmd(ctx, lines, i)


def main():
    with open("res/input_7_example") as f:
        try:
            tree = Tree("dir", "/")
            func(tree, f.read().split("\n"), 1)
        except:
            pass
        print(tree.dirs)
        print(tree.calc_size_of_dirs()) # 1749606 to low


if __name__ == '__main__':
    main()
