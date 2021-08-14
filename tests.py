import numpy as np
import main
import TicTacToe as ttt


def test1():
    # countPattern() test
    grid = np.array([
        [1, 0, 1],
        [2, 2, 2],
        [0, 1, 0]
    ])

    ttt.showGrid(grid)
    pattern = 2
    noOfPattern = 2
    print(f'Pattern with {noOfPattern} - {pattern} (X:1, O:2) in a line : ',
          main.countPattern(grid, noOfPattern, pattern))


def test2():
    # getHeuristic() test
    grid = np.array([
        [1, 0, 1],
        [2, 2, 2],
        [0, 0, 0]
    ])
    ttt.showGrid(grid)
    player = 1  # 1:X, 2:O
    move = (2, 1)
    print(f'Heuristic for move {move} is :',
          main.getHeuristic(grid, move, player))
    ttt.checkMoveAndPlace(grid, move, player)
    ttt.showGrid(grid)


test2()
