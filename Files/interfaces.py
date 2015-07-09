try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

class CreatePointWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        self.p=None
        tk.Tk.__init__(self, *args, **kwargs)
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

        self.go = tk.Button(text='OK', command=self.OK)
        self.abort = tk.Button(text='Cancel', command=self.Cancel)

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

        self.protocol('WM_DELETE_WINDOW', self.Cancel) 
        
    def quit(self):
        self.destroy()

    def OK(self):
        self.p = (self.name.get(), (self.x.get(), self.y.get()))
        self.quit()

    def Cancel(self):
        self.p = (None, None)
        self.quit()

if __name__ == '__main__':
    cpw = CreatePointWindow()
    cpw.mainloop()
    print(cpw.p)
