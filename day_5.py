def f1(a):
    return [a[i] if a[i] != " " else None for i in range(1, len(a), 4)]


def f2(a):
    a = list(a)
    return int(''.join(a[:-2])), int(a[-2]), int(a[-1])


def first(f, part_two=False):
    lines = f.readlines()
    crates = [f1(a[:-1]) for a in lines[:8]]
    stacks = [[] for _ in range(10)]
    for i, crate in enumerate(crates):
        for j, element in enumerate(crate):
            if element is not None:
                stacks[j].append(element)
    stacks = list(map(lambda x: list(reversed(x)), stacks))
    moves = [f2(filter(lambda a: a.isdigit(), b)) for b in lines[10:]]
    for move in moves:
        count, _from, to = move
        if part_two:
            stacks[to - 1] += stacks[_from - 1][-count:]
            stacks[_from - 1] = stacks[_from - 1][:-count]
        else:
            for _ in range(count):
                stacks[to - 1].append(stacks[_from - 1].pop())
    result = ""
    for stack in stacks:
        if len(stack):
            result += stack.pop()
    return result


def second(f):
    lines = f.readlines()
    print([[line[i] if line[i] != " " else None for i in range(1, len(line), 4)] for line in lines[:8]])
    stacks = [list(filter(lambda b: b != None, a)) for a in list(
        zip(*[[line[i] if line[i] != " " else None for i in range(1, len(line), 4)] for line in lines[:8]][::-1]))]
    moves = [line.replace("move", "").replace("from", "").replace("to", "").strip().split() for line in lines[10:]]
    print(stacks)
    [
        [stacks[int(to) - 1].append(stacks[int(_from) - 1].pop()) for _ in range(int(count))]
        for count, _from, to in moves
    ]
    return ''.join([stack[-1] if len(stack) else '' for stack in stacks])


def main():
    with open("res/input_5") as f:
        r1 = first(f)
    with open("res/input_5") as f:
        r = second(f)
        # r = first(f, True)
        # print(r)


if __name__ == '__main__':
    main()
