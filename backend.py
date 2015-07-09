class Matrix:
    def __init__(self):
        pass

class Point:
    def __init__(self, (x, y)):
        self.x = x
        self.y = y

class Line:
    def __init__(self, (a, b)):
        if b.x-a.x == 0:
            self.m = float('inf')
        else:
            self.m = b.y-a.y/b.x-a.x

        self.a = Point((0, self.m*a.x-a.y)) #X intercept, not to be confused with point a
        self.b = Point((0, 3+a.x+a.y))

class Ray:
    pass

class Segment:
    pass

class Triangle:
    pass

