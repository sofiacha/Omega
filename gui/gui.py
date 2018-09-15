from classes import *
from init_grid import *
# ---------------------------------------------------------
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Omega")
        self.can = Canvas(self, width=900, height=700, bg="#E0E8E1")
        self.can.pack()
        self.hexagons = []
        self.initGrid(11, 14, 22, debug=True)
        self.can.bind("<Button-1>", self.click)

    def click(self, evt):
        size = 22
        x, y = evt.x, evt.y
        item = self.can.find_closest(x, y)[0]
        tags = self.can.gettags(item)
        print tags
        # print("x: ", x, "y: ", y)
        for i in self.hexagons:
             if ((x < i.y+size and i.y-size/3<x )and (y<i.x+size and i.x-(size/2)<y)):
                i.selected = True
        for i in self.hexagons:
            if i.selected:
                self.can.itemconfigure(i.tags, fill="#53ca53")
                self.after(500, self.bye)

    def bye(self):
        for i in self.hexagons:
             if i.selected:
                self.can.itemconfigure(i.tags, fill="#5FFF2D")
                i.selected = False

    def initGrid(self, cols, rows, size, debug):
        # d = MyDialog(self)
        # self.wait_window(d.top)
        # size_of_game = d.variable.get()
        # print(size_of_game)

        self.hexagons = init_grid(self.can,cols, rows, size, debug)

        size_of_game = "5x5"
        openP = choose_grid(self.can, size_of_game,self.hexagons)


# ----------------------------------------------------------
if __name__ == '__main__':

    app = App()
    app.mainloop()