import numpy as np

from util import equal


def parse_input_to_stack(lines: list[str], is_example):
    return [list(filter(lambda b: b is not None, a)) for a in list(
        np.array(
            [np.array([line[i] if i < len(line) and line[i] != " " else None for i in
                       range(1, 4 * (3 if is_example else 9), 4)]) for line in
             lines[:3 if is_example else 8]][::-1]).transpose())]


def part_1(lines: list[str], is_example=False) -> str:
    stacks = parse_input_to_stack(lines, is_example)
    [
        [stacks[int(to) - 1].append(stacks[int(_from) - 1].pop()) for _ in range(int(count))]
        for count, _from, to in
        [
            line.replace("move", "").replace("from", "").replace("to", "").strip().split()
            for line in lines[5 if is_example else 10:]
        ]
    ]
    return ''.join([stack[-1] if len(stack) else '' for stack in stacks])


def part_2(lines: list[str], is_example=False) -> str:
    stacks = parse_input_to_stack(lines, is_example)
    for count, _from, to in [line.replace("move", "").replace("from", "").replace("to", "").strip().split() for line in
                             lines[5 if is_example else 10:]]:
        count, _from, to = int(count), int(_from), int(to)
        stacks[to - 1] += stacks[_from - 1][-count:]
        stacks[_from - 1] = stacks[_from - 1][:-count]
    return ''.join([stack[-1] if len(stack) else '' for stack in stacks])


if __name__ == '__main__':
    with open("res/5_0.txt") as f:
        example_input = f.readlines()
    with open("res/5_1.txt") as f:
        real_input = f.readlines()
    equal(part_1(example_input, is_example=True), 'CMZ')
    equal(part_2(example_input, is_example=True), 'MCD')
    print(f"1st part answer is: {part_1(real_input)}")
    print(f"2nd part answer is: {part_2(real_input)}")

# %%

# %%
