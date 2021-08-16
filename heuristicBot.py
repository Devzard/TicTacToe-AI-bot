import TicTacToe as ttt
import numpy as np
import random


def randomPlayer(availableMoves):
    """
    returns a random move
    """
    return random.choice(availableMoves)


def countPattern(grid, count, pattern):
    """
    counts the number of rows with 'count' number of 'pattern'
    """
    rcno = [0, 1, 2]
    patternCount = 0
    totalCount = 0
    # vertical and horizontal
    for i in rcno:
        # for one line
        # checking the row
        patternCount = 0
        for j in rcno:
            if grid[i, j] != pattern and grid[i, j] != 0:
                patternCount = 0
                break
            if grid[i, j] == pattern:
                patternCount += 1
        if patternCount == count:
            totalCount += 1
        # checking the column
        patternCount = 0
        for j in rcno:
            if grid[j, i] != pattern and grid[j, i] != 0:
                patternCount = 0
                break
            if grid[j, i] == pattern:
                patternCount += 1
        if patternCount == count:
            totalCount += 1
    # diagonals
    posDia = 0
    negDia = 0
    for i in rcno:
        if grid[i, i] != pattern and grid[i, i] != 0:
            posDia = 4
        if grid[i, i] == pattern:
            posDia += 1
        if grid[i, 2-i] != pattern and grid[i, 2-i] != 0:
            negDia = 4
        if grid[i, 2-i] == pattern:
            negDia += 1
    if posDia == count:
        totalCount += 1
    if negDia == count:
        totalCount += 1

    return totalCount


def getHeuristic(grid, move, player):
    """
    places a move and checks heuristics.
    Heuristics : 
    100 : three pieces in a row,
    10 : two pieces in a row,
    -10 : two opponent pieces in a row,
    -100 : three opponent pieces in a row.
    """
    tempGrid = grid.copy()
    ttt.checkMoveAndPlace(tempGrid, move, player)
    noOf2 = countPattern(tempGrid, 2, player)
    noOf3 = countPattern(tempGrid, 3, player)
    noOf2Opp = countPattern(tempGrid, 2, (player % 2)+1)
    noOf3Opp = countPattern(tempGrid, 3, (player % 2)+1)
    heuristic = 0 + 10*noOf2 + 100*noOf3 + (-10*noOf2Opp) + (-100*noOf3Opp)
    return heuristic


def oslAgent(grid, availableMoves, player):
    """
    one-step-lookahead
    1. places all the available moves and get heurisitcs
    2. choose the move with highest heuristic
    3. return the move position
    """
    heuristics = dict(zip(availableMoves, [getHeuristic(
        grid, move, player) for move in availableMoves]))
    maxValue = max(heuristics.values())
    maxHeuristics = [key for key in heuristics.keys(
    ) if heuristics[key] == maxValue]
    return random.choice(maxHeuristics)


def getHeuristic2(grid, player):
    """
    checks heuristics.
    Heuristics : 
    100 : three pieces in a row,
    10 : two pieces in a row,
    -10 : two opponent pieces in a row,
    -100 : three opponent pieces in a row.
    """
    noOf2 = countPattern(grid, 2, player)
    noOf3 = countPattern(grid, 3, player)
    noOf2Opp = countPattern(grid, 2, (player % 2)+1)
    noOf3Opp = countPattern(grid, 3, (player % 2)+1)
    heuristic = 0 + 10*noOf2 + 100*noOf3 + (-10*noOf2Opp) + (-100*noOf3Opp)
    return heuristic


def minimax(grid, depth, move, isMaximizing, player):
    """
    if terminal node or depth = 0 then
        return the heuristic value of node
    if maximizing then
        value = -infinity
        for every child of node
            value = max(value, minimax(child, depth-1, minimizing))
        return value
    else 
        value = infinity
        for every child of node
            value = min(value, minimax(child, depth-1, maximizing))
        return value
    """
    available = [(i, j) for i in range(3)
                 for j in range(3) if grid[i, j] == 0]
    if ttt.gameOver(grid, player, False)[0] or depth == 1:
        return getHeuristic2(grid, player)
    if isMaximizing:
        value = -np.Inf
        for validMove in available:
            childGrid = grid.copy()
            ttt.checkMoveAndPlace(childGrid, validMove, player)
            value = max(value, minimax(
                childGrid, depth-1, validMove, False, player))
        return value
    else:
        value = np.Inf
        for validMove in available:
            childGrid = grid.copy()
            ttt.checkMoveAndPlace(childGrid, validMove, (player % 2) + 1)
            value = min(value, minimax(
                childGrid, depth - 1, validMove, True, player))
        return value


def nslScoreMove(steps, grid, move, player):
    """
    scores each move for nslAgent
    """
    tempGrid = grid.copy()
    ttt.checkMoveAndPlace(tempGrid, move, player)
    score = minimax(tempGrid, steps, move, False, player)
    return score


def nslAgent(steps, grid, availableMoves, player):
    """
    n-step-lookahead
    1. look n step ahead
    2. select the best move using minimax
    3. return the move position
    """
    # get scores for every available move using minimax
    # select the max scores
    # return a random move from max scores
    heuristics = dict(zip(availableMoves, [nslScoreMove(
        steps, grid, move, player) for move in availableMoves]))
    maxValue = max(heuristics.values())
    maxHeuristics = [key for key in heuristics.keys(
    ) if heuristics[key] == maxValue]
    return random.choice(maxHeuristics)


def main():
    grid = np.zeros((3, 3))
    availableMoves = [(r, c) for r in range(3) for c in range(3)]
    player1 = 1
    player2 = 2
    win1 = 0
    win2 = 0
    showGrid = True
    noOfMatches = 1
    for _ in range(noOfMatches):
        grid = np.zeros((3, 3))
        availableMoves = [(r, c) for r in range(3) for c in range(3)]
        if showGrid:
            ttt.showGrid(grid)
        while True:
            # p1Move = randomPlayer(availableMoves)
            # p1Move = oslAgent(grid, availableMoves, player1) # one-step-lookahead agent
            # n-step-lookahead agent
            # p1Move = nslAgent(5, grid, availableMoves, player1)
            p1Move = eval(input('>>Enter your move : '))
            availableMoves.pop(availableMoves.index(p1Move))
            gameStatus = ttt.gameMove(grid, p1Move, player1, showGrid)
            if not gameStatus[0]:
                if gameStatus[1] == 1:
                    win1 += 1
                break
            # p2Move = oslAgent(grid, availableMoves, player2) # one-step-lookahead agent
            # n-step-lookahead agent
            p2Move = nslAgent(3, grid, availableMoves, player2)
            availableMoves.pop(availableMoves.index(p2Move))
            gameStatus = ttt.gameMove(grid, p2Move, player2, showGrid)
            if not gameStatus[0]:
                if gameStatus[1] == 2:
                    win2 += 1
                break
    print(f'>> 1 wins : {win1}, 2 wins : {win2}')


if __name__ == '__main__':
    main()
