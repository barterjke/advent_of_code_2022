from util import equal


def part_1(lines: list[str]) -> int:
    return (
        l := lambda a, b: int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1]),
        len(
            list(
                filter(
                    lambda c: l(c[0], c[1]) or l(c[1], c[0]),
                    [[b.split("-") for b in a.strip().split(",")] for a in lines]
                )
            )
        )
    )[-1]


def part_2(lines: list[str]) -> int:
    return (
        l := lambda a, b: int(a[1]) < int(b[0]) or int(b[1]) < int(a[0]),
        len(
            list(
                filter(
                    lambda c: not l(c[0], c[1]),
                    [[b.split("-") for b in a.strip().split(",")] for a in lines]
                )
            )
        )
    )[-1]


if __name__ == '__main__':
    with open("res/4_0.txt") as f:
        example_input = f.readlines()
    with open("res/4_1.txt") as f:
        real_input = f.readlines()
    equal(part_1(example_input), 2)
    equal(part_2(example_input), 4)
    print(f"1st part answer is: {part_1(real_input)}")
    print(f"2nd part answer is: {part_2(real_input)}")
