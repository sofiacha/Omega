from classes import *
from init_tools import *
from ai.abNegamax import *
# from ai.minimax import *
# from ai.negamax import *
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
        self.scores = []
        self.whiteGroups =[]
        self.blackGroups = []
        self.blackpieces = []
        self.whitepieces = []
        self.user_marker =""
        self.counter = 0
        self.Board = Board
        self.initGrid(11, 14, 22, debug=True)
        self.can.bind("<Button-1>", self.click)

    def click(self, evt):
        size = 22
        x, y = evt.x, evt.y
        b = False
        for i in self.hexagons:
             if ((x < i.y+size and i.y-size/3<x )and (y<i.x+size and i.x-(size/2)<y)):
                i.selected = True
                if i in self.openP:
                    if self.user_marker=="White" and self.counter%4==0:
                        disc = WhiteStone(self.can, i.y + size-3, i.x + size / 2, size/1.5 , "#fff", "{}.{}".format("W", i.tags.split(".")[1]))
                        self.counter += 1
                        disc.neighbors = i.neighbors
                        disc.occupied = i.occupied

                        self.whiteGroups = groupsf(self.whitepieces, disc, self.openP, "W.")
                        self.scores = score(self.blackGroups, self.whiteGroups)
                        print(self.scores)
                        print("---------------------------------------------------------------")
                        txt2 = "Whites: " + str(self.scores[0]) + "\nBlacks: " + str(self.scores[1])
                        if self.counter>1:
                            self.can.itemconfig(tagOrId="text2", text=txt2)
                        else:
                            self.can.create_text(100, 200, text=txt2, tags="text2")

                        self.whitepieces.append(disc)
                        self.openP.remove(i)


                    elif self.user_marker=="White" and self.counter%4==1:
                        disc = BlackStone(self.can, i.y + size - 3, i.x + size / 2, size / 1.5, "#000", "{}.{}".format("B", i.tags.split(".")[1]))
                        disc.neighbors = i.neighbors
                        disc.occupied = i.occupied

                        self.blackGroups = groupsf(self.blackpieces, disc, self.openP, "B.")
                        self.scores = score(self.blackGroups, self.whiteGroups)
                        print(self.scores)
                        print("--------------------------------------------------------------")
                        txt2 = "Whites: " + str(self.scores[0]) + "\nBlacks: " + str(self.scores[1])
                        self.can.itemconfig(tagOrId="text2", text=txt2)
                        self.blackpieces.append(disc)
                        self.counter += 1
                        self.openP.remove(i)

                        # AI -----------------------------------------------------------------------------------------------------#
                        self.Board = initBoard(self.openP, self.whitepieces, self.blackpieces, "B",
                                               self.user_marker)  # auto 8a ginetai ka8e fora prin thn kinhsh tou computer
                        # best_move = getBestMove(self.Board, "W", 1)
                        # print(best_move[0].tags +"   "+best_move[1].tags)
                        # best_move = getBestMoveNM(self.Board, 1)
                        best_move = getBestMoveAB(self.Board, 1)
                        print(best_move[0].tags +"   "+best_move[1].tags)
                        #Best positions ------------------------------------------------------------------------------------------#
                        hexW, hexB = findxy(self.openP, best_move)
                        #Apply best positions ------------------------------------------------------------------------------------#
                        disc = WhiteStone(self.can, hexW.y + size - 3, hexW.x + size / 2, size / 1.5,"#fff", "{}.{}".format("W", hexW.tags.split(".")[1]))
                        self.counter += 1
                        disc.neighbors = hexW.neighbors
                        disc.occupied = hexW.occupied
                        self.whiteGroups = groupsf(self.whitepieces, disc, self.openP, "W.")
                        self.scores = score(self.blackGroups, self.whiteGroups)
                        print(self.scores)
                        print("---------------------------------------------------------------")
                        txt2 = "Whites: " + str(self.scores[0]) + "\nBlacks: " + str(self.scores[1])
                        self.can.itemconfig(tagOrId="text2", text=txt2)
                        self.whitepieces.append(disc)
                        self.openP.remove(hexW)

                        disc = BlackStone(self.can, hexB.y + size - 3, hexB.x + size / 2, size / 1.5, "#000", "{}.{}".format("B", hexB.tags.split(".")[1]))
                        self.counter += 1
                        disc.neighbors = hexB.neighbors
                        disc.occupied = hexB.occupied
                        self.blackGroups = groupsf(self.blackpieces, disc, self.openP, "B.")
                        self.scores = score(self.blackGroups, self.whiteGroups)
                        print(self.scores)
                        print("----------------------------------------------------------------")
                        txt2 = "Whites: " + str(self.scores[0]) + "\nBlacks: " + str(self.scores[1])
                        self.can.itemconfig(tagOrId="text2", text=txt2)
                        self.blackpieces.append(disc)
                        self.openP.remove(hexB)

                        if len(self.openP)<4:
                            b = True

                    elif self.user_marker=="Black" and self.counter%4==2:
                        disc = WhiteStone(self.can, i.y + size - 3, i.x + size / 2, size / 1.5, "#fff", "{}.{}".format("W", i.tags.split(".")[1]))
                        self.counter += 1
                        disc.neighbors = i.neighbors
                        disc.occupied = i.occupied
                        self.whiteGroups = groupsf(self.whitepieces, disc, self.openP, "W.")
                        self.scores = score(self.blackGroups, self.whiteGroups)
                        print(self.scores)
                        print("---------------------------------------------------------------")
                        txt2 = "Whites: " + str(self.scores[0]) + "\nBlacks: " + str(self.scores[1])
                        self.can.itemconfig(tagOrId="text2", text=txt2)
                        self.whitepieces.append(disc)
                        self.openP.remove(i)

                    elif self.user_marker=="Black" and self.counter%4==3:
                        disc = BlackStone(self.can, i.y + size - 3, i.x + size / 2, size / 1.5, "#000", "{}.{}".format("B", i.tags.split(".")[1]))
                        self.counter += 1
                        disc.neighbors = i.neighbors
                        disc.occupied = i.occupied
                        self.blackGroups = groupsf(self.blackpieces, disc, self.openP, "B.")
                        self.scores = score(self.blackGroups, self.whiteGroups)
                        print(self.scores)
                        print("----------------------------------------------------------------")
                        txt2 = "Whites: " + str(self.scores[0]) + "\nBlacks: " + str(self.scores[1])
                        self.can.itemconfig(tagOrId="text2", text=txt2)
                        self.blackpieces.append(disc)
                        self.openP.remove(i)
                        if len(self.openP)>=4:

                            # AI -----------------------------------------------------------------------------------------------------#
                            self.Board = initBoard(self.openP, self.whitepieces, self.blackpieces, "W",
                                                   self.user_marker)  # auto 8a ginetai ka8e fora prin thn kinhsh tou computer
                            #best_move = getBestMove(self.Board, "B", 1)
                            # best_move = getBestMoveNM(self.Board, 1)
                            best_move = getBestMoveAB(self.Board, 1)
                            print(best_move[0].tags + "   " + best_move[1].tags)
                            # Best positions ------------------------------------------------------------------------------------------#
                            hexW, hexB = findxy(self.openP, best_move)

                            # Apply best positions ------------------------------------------------------------------------------------#
                            disc = WhiteStone(self.can, hexW.y + size - 3, hexW.x + size / 2, size / 1.5, "#fff", "{}.{}".format("W", hexW.tags.split(".")[1]))
                            self.counter += 1
                            disc.neighbors = hexW.neighbors
                            disc.occupied = hexW.occupied
                            self.whiteGroups = groupsf(self.whitepieces, disc, self.openP, "W.")
                            self.scores = score(self.blackGroups, self.whiteGroups)
                            print(self.scores)
                            print("---------------------------------------------------------------")
                            txt2 = "Whites: " + str(self.scores[0]) + "\nBlacks: " + str(self.scores[1])
                            self.can.itemconfig(tagOrId="text2", text=txt2)
                            self.whitepieces.append(disc)
                            self.openP.remove(hexW)

                            disc = BlackStone(self.can, hexB.y + size - 3, hexB.x + size / 2, size / 1.5, "#000", "{}.{}".format("B", hexB.tags.split(".")[1]))
                            self.counter += 1
                            disc.neighbors = hexB.neighbors
                            disc.occupied = hexB.occupied
                            self.blackGroups = groupsf(self.blackpieces, disc, self.openP, "B.")
                            self.scores = score(self.blackGroups, self.whiteGroups)
                            print(self.scores)
                            print("----------------------------------------------------------------")
                            txt2 = "Whites: " + str(self.scores[0]) + "\nBlacks: " + str(self.scores[1])
                            self.can.itemconfig(tagOrId="text2", text=txt2)
                            self.blackpieces.append(disc)
                            self.openP.remove(hexB)

                        else:
                            b = True
                    if b==True:
                        GameOver(self,self.scores)
                        print("game is over: W:",self.scores[0],"  B: ", self.scores[1])

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
        #TODO uncomment before publish
        d = GridSizeDialog(self)
        self.wait_window(d.top)
        size_of_game = d.variable.get()
        self.user_marker = d.variable2.get()

        # self.user_marker ="White"

        if self.user_marker=="White":
            computer_marker ="Black"
        else:
            computer_marker = "White"

        txt1 = "User Marker: " + self.user_marker + "\nComputer Marker: " + computer_marker
        self.can.create_text(100, 100, text=txt1)

        self.hexagons = init_grid(self.can,cols, rows, size, debug)
        size_of_game = "5x5"
        self.openP = choose_grid(self.can, size_of_game,self.hexagons)
        calculate_neighbors(self.openP, size)

        if computer_marker == "White":
            i = randint(0, len(self.openP)-1)
            disc = WhiteStone(self.can, self.openP[i].y + size - 3, self.openP[i].x + size / 2, size / 1.5, "#fff", "{}.{}".format("W", self.openP[i].tags.split(".")[1]))
            self.counter+=1
            disc.neighbors = self.openP[i].neighbors
            disc.occupied = self.openP[i].occupied
            self.whiteGroups = groupsf(self.whitepieces, disc, self.openP, "W.")
            self.scores = score(self.blackGroups, self.whiteGroups)
            print(self.scores)
            print("---------------------------------------------------------------")
            txt2 = "Whites: " + str(self.scores[0]) + "\nBlacks: " + str(self.scores[1])
            self.can.create_text(100, 200, text=txt2, tags="text2")
            self.whitepieces.append(disc)
            self.openP.remove(self.openP[i])

            i = randint(0, len(self.openP) - 1)
            disc = BlackStone(self.can, self.openP[i].y + size - 3, self.openP[i].x + size / 2, size / 1.5, "#000", "{}.{}".format("B", self.openP[i].tags.split(".")[1]))
            self.counter += 1
            disc.neighbors = self.openP[i].neighbors
            disc.occupied = self.openP[i].occupied
            self.blackGroups = groupsf(self.blackpieces, disc, self.openP, "B.")
            self.scores = score(self.blackGroups, self.whiteGroups)
            print(self.scores)
            print("---------------------------------------------------------------")
            txt2 = "Whites: " + str(self.scores[0]) + "\nBlacks: " + str(self.scores[1])
            self.can.itemconfig(tagOrId="text2", text=txt2)
            self.blackpieces.append(disc)
            self.openP.remove(self.openP[i])

# ----------------------------------------------------------
if __name__ == '__main__':

    app = App()
    app.mainloop()