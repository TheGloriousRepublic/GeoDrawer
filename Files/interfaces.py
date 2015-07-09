try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from Files.backend import *

class CreateObjectWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.r=None #Return variable

        self.go =         tk.Button(self, text='OK', command=self.OK) #OK button
        self.abort =      tk.Button(self, text='Cancel', command=self.Cancel) #Cancel Button
        
        self.bind('<Return>', self.OK)
        self.bind('<Escape>', self.Cancel)
        
        self.protocol('WM_DELETE_WINDOW', self.Cancel)

    def quit(self):
        tk.Tk.quit(self) #Exit mainloop
        self.destroy() #Destroy the window

    def OK(self, event=None): #OK protocol for use when the user follows through
        self.r = self.getret(self)
        self.quit()

    def Cancel(self, event=None): #Cancel for when the user aborts
        self.r = self.getblank(self)
        self.quit()

    def getret(self, event=None): #Filler
        return None

    def getblank(self, event=None): #Filler
        return None

class CreatePointWindow(CreateObjectWindow):
    def __init__(self, *args, **kwargs):
        CreateObjectWindow.__init__(self, *args, **kwargs)
        
        #self.x =          tk.DoubleVar() #X variable
        #self.y =          tk.DoubleVar() #Y variable
        #self.name =       tk.StringVar() #Name variable

        self.namel =      tk.Label(self, text='Name') #Label for name box
        self.namebox =    tk.Entry(self)#, textvariable=self.name) #Name box
        self.openparen =  tk.Label(self, text='(') #Open parenthesis
        self.xe =         tk.Entry(self)#, textvariable=self.x, width=5) #Entry for X
        self.comma =      tk.Label(self, text=',') #Comma
        self.ye =         tk.Entry(self)#, textvariable=self.y, width=5) #Entry for Y
        self.closeparen = tk.Label(self, text=')') #Close parenthesis

        #Line everything up
        self.namel.grid(column=0, row=0)
        self.namebox.grid(column=1, row=0, columnspan=4)
        self.openparen.grid(column=0, row=1)
        self.xe.grid(column=1, row=1)
        self.comma.grid(column=2, row=1)
        self.ye.grid(column=3, row=1)
        self.closeparen.grid(column=4, row=1)
        
        self.abort.grid(column=1, row=2)
        self.go.grid(column=3, row=2)

        self.title('Create Point') #Window Title

    def getret(self, event=None):
        return (self.namebox.get(), Point((float(self.xe.get()), float(self.ye.get())))) #Return tuple "(Name, (X, Y))"

    def getblank(self, event=None): #Return point on cancellation
        return(None, (None, None))

class CreateLineWindow(CreateObjectWindow):
    def __init__(self, *args, **kwargs):
        CreateObjectWindow.__init__(self, *args, **kwargs)

if __name__ == '__main__': #Test
    cpw = CreatePointWindow()
    cpw.mainloop()
    print(cpw.r)
