def abNegamax(board, maxDepth, currentDepth, alpha, beta):

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
        recursedScore, currentMove = abNegamax(newBoard, maxDepth, currentDepth+1, -beta, -max(alpha, bestScore))

        currentScore = -recursedScore

        #Update the best Score
        if currentScore > bestScore:
            bestScore = currentScore
            bestMove = move

            # if we're outside the bounds, then prune: exit immediately
            if bestScore >= beta:
                return bestScore, bestMove

    return bestScore, bestMove


def getBestMove(board, maxDepth):

    # Get the result of a minimax run and return the move
    score, move = abNegamax(board, maxDepth, 0, -float('inf'), float('inf'))
    return move
