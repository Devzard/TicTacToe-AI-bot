import TicTacToe as ttt
import heuristicBot
import numpy as np


def mark_piece(grid, index, player):
    """
    1. places a move by the RL agent
    2. check if invalid
    3. if not check if agent won
    4. if not place move by opponent
    5. check if opponent won
    6. return respective code at appropiate step
    returns -2:continue, -1:invalid move, 
            1:1 wins, 2:2 wins, 0:draw
    """
    if grid[index] != 0:
        return -1, grid
    else:
        grid[index] = player
        score = ttt.gridScore(grid)
        if score != -1 and score == 1:
            return player, grid
        elif score != -1:
            return 0, grid
        # opponent agent : a n-step-lookahead bot
        available_moves = [(i, j) for i in range(3)
                           for j in range(3) if grid[i, j] == 0]
        opp_player = (player % 2) + 1
        opp_move_idx = heuristicBot.nslAgent(
            2, grid, available_moves, opp_player)
        grid[opp_move_idx] = opp_player
        score = ttt.gridScore(grid)
        if score != -1 and score == 1:
            return opp_player, grid
        elif score != -1:
            return 0, grid
        return -2, grid


def test1():
    grid = np.array([
        [1, 2, 1],
        [2, 1, 2],
        [0, 2, 0]
    ])
    ttt.showGrid(grid)
    move = (2, 0)
    player = 1  # 1:X, 2:O
    res, ngrid = mark_piece(grid, move, player)
    print(res)
    ttt.showGrid(ngrid)


test1()
