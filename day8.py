from dataclasses import dataclass
import numpy as np


@dataclass
class Pack:
    x: int
    visible = False
    score = 1

    def __init__(self, x):
        self.x = int(x)


def check_visibility(lines):
    for line in lines:
        most = -1
        for j in line:
            j.visible = j.x > most or j.visible
            most = max(j.x, most)


def find(matrix: list[list[Pack]]):
    matrix = np.array(matrix)
    check_visibility(matrix) and check_visibility(np.flip(matrix, 1)) and check_visibility(
        matrix.transpose()) and check_visibility(np.flip(matrix.transpose(), 1))
    return sum([sum([x.visible for x in line]) for line in matrix])


def scenic_score(el: Pack, line: list[Pack]) -> int:
    score = 0
    for item in line:
        score += 1
        if el.x <= item.x:
            return score
    return score


def find_best_scenic_score(matrix: list[list[Pack]]):
    matrix = np.array(matrix)
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            left, right, up, down = list(reversed(matrix[i, :j])), matrix[i, j + 1:], list(
                reversed(matrix[:i, j])), matrix[i + 1:, j]
            el.score = scenic_score(el, left) * scenic_score(el, right) * scenic_score(el, up) * scenic_score(el, down)
    return max([max([x.score for x in line]) for line in matrix])


def main():
    with open("res/input_8") as f:
        matrix = [[Pack(y) for y in x] for x in f.read().split("\n")]
        print(find(matrix), find_best_scenic_score(matrix))  # 1798 259308


if __name__ == '__main__':
    main()
