class Point:
    # this is the constructor, it will be called when we create a new point object or instance of this class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # def draw(self):
    #     print(f"Point ({self.x}, {self.y})")


point = Point(10, 20)
other = Point(1, 2)
print(point < other)
