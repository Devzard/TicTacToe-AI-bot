# Tic-Tac-Toe AI bot

A bot for Tic-Tac-Toe that uses deep reinforcement learning trained using keras-rl **DQN agent**.

> All code in [`main.ipynb`](main.ipynb)

Trained weights are present in [`dqn_weights.h5f`](dqn_weights.h5f.index)

## Additional

1. A **PPO** agent built with stable-baselines.

   > All code in [`MlpPolicy.ipynb`](MlpPolicy.ipynb)

   A trained model with PPO1 of stable baselines is in [`PPO1_model`](PPO1_model.zip).  
   A trained model with PPO2 of stable baselines is in [`PPO2_model`](PPO2_model.zip).

2. A heuristic using bot. A **n-step-lookahead** bot which uses minimax algorithm to find the optimal move.

   ```python
   import heuristicBot
   ...
   move = heuristicBot.nslAgent(no_of_step_to_lookahead, game_grid, available_moves_on_grid, player_number)
   ...
   # returns a valid index to where the move should be made
   # PARAMETERS =>
   # no_of_step_to_lookahead = (max 9, min 1)
   # game_grid = a 9x9 2D numpy array with value 0:empty, 1:X, 2:O
   # available_moves_on_grid = list of all empty places on the grid
   # player_number = 1 or 2
   ```

## Requirements

numpy==1.19.4  
gym==0.18.3  
stable-baselines==2.10.2  
tensorflow==1.15.0  
tensorflow-gpu==1.15.0  
python==3.7  
keras-rl

by [Debashish Gogoi](https://github.com/Devzard)
