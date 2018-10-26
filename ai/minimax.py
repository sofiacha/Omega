def minimax(board, player, maxDepth, currentDepth):
    #check if we are done recursing
    if board.isGameOver() or currentDepth == maxDepth:
        return board.evaluate(player), None

    #otherwise bubble up values from below
    bestMove = None
    if board.currentPlayer() == player: bestScore = -float('inf')
    else: bestScore = float('inf')

    #Go through each move
    for move in board.getMoves():
        newBoard = board.makeMove(move)
        #Recurse
        currentScore, currentMove = minimax(newBoard, newBoard.player, maxDepth, currentDepth+1)
        #Update the best score
        if board.currentPlayer() == player:
            if currentScore > bestScore:
                bestScore = currentScore
                bestMove = move
        else:
            if currentScore < bestScore:
                bestScore = currentScore
                bestMove = move
    #Return the score and the best move
    return bestScore, bestMove

def getBestMove(board, player, maxDepth):
    #get the result of a minimax run and return the move
    score, move = minimax(board, player, maxDepth, 0)
    return move