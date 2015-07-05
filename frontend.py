try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
    
from backend import *

class DrawWidget(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.c = tk.Canvas()

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
        self.pointmenu.add_command(label='Add Point')
        self.pointmenu.add_command(label='Delete Point')
        self.pointmenu.add_command(label='Change Point')
        self.menubar.add_cascade(label='Points', menu=self.pointmenu)
        
        self.linetypemenu = tk.Menu(self.menubar, tearoff=False)

        self.linemenu = tk.Menu(self.linetypemenu, tearoff=False)
        self.linemenu.add_command(label='Draw Line')
        self.linemenu.add_command(label='Delete Line')
        self.linemenu.add_command(label='Change Line')
        self.linetypemenu.add_cascade(label='Lines', menu=self.linemenu)

        self.raymenu = tk.Menu(self.linetypemenu, tearoff=False)
        self.raymenu.add_command(label='Draw Ray')
        self.raymenu.add_command(label='Delete Ray')
        self.raymenu.add_command(label='Change Ray')
        self.linetypemenu.add_cascade(label='Rays', menu=self.raymenu)

        self.segmenu = tk.Menu(self.linetypemenu, tearoff=False)
        self.segmenu.add_command(label='Draw Line Segment')
        self.segmenu.add_command(label='Delete Line Segment')
        self.segmenu.add_command(label='Change Line Segment')
        self.linetypemenu.add_cascade(label='Line Segments', menu=self.segmenu)
        
        self.menubar.add_cascade(label='Lines', menu=self.linetypemenu)

        self.shapemenu = tk.Menu(self.menubar, tearoff=False)
        self.polymenu = tk.Menu(self.shapemenu, tearoff=False)

        self.nonpolymenu = tk.Menu(self.shapemenu, tearoff=False)

        self.ellipsemenu = tk.Menu(self.nonpolymenu, tearoff=False)
        self.ellipsemenu.add_command(label='Draw Ellipse')
        self.ellipsemenu.add_command(label='Change Ellipse')

        self.circlemenu = tk.Menu(self.ellipsemenu, tearoff=False)
        self.circlemenu.add_command(label='Draw Circle')
        self.circlemenu.add_command(label='Change Circle')
        
        self.trianglemenu = tk.Menu(self.polymenu, tearoff=False)
        
        self.trianglemenu.add_command(label='Draw Triangle')
        self.trianglemenu.add_command(label='Change Triangle')
        
        self.quadmenu = tk.Menu(self.polymenu, tearoff=False)
        self.quadmenu.add_command(label='Draw Quadrilateral')
        self.quadmenu.add_command(label='Change Quadrilateral')
        
        self.moremenu = tk.Menu(self.polymenu, tearoff=False)
        self.moremenu.add_command(label='Draw Other Polygon')
        self.moremenu.add_command(label='Change Polygon')
        
        self.menubar.add_cascade(label='Shapes', menu=self.shapemenu)
        self.shapemenu.add_cascade(label='Polygons', menu=self.polymenu)
        self.polymenu.add_cascade(label='Triangles', menu=self.trianglemenu)
        self.polymenu.add_cascade(label='Quadrilaterals', menu=self.quadmenu)
        self.polymenu.add_cascade(label='Other Polygons', menu=self.moremenu)

        self.shapemenu.add_cascade(label='Non-Polygons', menu=self.nonpolymenu)
        self.nonpolymenu.add_cascade(label='Ellipses', menu=self.ellipsemenu)
        self.ellipsemenu.add_cascade(label='Circles', menu=self.circlemenu)

        self.shapemenu.add_command(label='Delete Shape')
        
        self.config(menu=self.menubar)
