
class Algorithm(object):
    """ Template for all RL algorithms. It contains every function to interact with environment.
        This algorithm can
        1. take_action(state): choose how to take action when facing new state
        2. update(state, action, reward, new_state): use data collected from environment to update itself
        In each RL task, we can employ two algorithms. 
        One for exploration policy, which interact with environment, aiming at collecting as much useful data as possible.
        Another for learning policy, which learn from data, aiming at get the best performance when testing on environment.
    """
    def take_action(state):
        raise NotImplementedError
  
    def update(state, action, reward, next_state):
        raise NotImplementedError


