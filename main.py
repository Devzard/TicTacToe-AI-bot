import TicTacToe as ttt
import numpy as np
from random import randint


def randomPlayer(availableMoves):
    """
    returns a random move
    """
    move = randint(0, len(availableMoves)-1)
    pmove = availableMoves.pop(move)
    return pmove


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
    print(f'2:{noOf2}, 3:{noOf3}, o2:{noOf2Opp}, o3:{noOf3Opp}')
    heuristic = 0 + 10*noOf2 + 100*noOf3 + (-10*noOf2Opp) + (-100*noOf3Opp)
    return heuristic


def osaAgent(grid, availableMoves, player):
    """
    1. places all the available moves and get heurisitcs
    2. choose the move with highest heuristic
    """
    pass


def main():
    grid = np.zeros((3, 3))
    availableMoves = [(r, c) for r in range(3) for c in range(3)]
    player1 = 1
    player2 = 2
    while True:
        p1Move = randomPlayer(availableMoves)
        if not ttt.gameMove(grid, p1Move, player1):
            break
        p2Move = randomPlayer(availableMoves)
        if not ttt.gameMove(grid, p2Move, player2):
            break


if __name__ == '__main__':
    main()
