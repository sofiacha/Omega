def negamax(board, maxDepth, currentDepth):

    # Check if we're done recursing
    if board.isGameOver() or currentDepth == maxDepth:
        return board.evaluate(), None

    # Otherwise bubble up values from below
    bestMove = None
    bestScore = -float('inf')

    # Go through each move
    for move in board.getMoves():
        newBoard = board.makeMove(move)

        # Recurse
        recursedScore, currentMove = negamax(newBoard, maxDepth, currentDepth+1)

        currentScore = -recursedScore

        # Update the best score
        if currentScore > bestScore:
            bestScore = currentScore
            bestMove = move

    # Return the score and the best move
    return bestScore, bestMove

def getBestMoveNM(board, maxDepth):
    #get the result of a minimax run and return the move
    score, move = negamax(board, maxDepth, 0)
    return move