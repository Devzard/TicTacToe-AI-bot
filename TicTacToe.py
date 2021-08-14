import numpy as np

# 0: empty space, 1:'X', 2:'O'
patternList = ['_', 'X', 'O']


def showGrid(grid):
    for row in grid:
        for column in row:
            print('|', end=' ')
            if column == 1:
                print(patternList[1], end=' ')
            elif column == 2:
                print(patternList[2], end=' ')
            else:
                print(patternList[0], end=' ')
            print('|', end='')
        print()


def checkMoveAndPlace(grid, move, pattern):
    """
    Check if a move is valid and puts it if it is.
    Returns True for valid move and False if not.
    """
    # edge cases
    if (move[0] > 2 or move[1] > 3) or (move[0] < 0 or move[1] < 0):
        print('>> Invalid index.')
        return False
    # can't place move in already occupied place
    if grid[move] != 0:
        print('>> Invalid move.')
        return False
    grid[move] = pattern
    return True


def gridScore(grid):  # returns-> -1:continue, 0:draw, 1:win
    """
    Checks if the grid is completed.
    If yes it is a draw(returns 0) or win(returns 1)
    else the game should continue(returns -1)
    """
    if 0 not in grid:
        return 0
    rcno = [0, 1, 2]
    # checking for rows and column condition
    for i in rcno:
        if grid[i, 0] == grid[i, 1] == grid[i, 2] != 0:
            return 1
        elif grid[0, i] == grid[1, i] == grid[2, i] != 0:
            return 1
    # checking for diagonals
    if grid[0, 0] == grid[1, 1] == grid[2, 2] != 0:
        return 1
    elif grid[0, 2] == grid[1, 1] == grid[2, 0] != 0:
        return 1
    return -1


def gameOver(grid, player):
    """
    Checks if a game is (won or drawn)(returns True) 
    or it should continue(returns False)
    """
    res = gridScore(grid)
    if res == -1:
        print('>> Continue.')
        return False
    elif res == 0:
        print('>> Game draw.')
        return True
    elif res == 1:
        print('>>', player, 'wins.')
        return True


def gameMove(grid, move, player):
    """
    Used to pass moves to the grid.
    returns False if any error occurs else True.
    """
    print('>>', player, 'move')
    if not checkMoveAndPlace(grid, move, player):
        return False
    showGrid(grid)
    if gameOver(grid, player):
        return False
    print('---------------------')
    return True


def main():
    grid = np.zeros((3, 3))
    player1 = 1
    player2 = 2
    showGrid(grid)
    while True:
        player1inp = eval(input("Enter your move (p1) : "))
        if not gameMove(grid, player1inp, player1):
            break
        player2inp = eval(input("Enter your move (p2) : "))
        if not gameMove(grid, player2inp, player2):
            break


if __name__ == '__main__':
    main()
