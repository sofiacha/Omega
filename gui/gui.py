from classes import *
from init_grid import *
from random import randint
# ---------------------------------------------------------
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Omega")
        self.can = Canvas(self, width=900, height=700, bg="#E0E8E1")
        self.can.pack()
        self.hexagons = []
        self.openP = []
        self.blackpieces = []
        self.whitepieces = []
        self.user_marker =""
        self.counter = 0
        self.initGrid(11, 14, 22, debug=True)
        self.can.bind("<Button-1>", self.click)

    def click(self, evt):
        size = 22
        x, y = evt.x, evt.y
        item = self.can.find_closest(x, y)[0]
        tags = self.can.gettags(item)
        print tags
        for i in self.hexagons:
             if ((x < i.y+size and i.y-size/3<x )and (y<i.x+size and i.x-(size/2)<y)):
                i.selected = True
                if i in self.openP:
                    if self.user_marker=="White" and self.counter%4==0 and len(self.openP)>=4:
                        disc = WhiteCircle(self.can, i.y + size-3, i.x + size / 2, size/1.5 , "#fff", "{}.{}".format("W", i.tags.split(".")[1]))
                        self.counter += 1
                        self.whitepieces.append(disc)
                        self.openP.remove(i)

                    elif self.user_marker=="White" and self.counter%4==1:
                        disc = BlackCircle(self.can, i.y + size - 3, i.x + size / 2, size / 1.5, "#000", "{}.{}".format("B", i.tags.split(".")[1]))
                        self.blackpieces.append(disc)
                        self.counter += 1
                        self.openP.remove(i)

                        j = randint(0, len(self.openP) - 1)
                        disc = WhiteCircle(self.can, self.openP[j].y + size - 3, self.openP[j].x + size / 2, size / 1.5,"#fff", "{}.{}".format("W", self.openP[j].tags.split(".")[1]))
                        self.counter += 1
                        self.whitepieces.append(disc)
                        self.openP.remove(self.openP[j])

                        j = randint(0, len(self.openP) - 1)
                        disc = BlackCircle(self.can, self.openP[j].y + size - 3, self.openP[j].x + size / 2, size / 1.5, "#000", "{}.{}".format("B", self.openP[j].tags.split(".")[1]))
                        self.counter += 1
                        self.blackpieces.append(disc)
                        self.openP.remove(self.openP[j])

                    elif self.user_marker=="Black" and self.counter%4==2:
                        disc = WhiteCircle(self.can, i.y + size - 3, i.x + size / 2, size / 1.5, "#fff", "{}.{}".format("W", i.tags.split(".")[1]))
                        self.counter += 1
                        self.whitepieces.append(disc)
                        self.openP.remove(i)

                    elif self.user_marker=="Black" and self.counter%4==3:
                        disc = BlackCircle(self.can, i.y + size - 3, i.x + size / 2, size / 1.5, "#000", "{}.{}".format("B", i.tags.split(".")[1]))
                        self.counter += 1
                        self.blackpieces.append(disc)
                        self.openP.remove(i)
                        if len(self.openP)>=4:
                            j = randint(0, len(self.openP) - 1)
                            disc = WhiteCircle(self.can, self.openP[j].y + size - 3, self.openP[j].x + size / 2, size / 1.5, "#fff", "{}.{}".format("W", self.openP[j].tags.split(".")[1]))
                            self.counter += 1
                            self.whitepieces.append(disc)
                            self.openP.remove(self.openP[j])

                            j = randint(0, len(self.openP) - 1)
                            disc = BlackCircle(self.can, self.openP[j].y + size - 3, self.openP[j].x + size / 2, size / 1.5, "#000", "{}.{}".format("B", self.openP[j].tags.split(".")[1]))
                            self.counter += 1
                            self.blackpieces.append(disc)
                            self.openP.remove(self.openP[j])
                        else:
                            print("game is over")
                            GameOver(self)
                    if len(self.openP)<4:
                        GameOver(self)
                        print("game is over")

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
        # d = GridSizeDialog(self)
        # self.wait_window(d.top)
        # size_of_game = d.variable.get()
        # user_marker = d.variable2.get()
        self.user_marker ="Black"
        if self.user_marker=="White":
            computer_marker ="Black"
        else:
            computer_marker = "White"
        txt1 = "User Marker: " + self.user_marker + "\nComputer Marker: " + computer_marker
        self.can.create_text(100, 100, text=txt1)

        self.hexagons = init_grid(self.can,cols, rows, size, debug)
        size_of_game = "5x5"
        self.openP = choose_grid(self.can, size_of_game,self.hexagons)
        if computer_marker == "White":
            i = randint(0, len(self.openP)-1)
            disc = WhiteCircle(self.can, self.openP[i].y + size - 3, self.openP[i].x + size / 2, size / 1.5, "#fff", "{}.{}".format("W", self.openP[i].tags.split(".")[1]))
            self.counter+=1
            i = randint(0, len(self.openP) - 1)
            disc = BlackCircle(self.can, self.openP[i].y + size - 3, self.openP[i].x + size / 2, size / 1.5, "#000", "{}.{}".format("B", self.openP[i].tags.split(".")[1]))
            self.counter += 1



# ----------------------------------------------------------
if __name__ == '__main__':

    app = App()
    app.mainloop()