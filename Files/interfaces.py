try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

class CreateObjectWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        self.r=None
        tk.Tk.__init__(self, *args, **kwargs)

        self.go =         tk.Button(self, text='OK', command=self.OK)
        self.abort =      tk.Button(self, text='Cancel', command=self.Cancel)
        
        self.bind('<Return>', self.OK)
        self.bind('<Escape>', self.Cancel)
        
        self.protocol('WM_DELETE_WINDOW', self.Cancel)

    def quit(self):
        self.destroy()

    def OK(self, event=None):
        self.r = self.getret(self)
        self.quit()

    def Cancel(self, event=None):
        self.r = self.getblank(self)
        self.quit()

    def getret(self, event=None):
        return None

    def getblank(self, event=None):
        return None

class CreatePointWindow(CreateObjectWindow):
    def __init__(self, *args, **kwargs):
        CreateObjectWindow.__init__(self, *args, **kwargs)
        
        self.x =          tk.DoubleVar()
        self.y =          tk.DoubleVar()
        self.name =       tk.StringVar()

        self.namel =      tk.Label(self, text='Name')
        self.namebox =    tk.Entry(self, textvariable=self.name)
        self.openparen =  tk.Label(self, text='(')
        self.xe =         tk.Entry(self, textvariable=self.x, width=5)
        self.comma =      tk.Label(self, text=',')
        self.ye =         tk.Entry(self, textvariable=self.y, width=5)
        self.closeparen = tk.Label(self, text=')')

        self.namel.grid(column=0, row=0)
        self.namebox.grid(column=1, row=0, columnspan=4)
        self.openparen.grid(column=0, row=1)
        self.xe.grid(column=1, row=1)
        self.comma.grid(column=2, row=1)
        self.ye.grid(column=3, row=1)
        self.closeparen.grid(column=4, row=1)
        
        self.abort.grid(column=1, row=2)
        self.go.grid(column=3, row=2)

        self.title('Create Point')

    def getret(self, event=None):
        return (self.name.get(), (self.x.get(), self.y.get()))

    def getblank(self, event=None):
        return(None, (None, None))

if __name__ == '__main__':
    cpw = CreatePointWindow()
    cpw.mainloop()
    print(cpw.r)
