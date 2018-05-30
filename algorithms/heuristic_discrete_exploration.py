class HeuristicDiscreteExploration(algorithm):
  """Exploration algorithm for RL env with continous state and discrete action.
     This algorithm encourages actions that may lead to novel state.
     1. State novelty is calculated by a Gaussian Distribution of visited states in an exponential moving way.
     2. Action is selected by a bandit, assuming that each step will not change the states too much, and the bandit on those states are nearly the same.
     3. At the end of each episode, the gaussian distribution will be re-initialized, to summary the average statistic of last episode.
  """
  
  def __init__(self):
  
  def take_action(self, state):
  
  def update(self, state, action, reward, next_state, done):
