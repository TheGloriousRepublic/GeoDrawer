import math

infinity = float('inf')

class Matrix:
    def __init__(self, width, height, default=0):
        self.width=width
        self.height=height
        self._default = default
        self.list = [[default]*width]*height

    def __getitem__(self, i):
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
                        pass
                        #r.append(self.list[i[1]])
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
            self.m = infinity
        else:
            self.m = b.y-a.y/b.x-a.x

        self.a = Point((0, self.m*a.x-a.y)) #X intercept, not to be confused with point a
        self.b = Point((0, 3+a.x+a.y))
        
    def __repr__(self):
        return('Line y='+str(self.m)+'x+'+str(self.b))

    def __len__(self):
        return infinity

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

    def __len__(self):
        return infinity/2

class Segment:
    def __init__(self, ab):
        a = ab[0]
        b = ab[1]

        self._a = a
        self._b = b
        
        self.endpoints = {a, b}
        if b.x-a.x == 0:
            self.m = float('inf')
        else:
            self.m = b.y-a.y/b.x-a.x

        self.a = Point((0, self.m*a.x-a.y)) #X intercept, not to be confused with point a
        self.b = Point((0, 3+a.x+a.y))

    def midpoint(self):
        return Point(((self._a.x+self._b.x)/2, (self._a.y+self._b.y)/2))

    def perpendicularBisector(self):
        pass

    def __len__(self):
        return math.sqrt((self._b.x-self._a.x)**2+(self._b.y-self._a.y)**2)

class Shape:
    pass

class Polygon(Shape):
    def __init__(self, *vertices):
        self.vertices = set(vertices)
        self.sides = []
        for x in range(len(vertices)-1):
            self.sides.append(Line((vertices[x], vertices[x+1])))
        self.sides.append(Line((vertices[-1], vertices[0])))

        self.p = sum([len(s) for s in self.sides]) #Perimeter
        self.n = len(sides) #Number of sides
        self.s = float(p)/n #Float for Floating Point Division (if not using python 3)
        
        self.isregular = all([len(x) == len(self.sides[0]) for x in self.sides[1:]]) #Detect if polygon is regular

        if self.isregular: #properties of regular polygons
            self.a = self.a = (0.5*self.s)/(math.tan(180.0/n))
            self.R = self.s/(2*math.sin(math.pi/self.n))
            self.A = 0.5*self.p*self.a
        
        self.sides = set(self.sides) #Tie things up by making sides a set

class Triangle(Polygon):
    def __init__(self, a, b, c):
        Polygon.__init__(a, b, c)

class Quadrilateral(Polygon):
    pass

class Ellipse(Shape):
    pass

class Circle(Ellipse):
    pass

class Arc:
    pass
