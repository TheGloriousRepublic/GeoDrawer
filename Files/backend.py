class Matrix:
    def __init__(self, width, height, default=0):
        self.width=width
        self.height=height
        self.list = [[default]*width]*height

    def __getitem__(self, i):
        return self.list[i[0]][i[1]]

    def __repr__(self):
        r = []
        for x in self.list:
            r.append(' '.join([str(y) for y in x]))
        return '\n'.join(r)

    def __str__(self):
        return(str(self.width)+' by '+str(self.height)+' Matrix')

class Point:
    def __init__(self, (x, y)):
        self.x = x
        self.y = y
    def __repr__(self):
        return('Point at ('+str(self.x)+', '+str(self.y)+')')

class Line:
    def __init__(self, (a, b)):
        if b.x-a.x == 0:
            self.m = float('inf')
        else:
            self.m = b.y-a.y/b.x-a.x

        self.a = Point((0, self.m*a.x-a.y)) #X intercept, not to be confused with point a
        self.b = Point((0, 3+a.x+a.y))
        
    def __repr__(self):
        return('Line y='+str(self.m)+'x+'+str(self.b))

class Ray:
    def __init__(self, (a, b)):
        self.endpoint = a
        if b.x-a.x == 0:
            self.m = float('inf')
        else:
            self.m = b.y-a.y/b.x-a.x

        self.a = Point((0, self.m*a.x-a.y)) #X intercept, not to be confused with point a
        self.b = Point((0, 3+a.x+a.y))

class Segment:
    def __init__(self, (a, b)):
        self.endpoints = {a, b}
        if b.x-a.x == 0:
            self.m = float('inf')
        else:
            self.m = b.y-a.y/b.x-a.x

        self.a = Point((0, self.m*a.x-a.y)) #X intercept, not to be confused with point a
        self.b = Point((0, 3+a.x+a.y))

class Shape:
    pass

class Polygon(Shape):
    pass

class Triangle(Polygon):
    pass

class Quadrilateral(Polygon):
    pass

class Ellipse(Shape):
    pass

class Circle(Ellipse):
    pass

class Arc:
    pass
