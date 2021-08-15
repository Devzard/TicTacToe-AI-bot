import numpy as np
import heuristicBot
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
          heuristicBot.countPattern(grid, noOfPattern, pattern))


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
    heuristic = heuristicBot.getHeuristic(grid, move, player)
    print(f'Heuristic for move {move} is :',
          heuristic)
    print(type(heuristic))
    ttt.checkMoveAndPlace(grid, move, player)
    ttt.showGrid(grid)


def test3():
    # oslaAgent() test
    grid = np.array([
        [1, 0, 1],
        [2, 0, 2],
        [0, 0, 0]
    ])
    ttt.showGrid(grid)
    player = 1  # 1:X, 2:O
    am = [(i, j) for i in range(3) for j in range(3) if grid[i, j] == 0]
    print(f'Heuristics for player {player} is : ',
          heuristicBot.oslaAgent(grid, am, player))


def test4():
    # minimax() test
    grid = np.array([
        [1, 0, 1],
        [2, 0, 2],
        [0, 1, 2]
    ])
    ttt.showGrid(grid)
    move = (2, 1)
    player = 1  # 1:X, 2:O
    print(
        f'Minimax value is : {heuristicBot.minimax(grid, 3, move, False, player)}')


def test5():
    # nslAgent() test
    grid = np.array([
        [1, 2, 1],
        [2, 1, 2],
        [0, 0, 2]
    ])
    ttt.showGrid(grid)
    move = (2, 1)
    player = 1  # 1:X, 2:O
    am = [(i, j) for i in range(3) for j in range(3) if grid[i, j] == 0]
    nslMove = heuristicBot.nslAgent(3, grid, am, player)
    print(f'Nsl agent move : {nslMove}')


test5()
