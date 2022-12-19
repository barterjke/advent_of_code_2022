

def day_3_1(f):
    return sum(
        map(
            lambda x: ord(x) - 96 if x.islower() else ord(x) - 38,
            map(
                lambda y: (s := len(y) // 2, (set(y[:s]) & set(y[s:])).pop())[-1],
                f.readlines()
            )
        )
    )


def day_3_2(f):
    return sum(
        map(
            lambda x: ord(x) - 96 if x.islower() else ord(x) - 38,
            map(
                lambda y: (y[0] & y[1] & y[2]).pop(),
                (
                    lines := f.readlines(),
                    [tuple(map(lambda z: set(z[:-1]), (lines[i], lines[i + 1], lines[i + 2])))
                     for i in range(0, len(lines), 3)]
                )[-1]
            )
        )
    )


def day_4_1(f):
    return (
        l := lambda a, b: int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1]),
        len(
            list(
                filter(
                    lambda c: l(c[0], c[1]) or l(c[1], c[0]),
                    [[b.split("-") for b in a.strip().split(",")] for a in f.readlines()]
                )
            )
        )
    )[-1]


def day_4_2(f):
    return (
        l := lambda a, b: int(a[1]) < int(b[0]) or int(b[1]) < int(a[0]),
        len(
            list(
                filter(
                    lambda c: not l(c[0], c[1]),
                    [[b.split("-") for b in a.strip().split(",")] for a in f.readlines()]
                )
            )
        )
    )[-1]

def main():
    with open("res/input_4") as f:
        r = day_4_2(f)
        print(r)


if __name__ == '__main__':
    main()
