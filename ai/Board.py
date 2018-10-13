import copy

class Board:

    def __init__(self, size):
        self.size = size
        self.listCells = []
        self.listWhites = []
        self.listBlacks = []
        self.player = 'W'  #player is always B or W

    #returns a list of move objects that correspond to the moves that can be made from the board position
    def getMoves(self): #move object = Cell object
        listCells = copy.deepcopy(self.listCells)
        for i in listCells:
            i.tags = self.player + "." + i.tags.split('.')[1]
        return listCells

    #takes one move instance and return a completely new board object that represents the position after the move is made
    def makeMove(self, move): #move needs to be of class Cell
        newBoard = copy.deepcopy(self)  #TODO edw prepei na baloume n pros8etei k stous geitones to stone pou pros8etei
        for i in newBoard.listCells:
            if i.tags.split('.')[1] == move.tags.split('.')[1]:
                if move.tags.split('.')[0] == 'W':
                    newBoard.listWhites.append(move)
                else:
                    newBoard.listBlacks.append(move)
                newBoard.listCells.remove(i)
                # newBoard.size-=1
        return newBoard

    #static evaluation function: returns the score for the current position from the point of view of the given player
    def evaluate(self,player): #TODO edw kanoume evaluate ta panta?
        print(0)


    #returns the player whose turn it is to play on the current board
    def currentPlayer(self): #TODO edw isws na baleis to poios paizei me counter
        if self.player == 'W':
            self.player ='B'
        else:
            self.player = 'W'
        return self.player

    #returns true if the position of the board is terminal
    def isGameOver(self): # edw mallon dn exei nohma na to exeis etsi prepei na tsekareis otan einai ston antistoixo paikth k pws 8a to pairnei auto
        if len(self.listCells)==0:  #TODO edw na balw to swsto functionality counter again?
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
