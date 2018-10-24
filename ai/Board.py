import copy

class Board:

    def __init__(self, size):
        self.size = size
        self.listCells = []
        self.listWhites = []
        self.listBlacks = []
        self.player = 'W'  #player is always B or W
        self.user_marker = ''

    #Ta dika mou move einai ta cells

    #returns a list of move objects that correspond to the moves that can be made from the board position
    def getMoves(self): #move object = Cell object
        listCells = copy.deepcopy(self.listCells)
        listOfMoves = []
        for i in listCells:
            for j in listCells:
                if i is not j:
                    i.tags = "W." + i.tags.split('.')[1]
                    j.tags = "B." + j.tags.split('.')[1]
                    a = [copy.deepcopy(i), copy.deepcopy(j)]
                    listOfMoves.append(a)
        return listOfMoves


    def update_neighbors(self, stoneGroup, disc):
        tag = disc.tags
        for item in stoneGroup:
            for j in range(len(item.neighbours)):
                if item.neighbours[j].split(".")[1] == disc.tags.split(".")[1] and disc.tags not in item.occupied:
                    item.occupied.append(disc.tags)
                    for i in range(len(disc.neighbours)):
                        if disc.neighbours[i].split(".")[1] == item.tags.split(".")[1] and item.tags not in disc.occupied:
                            disc.occupied.append(item.tags)


    #takes one move instance and return a completely new board object that represents the position after the move is made
    def makeMove(self, move): #move needs to be of class Cell
        newBoard = copy.deepcopy(self)

        newBoard.size -=2

        newBoard.listBlacks.append(move[1]) #black
        newBoard.listWhites.append(move[0]) #white

        for i in newBoard.listCells:
            if i.tags.split('.')[1] == move[0].tags.split('.')[1]:
                newBoard.listCells.remove(i)
            if i.tags.split('.')[1] == move[1].tags.split('.')[1]:
                newBoard.listCells.remove(i)


        self.update_neighbors(newBoard.listWhites, move[0])
        self.update_neighbors(newBoard.listBlacks, move[0])
        # self.update_neighbors(newBoard.listCells, move[0])

        self.update_neighbors(newBoard.listWhites, move[1])
        self.update_neighbors(newBoard.listBlacks, move[1])
        # self.update_neighbors(newBoard.listCells, move[1])

        if newBoard.player == 'W':
            newBoard.player ='B'
        else:
            newBoard.player = 'W'

        return newBoard

    #static evaluation function: returns the score for the current position from the point of view of the given player
    def evaluate(self,player): #TODO edw kanoume evaluate ta panta?
        print(0)

    #returns the player whose turn it is to play on the current board #allagh paikth mono sto makeMove kai edw aplh epistrofh paikth k o 8eos boh8os
    def currentPlayer(self):
        # if self.player == 'W':
        #     self.player ='B'
        # else:
        #     self.player = 'W'
        return self.player

    #returns true if the position of the board is terminal
    def isGameOver(self): # edw mallon dn exei nohma na to exeis etsi prepei na tsekareis otan einai ston antistoixo paikth k pws 8a to pairnei auto
        if (self.user_marker=="White" and self.currentPlayer() == 'W' and  len(self.listCells)<=3) or (self.user_marker=="Black" and self.currentPlayer() == 'W' and  len(self.listCells)<=3):
            return True
        else:
            return False

class Cell:

    def __init__(self, x, y, neighbours,occupied, tags):
        self.x = x
        self.y = y
        self.tags = tags
        self.neighbours = neighbours
        self.occupied = occupied

    def getPosition(self):
        return self.x,self.y
