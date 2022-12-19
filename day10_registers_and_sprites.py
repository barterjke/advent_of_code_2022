from itertools import chain


def first(content):
    x_reg = 1
    total = 0
    cycle = 0
    for line in content.split("\n"):
        if line == "noop":
            cycle += 1
            if cycle in (20, 60, 100, 140, 180, 220):
                total += cycle * x_reg
            continue
        val = int(line[len("addx "):])
        cycle += 1
        if cycle in (20, 60, 100, 140, 180, 220):
            total += cycle * x_reg
        cycle += 1
        if cycle in (20, 60, 100, 140, 180, 220):
            total += cycle * x_reg
        x_reg += val
    return total


def second(content: str):
    x_reg = 1
    total = 0
    cycle = 0
    cycle_for_command = 0
    cmd_stack = list(reversed(content.split("\n")))
    cmd = cmd_stack.pop()
    while len(cmd_stack):
        cycle += 1
        if cycle in (20, 60, 100, 140, 180, 220):
            total += cycle * x_reg
        if cmd == "noop":
            cmd = cmd_stack.pop()
            cycle_for_command = 0 if cmd == "noop" else 2
            continue
        else:
            val = int(cmd[len("addx "):])
            cycle_for_command -= 1
            if cycle_for_command == 0:
                cmd = cmd_stack.pop()
                cycle_for_command = 2
                x_reg += val
    return total


def third(content):
    x, cycle, total, cmds = 1, 0, 0, chain.from_iterable(
        map(lambda line: ["noop"] if line == "noop" else ["noop", "noop", line], content.split("\n")))
    for cmd in cmds:
        total += cycle * x if cycle in (20, 60, 100, 140, 180, 220) else 0
        if cmd == "noop":
            cycle += 1
        else:
            x += int(cmd[len("addx "):])
    return total


def CRT_drawer(content):
    x, cycle, cmds = 1, 1, chain.from_iterable(
        map(lambda line: ["noop"] if line == "noop" else ["noop", "noop", line], content.split("\n")))
    result = []
    s = ""
    # print('Sprite position:', "." * (x - 1) + 3 * "#" + (38 - x) * ".")
    for cmd in cmds:
        if cmd == "noop":
            s += "#" if cycle - 1 in (x, x - 1, x + 1) else " "
            # print("current CRT row:")
            cycle += 1
            if cycle == 41:
                cycle = 1
                result.append(s)
                s = ""
        else:
            x += int(cmd[len("addx "):])
            # print('Sprite position:', "." * (x - 1) + 3 * "#" + (38 - x) * ".")
    return "\n".join(result)


def main():
    with open("res/input_10") as f:
        print(third(content := f.read()), "\n", CRT_drawer(content))


if __name__ == '__main__':
    main()
