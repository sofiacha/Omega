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
        # d = MyDialog(self)
        # self.wait_window(d.top)
        # size_of_game = d.variable.get()
        # number_of_players = d.variable2.get()


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
                                "{}.{}".format(ro, col))
                self.hexagons.append(h)
                if debug:
                    coords = "{}, {}".format(ro+1, col+1)
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
                                "{}.{}".format(ro, col))
            self.hexagons.append(h)
            if debug:
                coords = "{}, {}".format(ro+1, col+1)
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
                              "{}.{}".format(ro, col))
                self.hexagons.append(h)
                if debug:
                    coords = "{}, {}".format(ro+1, col+1)
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
                                "{}.{}".format(ro, col))
            self.hexagons.append(h)
            if debug:
                coords = "{}, {}".format(ro+1, col+1)
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
                                "{}.{}".format(ro, col))
            self.hexagons.append(h)
            if debug:
                coords = "{}, {}".format(ro+1, col+1)
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
                                "{}.{}".format(ro, col))
            self.hexagons.append(h)
            if debug:
                coords = "{}, {}".format(ro+1, col+1)
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
                                "{}.{}".format(r, c))
                self.hexagons.append(h)
                if debug:
                    coords = "{}, {}".format(r+1, c+1)
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
                                "{}.{}".format(r, c))
                self.hexagons.append(h)
                if debug:
                    coords = "{}, {}".format(r+1, c+1)
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
                              "{}.{}".format(ro, ciol))
                self.hexagons.append(h)
                if debug:
                    coords = "{}, {}".format(ro+1, ciol+1)
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
                              "{}.{}".format(ro, ciol))
                self.hexagons.append(h)
                if debug:
                    coords = "{}, {}".format(ro+1, ciol+1)
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
                                "{}.{}".format(ro, cil))
            self.hexagons.append(h)
            if debug:
                coords = "{}, {}".format(ro+1, cil+1)
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
                             "{}.{}".format(ro, ci))
            self.hexagons.append(h)
            if debug:
                coords = "{}, {}".format(ro+1, ci+1)
                self.can.create_text((ro * (size * sqrt(3))) + offset+120,
                                     ci * (size * 1.5) + 9.75 * (size * sqrt(3) / 2) + 146+10,
                                     text=coords)

    def click(self, evt):
        """
        hexagon detection on mouse click
        """
        x, y  = evt.x, evt.y
        for i in self.hexagons:
             if (abs(i.x-y) <= 39/2 and abs(i.y-x) <=39/2):
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