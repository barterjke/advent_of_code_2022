import math
from dataclasses import dataclass
from functools import reduce


def perform_operation(value: int, operation: list[str]) -> int:
    if operation == ['old', '*', 'old']:
        return value * value
    _, sign, other_value = operation
    return value * int(other_value) if sign == "*" else value + int(other_value)


def func(content, number_of_rounds=20, stress_level=3):
    content = content.split("\n")
    i = 0
    monkeys = []
    while i < len(content):
        _, _, *items = content[i + 1].split()
        operation = content[i + 2].split()[3:]
        test = int(content[i + 3].split()[-1])
        if_true = int(content[i + 4].split()[-1])
        if_false = int(content[i + 5].split()[-1])
        i += 7
        monkeys.append(([int(x[:-1]) if x.endswith(",") else int(x) for x in items], operation, test,
                        if_true, if_false, 0))
    dividors_prod = math.prod(map(lambda x: x[2], monkeys))
    for i in range(number_of_rounds):
        for j, monkey in enumerate(monkeys):
            items, operation, test, if_true, if_false, inspected_items = monkey
            inspected_items += len(items)
            for item in items:
                item = perform_operation(item, operation) // stress_level
                if stress_level == 1:
                    item %= dividors_prod
                next_monkey = if_true if item % test == 0 else if_false
                monkeys[next_monkey][0].append(item)
            monkeys[j] = ([], operation, test, if_true, if_false, inspected_items)
        # for monkey in monkeys:
        #     print(monkey['items'])
        # print("...")
    return reduce(lambda x, y: x * y, sorted([x[-1] for x in monkeys])[-2:])

def main():
    with open("res/11") as f:
        print(func(f.read(), 10000, 1))


if __name__ == '__main__':
    main()
