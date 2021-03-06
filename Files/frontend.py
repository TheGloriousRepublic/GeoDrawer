try:
    from Files.interfaces import *
    from Files.backend import *
except ImportError:
    from interfaces import *
    from backend import *

class DrawWidget(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.protocol('WM_DELETE_WINDOW', self.Close)
        
        self.c = tk.Canvas(self, bg='white')
        self.c.pack(fill=tk.BOTH, expand=1)

        self.objects = {}

        self.objects['O'] = {'main':Point((0, 0)), 'color':'black'}
        self.Draw()
        
        self.setupMenubar()

    def setupMenubar(self):
        #Here starts the menubar. It is a massive tangle of commands with almost no
        #Logical ordering. Don't try to read it.
        self.menubar = tk.Menu(self)

        self.filemenu = tk.Menu(self.menubar, tearoff=False)
        self.filemenu.add_command(label='Save')
        self.filemenu.add_command(label='Save As')
        self.filemenu.add_command(label='Export Image', command=self.noimage)
        self.filemenu.add_command(label='Open')
        self.filemenu.add_command(label='Print')
        self.filemenu.add_command(label='Exit')
        self.menubar.add_cascade(label='File', menu=self.filemenu)

        self.generalmenu = tk.Menu(self.menubar, tearoff=False)
        self.generalmenu.add_command(label='Delete Object')
        self.calcmenu = tk.Menu(self.generalmenu, taroff=False)
        self.calcmenu.add_command(label='Standard', command=self.stacalc)
        self.calcmenu.add_command(label='Scientific', command=self.scicalc)
        self.calcmenu.add_command(label='Programmer', command=self.progcalc)
        self.calcmenu.add_command(label='Statistics', command=self.statcalc)
        self.generalmenu.add_cascade(label='Calculator', menu=self.calcmenu)
        self.menubar.add_cascade(label='General', menu=self.generalmenu)

        self.funcmenu = tk.Menu(self.menubar, tearoff=False)
        self.funcmenu.add_command(label='Graph Function')
        self.menubar.add_cascade(label='Functions', menu=self.funcmenu)
        
        self.pointmenu = tk.Menu(self.menubar, tearoff=False)
        self.pointmenu.add_command(label='Add or Set Point', command=self.newpoint)

        self.pointscan = tk.Menu(self.pointmenu, tearoff=False)
        self.pointmenu.add_cascade(label='Scan Point', menu=self.pointscan)
        self.menubar.add_cascade(label='Points', menu=self.pointmenu)
        
        self.linetypemenu = tk.Menu(self.menubar, tearoff=False)

        self.linemenu = tk.Menu(self.linetypemenu, tearoff=False)
        self.linemenu.add_command(label='Add or Set Line', command=self.newline)
        self.lineattributes = tk.Menu(self.linemenu, tearoff=False)
        self.linemenu.add_cascade(label='Line Attributes', menu=self.lineattributes)
        self.linescan = tk.Menu(self.linemenu, tearoff=False)
        self.linemenu.add_cascade(label='Scan Line', menu=self.linescan)
        self.linetypemenu.add_cascade(label='Lines', menu=self.linemenu)

        self.raymenu = tk.Menu(self.linetypemenu, tearoff=False)
        self.raymenu.add_command(label='Add or Set Ray')
        self.rayattributes = tk.Menu(self.linemenu, tearoff=False)
        self.raymenu.add_cascade(label='Ray Attributes', menu=self.rayattributes)
        self.rayscan = tk.Menu(self.raymenu, tearoff=False)
        self.raymenu.add_cascade(label='Scan Ray', menu=self.rayscan)
        self.linetypemenu.add_cascade(label='Rays', menu=self.raymenu)

        self.segmenu = tk.Menu(self.linetypemenu, tearoff=False)
        self.segmenu.add_command(label='Add or Set Line Segment')
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
        self.ellipsemenu.add_command(label='Add or Set Ellipse')
        self.ellipseattributes = tk.Menu(self.ellipsemenu, tearoff=False)
        self.ellipsemenu.add_cascade(label='Ellipse Attributes', menu=self.ellipseattributes)
        self.ellipsescan = tk.Menu(self.ellipsemenu, tearoff=False)
        self.ellipsemenu.add_cascade(label='Scan Ellipse', menu=self.ellipsescan)

        self.circlemenu = tk.Menu(self.ellipsemenu, tearoff=False)
        self.circlemenu.add_command(label='Add or Set Circle')
        self.circleattributes = tk.Menu(self.circlemenu, tearoff=False)
        self.circlemenu.add_cascade(label='Circle Attributes', menu=self.circleattributes)
        self.circlescan = tk.Menu(self.circlemenu, tearoff=False)
        self.circlemenu.add_cascade(label='Scan Circle', menu=self.circlescan)
        
        self.trianglemenu = tk.Menu(self.polymenu, tearoff=False)
        
        self.trianglemenu.add_command(label='Add or Set Triangle')

        self.triangleattributes = tk.Menu(self.trianglemenu, tearoff=False)
        self.trianglemenu.add_cascade(label='Triangle Attributes', menu=self.triangleattributes)
        self.trianglescan = tk.Menu(self.trianglemenu, tearoff=False)
        self.trianglemenu.add_cascade(label='Scan Triangle', menu=self.trianglescan)
        
        self.quadmenu = tk.Menu(self.polymenu, tearoff=False)
        self.quadmenu.add_command(label='Add or Set Quadrilateral')        
        self.quadattributes = tk.Menu(self.quadmenu, tearoff=False)
        self.quadmenu.add_cascade(label='Quadrilateral Attributes', menu=self.quadattributes)
        self.quadscan = tk.Menu(self.quadmenu, tearoff=False)
        self.quadmenu.add_cascade(label='Scan Quadrilateral', menu=self.quadscan)
        
        self.moremenu = tk.Menu(self.polymenu, tearoff=False)
        self.moremenu.add_command(label='Add or Set Other Polygon')
        
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

        self.matrixmenu = tk.Menu(self.menubar, tearoff=False)
        self.matrixmenu.add_command(label='Convert Shape To Matrix')
        self.matrixmenu.add_command(label='Operate on Matrices')
        self.matrixmenu.add_command(label='Operate Matrix by Scalar')
        self.matrixmenu.add_command(label='Transpose Matrix')
        self.menubar.add_cascade(label='Matrices', menu=self.matrixmenu)

        self.config(menu=self.menubar)

    def newpoint(self):
        print('Creating Point')
        cpw = CreatePointWindow()
        cpw.mainloop()
        point = cpw.r
        if None not in point:
            self.objects[point[0]] = {'main':point[1]}
            
        self.Draw()

    def newline(self):
        print('Creating Line')
        clw = CreateLineWindow()
        clw.mainloop()
        line = cpw.r
        if None not in point:
            self.objects[point[0]] = {'main':line[1]}
            
        self.Draw()

    def stacalc(self):
        clcw = StandardCalculatorWindow()
        clcw.mainloop()

    def scicalc(self):
        clcw = ScientificCalculatorWindow()
        clcw.mainloop()

    def progcalc(self):
        clcw = ProgrammerCalculatorWindow()
        clcw.mainloop()

    def statcalc(self):
        clcw = StatisticsCalculatorWindow()
        clcw.mainloop()
        
    def noimage(self):
        if pyver == 2:
            import tkMessageBox
            tkMessageBox.showwarning('No Image Export', 'Image exporting not available! Use screenshots for now!')
        elif pyver == 3:
            from Tkinter import messagebox
            messagebox.showwarning('No Image Export', 'Image exporting not available! Use screenshots for now!')


    def Draw(self):
        print('Redrawing...')
        self.c.delete('all')
        print('Cleared Canvas')
        for x in self.objects:
            ob = self.objects[x]
            main = ob['main']
            print('Drawing '+str(x))
            if isinstance(main, Point):
                if not ob.get('color'): #Set color to red if there isn't one
                    ob['color'] = '#ff0000'
                self.c.create_oval(main.x+298, 300-main.y-2, main.x+302, 300-main.y+2, fill=ob['color'], outline=ob['color'])
            elif isinstance(main, Line):
                pass
            elif isinstance(main, Ray):
                pass
            elif isinstance(main, Segment):
                pass
                 
    def Close(self, event=None):
        self.quit()
        
    def quit(self):
        self.destroy()
