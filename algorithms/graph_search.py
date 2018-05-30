
class GraphSearch(algorithm):
  """GraphSearch is a naive RL algorithm that designed for deterministic goal-seeking env with continuous/discrete states and discrete actions.
     GraphSearch takes each state as a node, and each action at a edge that leads current states to next states.
     A current estimated distance from the goal state is kept in each state node, along with the current estimated best action.
     GraphSearch takes a sophiscated memory to store all the state, especially
     1. which states can reach current state in our historical record?
     GraphSearch will keep a dict to record the shortest distance and taken action.
     GraphSearch will also keep a policy network, which is trained by current estimated best action.
     As a result, GraphSearch will take action according to
     1. it's memory, and recorded best action
     2. it's policy network
  """
  def __init__(self):
    self.policy = LinearPolicyNetwork()
    self.memory = GraphMemory()
  
  def take_action(self, state):
  
  def update(self, state, action, reward, next_state, done):
  
  
