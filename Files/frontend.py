from interfaces import *
    
from backend import *

class DrawWidget(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.c = tk.Canvas()

        self.objects = {}

        #Here starts the menubar. It is a massive tangle of commands with almost no
        #Logical ordering. Don't try to read it.
        self.menubar = tk.Menu(self)

        self.filemenu = tk.Menu(self.menubar, tearoff=False)
        self.filemenu.add_command(label='Save')
        self.filemenu.add_command(label='Save As')
        self.filemenu.add_command(label='Open')
        self.filemenu.add_command(label='Print')
        self.filemenu.add_command(label='Exit')
        self.menubar.add_cascade(label='File', menu=self.filemenu)

        self.generalmenu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label='General', menu=self.generalmenu)
        
        self.pointmenu = tk.Menu(self.menubar, tearoff=False)
        self.pointmenu.add_command(label='Add Point', command=self.newpoint)
        self.pointmenu.add_command(label='Delete Point')
        self.pointmenu.add_command(label='Change Point')

        self.pointscan = tk.Menu(self.pointmenu, tearoff=False)
        self.pointmenu.add_cascade(label='Scan Point', menu=self.pointscan)
        self.menubar.add_cascade(label='Points', menu=self.pointmenu)
        
        self.linetypemenu = tk.Menu(self.menubar, tearoff=False)

        self.linemenu = tk.Menu(self.linetypemenu, tearoff=False)
        self.linemenu.add_command(label='Draw Line')
        self.linemenu.add_command(label='Delete Line')
        self.linemenu.add_command(label='Change Line')
        self.lineattributes = tk.Menu(self.linemenu, tearoff=False)
        self.linemenu.add_cascade(label='Line Attributes', menu=self.lineattributes)
        self.linescan = tk.Menu(self.linemenu, tearoff=False)
        self.linemenu.add_cascade(label='Scan Line', menu=self.linescan)
        self.linetypemenu.add_cascade(label='Lines', menu=self.linemenu)

        self.raymenu = tk.Menu(self.linetypemenu, tearoff=False)
        self.raymenu.add_command(label='Draw Ray')
        self.raymenu.add_command(label='Delete Ray')
        self.raymenu.add_command(label='Change Ray')
        self.rayattributes = tk.Menu(self.linemenu, tearoff=False)
        self.raymenu.add_cascade(label='Ray Attributes', menu=self.rayattributes)
        self.rayscan = tk.Menu(self.raymenu, tearoff=False)
        self.raymenu.add_cascade(label='Scan Ray', menu=self.rayscan)
        self.linetypemenu.add_cascade(label='Rays', menu=self.raymenu)

        self.segmenu = tk.Menu(self.linetypemenu, tearoff=False)
        self.segmenu.add_command(label='Draw Line Segment')
        self.segmenu.add_command(label='Delete Line Segment')
        self.segmenu.add_command(label='Change Line Segment')
        self.segattributes = tk.Menu(self.linemenu, tearoff=False)
        self.segmenu.add_cascade(label='Segment Attributes', menu=self.segattributes)
        self.segscan = tk.Menu(self.segmenu, tearoff=False)
        self.segmenu.add_cascade(label='Scan Segment', menu=self.segscan)
        self.linetypemenu.add_cascade(label='Line Segments', menu=self.segmenu)
        
        self.menubar.add_cascade(label='Lines', menu=self.linetypemenu)

        self.shapemenu = tk.Menu(self.menubar, tearoff=False)
        self.polymenu = tk.Menu(self.shapemenu, tearoff=False)

        self.nonpolymenu = tk.Menu(self.shapemenu, tearoff=False)

        self.ellipsemenu = tk.Menu(self.nonpolymenu, tearoff=False)
        self.ellipsemenu.add_command(label='Draw Ellipse')
        self.ellipsemenu.add_command(label='Change Ellipse')
        self.ellipseattributes = tk.Menu(self.ellipsemenu, tearoff=False)
        self.ellipsemenu.add_cascade(label='Ellipse Attributes', menu=self.ellipseattributes)
        self.ellipsescan = tk.Menu(self.ellipsemenu, tearoff=False)
        self.ellipsemenu.add_cascade(label='Scan Ellipse', menu=self.ellipsescan)

        self.circlemenu = tk.Menu(self.ellipsemenu, tearoff=False)
        self.circlemenu.add_command(label='Draw Circle')
        self.circlemenu.add_command(label='Change Circle')
        self.circleattributes = tk.Menu(self.circlemenu, tearoff=False)
        self.circlemenu.add_cascade(label='Circle Attributes', menu=self.circleattributes)
        self.circlescan = tk.Menu(self.circlemenu, tearoff=False)
        self.circlemenu.add_cascade(label='Scan Circle', menu=self.circlescan)
        
        self.trianglemenu = tk.Menu(self.polymenu, tearoff=False)
        
        self.trianglemenu.add_command(label='Draw Triangle')
        self.trianglemenu.add_command(label='Change Triangle')

        self.triangleattributes = tk.Menu(self.trianglemenu, tearoff=False)
        self.trianglemenu.add_cascade(label='Triangle Attributes', menu=self.triangleattributes)
        self.trianglescan = tk.Menu(self.trianglemenu, tearoff=False)
        self.trianglemenu.add_cascade(label='Scan Triangle', menu=self.trianglescan)
        
        self.quadmenu = tk.Menu(self.polymenu, tearoff=False)
        self.quadmenu.add_command(label='Draw Quadrilateral')
        self.quadmenu.add_command(label='Change Quadrilateral')
        
        self.quadattributes = tk.Menu(self.quadmenu, tearoff=False)
        self.quadmenu.add_cascade(label='Quadrilateral Attributes', menu=self.quadattributes)
        self.quadscan = tk.Menu(self.quadmenu, tearoff=False)
        self.quadmenu.add_cascade(label='Scan Quadrilateral', menu=self.quadscan)
        
        self.moremenu = tk.Menu(self.polymenu, tearoff=False)
        self.moremenu.add_command(label='Draw Other Polygon')
        self.moremenu.add_command(label='Change Polygon')
        
        self.moreattributes = tk.Menu(self.moremenu, tearoff=False)
        self.moremenu.add_cascade(label='Polygon Attributes', menu=self.moreattributes)
        self.morescan = tk.Menu(self.moremenu, tearoff=False)
        self.moremenu.add_cascade(label='Scan Polygon', menu=self.morescan)
        
        self.menubar.add_cascade(label='Shapes', menu=self.shapemenu)
        self.shapemenu.add_cascade(label='Polygons', menu=self.polymenu)
        self.polymenu.add_cascade(label='Triangles', menu=self.trianglemenu)
        self.polymenu.add_cascade(label='Quadrilaterals', menu=self.quadmenu)
        self.polymenu.add_cascade(label='Other Polygons', menu=self.moremenu)

        self.shapemenu.add_cascade(label='Non-Polygons', menu=self.nonpolymenu)
        self.nonpolymenu.add_cascade(label='Ellipses', menu=self.ellipsemenu)
        self.ellipsemenu.add_cascade(label='Circles', menu=self.circlemenu)

        self.shapemenu.add_command(label='Delete Shape')

        self.matrixmenu = tk.Menu(self.menubar, tearoff=False)
        self.matrixmenu.add_command(label='Convert Shape To Matrix')
        self.matrixmenu.add_command(label='Add Matrices')
        self.matrixmenu.add_command(label='Multiply Matrix by Scalar')
        self.matrixmenu.add_command(label='Transpose Matrix')
        self.matrixmenu.add_command(label='Multiply Matrices')
        self.menubar.add_cascade(label='Matrices', menu=self.matrixmenu)

        self.config(menu=self.menubar)

    def newpoint(self):
        cpw = CreatePointWindow()
        cpw.mainloop()
        point = cpw.r
        if point[1] != (None, None):
            self.objects[point[0]] = Point(point[1])

        print objects

    def quit(self):
        self.destroy()
