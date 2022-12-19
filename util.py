import dataclasses


def equal(got, expected):
    assert expected == got, f"expected {expected}, got {got}"


@dataclasses.dataclass(eq=True, frozen=True)
class Vec2:
    x: int
    y: int

    def normalize(self):
        x = self.x if abs(self.x) <= 1 else self.x / abs(self.x)
        y = self.y if abs(self.y) <= 1 else self.y / abs(self.y)
        return Vec2(x, y)

    def __mul__(self, other: int):
        return Vec2(self.x * other, self.y * other)

    def __add__(self, other: 'Vec2'):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vec2'):
        return Vec2(self.x - other.x, self.y - other.y)
