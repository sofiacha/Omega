from classes import *
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

    def initGrid(self, cols, rows, size, debug):
        d = MyDialog(self)
        self.wait_window(d.top)
        size_of_game = d.variable.get()
        print(size_of_game)

        #1h sthlh
        for col in range(3):
            if col % 2 == 0:
                offset = size * sqrt(3) / 2  #edw afhnei to keno tou enos hexagonal -_-_-_-_-
            else:
                offset = 0
            for ro in range(1):
                h = FillHexagon(self.can,
                                col * (size * 1.5) + 8.05*(size * sqrt(3) / 2 )+ 145,
                                (ro * (size * sqrt(3))) + offset+100,  #(self, parent, x, y, length, color, tags):
                                size,
                                "#5FFF2D",
                                "{}".format(len(self.hexagons)-1))
                self.hexagons.append(h)
                if debug:
                    coords = "{}".format(len(self.hexagons)-1)
                    self.can.create_text((ro * (size * sqrt(3))) +120 + offset,
                                         col * (size * 1.5) + 8.05 * (size * sqrt(3) / 2) +145 +10,
                                         text=coords)
        #2h sthlh
        for col in range(7):
            if col % 2 == 0:
                offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
            else:
                offset = 0
            for ro in range(1, 2, 1):
                h = FillHexagon(self.can,
                                col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) + 146,
                                (ro * (size * sqrt(3))) + offset+100,  # (self, parent, x, y, length, color, tags):
                                size,
                                "#5FFF2D",
                                "{}".format(len(self.hexagons)-1))
            self.hexagons.append(h)
            if debug:
                coords = "{}".format(len(self.hexagons)-1)
                self.can.create_text((ro * (size * sqrt(3))) + offset + 120,
                                     col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) + 146+10,
                                     text=coords)
        #3h grammh
        for col in range(11):
                if col % 2 == 0:
                   offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
                else:
                   offset = 0
                for ro in range(2,3,1):
                   h = FillHexagon(self.can,
                              col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2)+81,
                              (ro * (size * sqrt(3))) + offset+100,  # (self, parent, x, y, length, color, tags):
                              size,
                              "#5FFF2D",
                              "{}".format(len(self.hexagons)-1))
                self.hexagons.append(h)
                if debug:
                    coords = "{}".format(len(self.hexagons)-1)
                    self.can.create_text((ro * (size * sqrt(3))) + offset+120,
                                         col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2)+81+10,
                                         text=coords)


        #4h sthlh
        for col in range(15):
            if col % 2 == 0:
                offset = size * sqrt(3) / 2 # edw afhnei to keno tou enos hexagonal -_-_-_-_-
            else:
                offset = 0
            for ro in range(3, 4, 1):
                h = FillHexagon(self.can,
                                col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2)+14,
                                (ro * (size * sqrt(3))) + offset+100,  # (self, parent, x, y, length, color, tags):
                                size,
                                "#5FFF2D",
                                "{}".format(len(self.hexagons)-1))
            self.hexagons.append(h)
            if debug:
                coords = "{}".format(len(self.hexagons)-1)
                self.can.create_text((ro * (size * sqrt(3))) + offset + 120,
                                     col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) + 15+ 10 ,
                                     text=coords)
        #5h sthlh
        for col in range(19):
            if col % 2 == 0:
                offset = size * sqrt(3) / 2 # edw afhnei to keno tou enos hexagonal -_-_-_-_-
            else:
                offset = 0
            for ro in range(4, 5, 1):
                h = FillHexagon(self.can,
                                col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2)-52,
                                (ro * (size * sqrt(3))) + offset+100,  # (self, parent, x, y, length, color, tags):
                                size,
                                "#5FFF2D",
                                "{}".format(len(self.hexagons)-1))
            self.hexagons.append(h)
            if debug:
                coords = "{}".format(len(self.hexagons)-1)
                self.can.create_text((ro * (size * sqrt(3))) + offset + 120,
                                     col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) -50 + 10,
                                     text=coords)

        #6h sthlh
        for col in range(19):
            if col % 2 == 0:
                offset = size * sqrt(3) / 2 # edw afhnei to keno tou enos hexagonal -_-_-_-_-
            else:
                offset = 0
            for ro in range(5, 6, 1):
                h = FillHexagon(self.can,
                                col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2)-52,
                                (ro * (size * sqrt(3))) + offset+100,  # (self, parent, x, y, length, color, tags):
                                size,
                                "#5FFF2D",
                                "{}".format(len(self.hexagons)-1))
            self.hexagons.append(h)
            if debug:
                coords = "{}".format(len(self.hexagons)-1)
                self.can.create_text((ro * (size * sqrt(3))) + offset+120,
                                     col * (size * 1.5) + 4.55 * (size * sqrt(3) / 2) - 50 +10,
                                     text=coords)

        #7 ews 15 sthles
        for c in range(19):
            if c % 2 == 0:
                offset = size * sqrt(3) / 2  #edw afhnei to keno tou enos hexagonal -_-_-_-_-
            else:
                offset = 0
            for r in range(6,rows,1):
                h = FillHexagon(self.can,
                                c * (size * 1.5)+ 35 ,
                                (r * (size * sqrt(3))) + offset+100,
                                size,
                                "#5FFF2D",
                                "{}".format(len(self.hexagons)-1))
                self.hexagons.append(h)
                if debug:
                    coords = "{}".format(len(self.hexagons)-1)
                    self.can.create_text((r * (size * sqrt(3))) + offset+120,
                                         c * (size * 1.5)+ 35 +10,
                                         text=coords)

        #16h sthlh
        for c in range(17):
            if c % 2 != 0:
                offset = size * sqrt(3) / 2  #edw afhnei to keno tou enos hexagonal -_-_-_-_-
            else:
                offset = 0
            for r in range(rows,rows+1,1):
                h = FillHexagon(self.can,
                                c * (size * 1.5)+ 68 ,
                                (r * (size * sqrt(3))) + offset+100,
                                size,
                                "#5FFF2D",
                                "{}".format(len(self.hexagons)-1))
                self.hexagons.append(h)
                if debug:
                    coords = "{}".format(len(self.hexagons)-1)
                    self.can.create_text((r * (size * sqrt(3))) + offset+120,
                                         c * (size * 1.5)+ 68+10,
                                         text=coords)

        #17h sthlh
        for ciol in range(13):
                if ciol % 2 != 0:
                   offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
                else:
                   offset = 0
                for ro in range(rows+1,rows+2,1):
                   h = FillHexagon(self.can,
                              ciol * (size * 1.5) + 2.8 * (size * sqrt(3) / 2)+81,
                              (ro * (size * sqrt(3))) + offset+100,  # (self, parent, x, y, length, color, tags):
                              size,
                              "#5FFF2D",
                              "{}".format(len(self.hexagons)-1))
                self.hexagons.append(h)
                if debug:
                    coords = "{}".format(len(self.hexagons)-1)
                    self.can.create_text((ro * (size * sqrt(3))) + offset+120,
                                         ciol * (size * 1.5) + 2.8 * (size * sqrt(3) / 2) + 81+10,
                                         text=coords)
        #18h sthlh
        for ciol in range(9):
                if ciol % 2 != 0:
                   offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
                else:
                   offset = 0
                for ro in range(rows+2,rows+3,1):
                   h = FillHexagon(self.can,
                              ciol * (size * 1.5) + 2.8 * (size * sqrt(3) / 2)+146,
                              (ro * (size * sqrt(3))) + offset+100,  # (self, parent, x, y, length, color, tags):
                              size,
                              "#5FFF2D",
                              "{}".format(len(self.hexagons)-1))
                self.hexagons.append(h)
                if debug:
                    coords = "{}".format(len(self.hexagons)-1)
                    self.can.create_text((ro * (size * sqrt(3))) + offset+120,
                                         ciol * (size * 1.5) + 2.8 * (size * sqrt(3) / 2) + 146+10,
                                         text=coords)
        #19h sthlh
        for cil in range(5):
            if cil % 2 != 0:
                offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
            else:
                offset = 0
            for ro in range(rows+3, rows + 4, 1):
                h = FillHexagon(self.can,
                                cil * (size * 1.5) + 6.3 * (size * sqrt(3) / 2)+146,
                                (ro * (size * sqrt(3))) + offset+100,  # (self, parent, x, y, length, color, tags):
                                size,
                                "#5FFF2D",
                                "{}".format(len(self.hexagons)-1))
            self.hexagons.append(h)
            if debug:
                coords = "{}".format(len(self.hexagons)-1)
                self.can.create_text((ro * (size * sqrt(3))) + offset+120,
                                     cil * (size * 1.5) + 6.3 * (size * sqrt(3) / 2) + 146+10,
                                     text=coords)
         #20h sthlh
        for ci in range(1):
            if ci % 2 != 0:
                offset = size * sqrt(3) / 2  # edw afhnei to keno tou enos hexagonal -_-_-_-_-
            else:
                offset = 0
            for ro in range(rows + 4, rows + 5, 1):
                h = FillHexagon(self.can,
                             ci * (size * 1.5) + 9.75 * (size * sqrt(3) / 2)+146,
                             (ro * (size * sqrt(3))) + offset + 100,  # (self, parent, x, y, length, color, tags):
                             size,
                             "#5FFF2D",
                             "{}".format(len(self.hexagons)-1))
            self.hexagons.append(h)
            if debug:
                coords = "{}".format(len(self.hexagons)-1)
                self.can.create_text((ro * (size * sqrt(3))) + offset+120,
                                     ci * (size * 1.5) + 9.75 * (size * sqrt(3) / 2) + 146+10,
                                     text=coords)
        if (size_of_game == "5x5"):
            cL = 115
            cR = 119
            cRM = 153
            cLM = 64
            cLB = 179
            cRB = 183
        if (size_of_game == "6x6"):
            cL = 106
            cR = 111
            cRM = 234
            cLM = 48
            cLB = 186
            cRB = 191
        if (size_of_game == "7x7"):
            cL = 98
            cR = 104
            cRM = 249
            cLM = 28
            cLB = 194
            cRB = 200
        if (size_of_game == "8x8"):
            cL = 57
            cR = 96
            cRM = 260
            cLM = 15
            cLB = 71
            cRB = 208
        if (size_of_game == "9x9"):
            cL = 56
            cR = 89
            cRM = 267
            cLM = 6
            cLB = 72
            cRB = 217
        if (size_of_game == "10x10"):
            cL = 36
            cR = 81
            cRM = 270
            cLM = 1
            cLB = 54
            cRB = 225
        CornerLeft(self.can, self.hexagons[cL].y+7,self.hexagons[cL].x-22)            #5x5 : 115,   6x6: 106, 7x7: 98,  8x8:57,   9x9:  56, 10x10: 36
        CornerRight(self.can, self.hexagons[cR].y -19, self.hexagons[cR].x - 22)      #5x5 : 119,   6x6: 111, 7x7: 104  8x8:96,   9x9:  89, 10x10: 81
        CornerRightMiddle(self.can, self.hexagons[cRM].y +20, self.hexagons[cRM].x-33 ) # 5x5 : 153,  6x6: 234, 7x7: 249, 8x8:260,  9x9:  267,10x10: 270
        CornerLeftMiddle(self.can, self.hexagons[cLM].y+20 ,self.hexagons[cLM].x-33 )     # 5x5 : 64,   6x6: 48,  7x7: 28,  8x8:15,   9x9:  6,  10x10: 1
        CornerLeftBottom(self.can, self.hexagons[cLB].y-19 ,self.hexagons[cLB].x -10)   # 5x5 : 179,  6x6: 186, 7x7: 194, 8x8:71,   9x9:  72, 10x10: 54
        CornerRightBottom(self.can, self.hexagons[cRB].y +57,self.hexagons[cRB].x -10)  # 5x5 : 183,  6x6: 191, 7x7: 200, 8x8:208,  9x9:  217,10x10: 225

    def click(self, evt):
        """
        hexagon detection on mouse click
        """
        size = 22
        x, y = evt.x, evt.y
        print("x: ", x, "y: ", y)
        for i in self.hexagons:
             if ((x < i.y+size and i.y-size/3<x )and (y<i.x+size and i.x-(size/2)<y)):
                 i.selected = True
        for i in self.hexagons:  # re-configure selected only
            if i.selected:
                self.can.itemconfigure(i.tags, fill="#53ca53")
                self.after(500, self.bye)

    def bye(self):
        for i in self.hexagons:
            self.can.itemconfigure(i.tags, fill="#5FFF2D")
            i.selected = False
 # ----------------------------------------------------------
if __name__ == '__main__':

    app = App()
    app.mainloop()