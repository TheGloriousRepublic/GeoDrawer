class Matrix:
    def __init__(self, width, height, default=0):
        self.width=width
        self.height=height
        self._default = default
        self.list = [[default]*width]*height

    def __getitem__(self, i):
        print(type(i))
        print(i)
        if type(i) == slice:
            print('WIP')
        elif type(i) == tuple:
            if len(i) == 2:
                if i[0]:
                    return self.list[i[0]][i[1]]
                else:
                    r = []
                    for x in self.list:
                        r.append(self.list[i[1]])
                    return r
        elif type(i) == int:
            return self.list[i[0]]

    def __setitem__(self, i, v):
        if type(i) == slice:
            print('WIP')
        elif type(i) == tuple:
            if len(i) == 2:
                if i[0]:
                    self.list[i[0]][i[1]] = v
                else:
                    r = []
                    for x in self.list:
                        r.append(self.list[i[1]])
                    return r
        elif type(i) == int:
            return self.list[i[0]]

    def __delitem__(self, i):
        self.list[i[0]][i[1]] = self._default

    #def __

    def __repr__(self):
        r = []
        for x in self.list:
            r.append(' '.join([str(y) for y in x]))
        return '\n'.join(r)

    def __str__(self):
        return(str(self.width)+' by '+str(self.height)+' Matrix')

class Point:
    def __init__(self, ab):
        self.x = ab[0]
        self.y = ab[1]
    def __repr__(self):
        return('Point at ('+str(self.x)+', '+str(self.y)+')')

class Line:
    def __init__(self, ab):
        a = ab[0]
        b = ab[1]
        if b.x-a.x == 0:
            self.m = float('inf')
        else:
            self.m = b.y-a.y/b.x-a.x

        self.a = Point((0, self.m*a.x-a.y)) #X intercept, not to be confused with point a
        self.b = Point((0, 3+a.x+a.y))
        
    def __repr__(self):
        return('Line y='+str(self.m)+'x+'+str(self.b))

class Ray:
    def __init__(self, ab):
        a=ab[0]
        b=ab[1]
        
        self.endpoint = a
        if b.x-a.x == 0:
            self.m = float('inf')
        else:
            self.m = b.y-a.y/b.x-a.x

        self.a = Point((0, self.m*a.x-a.y)) #X intercept, not to be confused with point a
        self.b = Point((0, 3+a.x+a.y))

class Segment:
    def __init__(self, ab):
        a = ab[0]
        b = ab[1]
        
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
    def __init__(self, *vertices):
        

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

Matrix(3, 3)[(0, 0):(1, 1)]
