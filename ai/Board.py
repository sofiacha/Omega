import copy

class Board:

    def __init__(self, size):
        self.size = size
        self.listCells = []
        self.listWhites = []
        self.listBlacks = []
        self.player = 'W'  # player is always B or W
        self.user_marker = ''
        self.score = []
        self.previous_score = [0, 0]
        self.groupW = []
        self.groupB = []

    # Ta dika mou move einai ta cells
    # returns a list of move objects that correspond to the moves that can be made from the board position
    def getMoves(self): # move object = Cell object
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

    # takes one move instance and return a completely new board object that represents the position after the move is made
    def makeMove(self, move): #move needs to be of class Cell
        newBoard = copy.deepcopy(self)
        newBoard.size -=2
        newBoard.previous_score = copy.deepcopy(newBoard.score)
        newBoard.groupB = groupsfAI(newBoard.listBlacks, move[1], newBoard.listCells, "B.")
        newBoard.groupW = groupsfAI(newBoard.listWhites, move[0], newBoard.listCells, "W.")

        newBoard.score = scorefAI(newBoard.groupB, newBoard.groupW)
        newBoard.listBlacks.append(move[1]) # black
        newBoard.listWhites.append(move[0]) # white

        for i in newBoard.listCells:
            if i.tags.split('.')[1] == move[0].tags.split('.')[1]:
                newBoard.listCells.remove(i)
            if i.tags.split('.')[1] == move[1].tags.split('.')[1]:
                newBoard.listCells.remove(i)

        # edw exei nohma na to energopoieis mono otan trexeis minimax 8arrw

        if newBoard.player == 'W':
            newBoard.player ='B'
        else:
            newBoard.player = 'W'
        return newBoard

    # static evaluation function: returns the score for the current position from the point of view of the given player
    def evaluate(self,player): # TODO 8elei pio e3upno tropo gia to f add 3 stones thingy, distance greater than 1 ok but if smaller don't put anything
        score = self.score
        if not score:
            score.append(len(self.listWhites))
            score.append(len(self.listBlacks))
        if self.player == "W":
            x = score[0]
            y = score[1]
        else:
            y = score[0]
            x = score[1]
        f = 5*x-1*y
        return f

    def evaluateNM(self): # TODO 8elei pio e3upno tropo gia to f add 3 stones thingy, distance greater than 1 ok but if smaller don't put anything
        score = self.score
        previous_score = self.previous_score
        if not score:
            score.append(len(self.listWhites))
            score.append(len(self.listBlacks))

        if self.player == "W":
            x = score[0]
            y = score[1]
            if not previous_score:
                xx = 0
                yy = 0
            else:
                xx = previous_score[0]
                yy = previous_score[1]

            c=0
            for i in self.groupW:
                if len(i) > 3:
                    c+=1
        else:
            y = score[0]
            x = score[1]
            if not previous_score:
                yy=0
                xx=0
            else:
                yy = previous_score[0]
                xx = previous_score[1]
            c=0
            for i in self.groupB:
                if len(i) > 3:
                    c+=1
        f = 5 * (x-xx) - 1 * (y-yy) - c*2
        return f

    # returns the player whose turn it is to play on the current board #allagh paikth mono sto makeMove kai edw aplh epistrofh paikth k o 8eos boh8os
    def currentPlayer(self):
        return self.player

    # returns true if the position of the board is terminal
    def isGameOver(self): # edw mallon dn exei nohma na to exeis etsi prepei na tsekareis otan einai ston antistoixo paikth k pws 8a to pairnei auto
        if (self.user_marker=="Black" and self.currentPlayer() == 'W' and  len(self.listCells)<=3):
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

# - Useful functions ---------------------------------------------------------------------------------------#
def dfsAI(graphs, disc, BorW):
    graph = {}
    for i in graphs:
        graph[BorW + i.tags.split(".")[1]] = set(i.occupied)
    visited, stack = set(), [disc.tags]
    if graph:
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(graph[vertex] - visited)
    return visited

def groupsfAI(stones, disc, openPosition, BorW): # stones2 = disc
    group = []
    update_neighborsAI(stones, disc)
    for item in stones:
        group.append(dfsAI(set(openPosition).union(set(stones)), item, BorW))
    group.append(dfsAI(set(openPosition).union(set(stones)), disc, BorW))
    t1 = set(frozenset(i) for i in group)
    groups = [set(jj) for jj in t1]
    return groups

def scorefAI(blacks, whites):
    black_sizes = [len(i) for i in blacks]
    white_sizes = [len(i) for i in whites]
    if len(black_sizes) > 0:
        scoreb = 1
        for i in black_sizes:
            scoreb = scoreb * i
    else:
        scoreb = 0

    if len(white_sizes) > 0:
        scorew = 1
        for i in white_sizes:
            scorew = scorew * i
    else:
        scorew = 0
    scores = [scorew, scoreb]
    return scores

def update_neighborsAI(stoneGroup, disc):
    tag = disc.tags
    for item in stoneGroup:
        for j in range(len(item.neighbours)):
            if item.neighbours[j].split(".")[1] == disc.tags.split(".")[1] and disc.tags not in item.occupied:
                item.occupied.append(disc.tags)
                for i in range(len(disc.neighbours)):
                    if disc.neighbours[i].split(".")[1] == item.tags.split(".")[1] and item.tags not in disc.occupied:
                        disc.occupied.append(item.tags)
