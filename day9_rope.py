import dataclasses
import numpy as np
import matplotlib.pyplot as plt

from util import Vec2


def first(content: str) -> int:
    moves = [line.split() for line in content.split("\n")]
    head = Vec2(0, 0)
    tail = Vec2(0, 0)
    grid = {Vec2(0, 0)}
    direction_to_move = {'R': Vec2(1, 0), 'L': Vec2(-1, 0), 'D': Vec2(0, -1), 'U': Vec2(0, 1)}
    for direction, value in moves:
        for _ in range(int(value)):
            head += direction_to_move[direction]
            dif = head - tail
            if abs(dif.x) > 1 or abs(dif.y) > 1:
                tail += dif.normalize()
            grid.add(tail)
    return len(grid)


def draw_grid(grid):
    matrix = np.array([np.array([0 for _ in range(30)]) for _ in range(30)])
    print(Vec2(0, 0) in grid)
    print(min([x.x for x in grid]))
    print(min([x.y for x in grid]))
    for it in grid:
        matrix[int(it.y + 5), int(it.x + 11)] = 1
    plt.imshow(matrix, interpolation='none')
    plt.show()


def second(content: str) -> int:
    moves = [line.split() for line in content.split("\n")]
    head = Vec2(0, 0)
    rest = [Vec2(0, 0) for _ in range(9)]
    grid = {Vec2(0, 0)}
    direction_to_move = {'R': Vec2(1, 0), 'L': Vec2(-1, 0), 'D': Vec2(0, -1), 'U': Vec2(0, 1)}
    for direction, value in moves:
        for _ in range(int(value)):
            head += direction_to_move[direction]
            for i, tail in enumerate(rest):
                local_head = rest[i - 1] if i != 0 else head
                dif = local_head - tail
                if abs(dif.x) > 1 or abs(dif.y) > 1:
                    rest[i] += dif.normalize()
                if i == 8:
                    grid.add(rest[i])
    draw_grid(grid)
    return len(grid)


def main():
    with open("res/input_9") as f:
        print(first(content := f.read()), second(content))


if __name__ == '__main__':
    main()
