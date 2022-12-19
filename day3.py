from util import equal


def part_1(lines):
    return sum(
        map(
            lambda x: ord(x) - 96 if x.islower() else ord(x) - 38,
            map(
                lambda y: (s := len(y) // 2, (set(y[:s]) & set(y[s:])).pop())[-1],
                lines
            )
        )
    )


def part_2(lines):
    return sum(
        map(
            lambda x: ord(x) - 96 if x.islower() else ord(x) - 38,
            map(
                lambda y: (y[0] & y[1] & y[2]).pop(),
                (
                    [tuple(map(lambda z: set(z[:-1]), (lines[i], lines[i + 1], lines[i + 2])))
                     for i in range(0, len(lines), 3)]
                )
            )
        )
    )


if __name__ == '__main__':
    with open("res/3_0.txt") as f:
        example_input = f.readlines()
    with open("res/3_1.txt") as f:
        real_input = f.readlines()
    equal(part_1(example_input), 157)
    equal(part_2(example_input), 70)
    print(f"1st part answer is: {part_1(real_input)}")
    print(f"2nd part answer is: {part_2(real_input)}")
