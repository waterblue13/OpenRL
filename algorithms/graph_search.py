from . import rl_algorithm
from ..memory import graph_memory
from ..networks import linear_policy_network
from ..utils import dformat

class GraphSearch(rl_algorithm.Algorithm):
    """GraphSearch is a naive RL algorithm that designed for deterministic goal-seeking env with continuous/discrete states and discrete actions.
       GraphSearch takes each state as a node, and each action at a edge that leads current states to next states.
       A current estimated distance (of the shortest path) from the goal state is kept each state node
       GraphSearch takes a sophiscated memory to store all the state, especially
       1. which states can reach current state in our historical record?

    """
    def __init__(self, state_dim, action_dim):
        self.memory = graph_memory.GraphMemory()
        self.distance = {}  # key: state, value: an estimation of the shortest path to goal state
        self.best_action = {} # all the goal states that we meet 
        self.round_num = 4  # round number is 2

    def take_action(self, state):
        return None

    def round(self, state, action, reward, next_state):
        """to-dos"""
        round_state = dformat(state, self.round_num)
        round_next_state = dformat(next_state, self.round_num)
        return round_state, action, reward, round_next_state

    def update(self, state, action, reward, next_state, done):
        state, action, reward, next_state = self.round(state, action, reward, next_state)
        self.memory.add(state, action, reward, next_state)
        if done:
            self.distance[next_state] = 0
            states = set([next_state])
            print("states:" + str(states))
            while states:
                data = self.memory.get(states)
                #print("data:" + str(data))
                states = set([])
                for state, action, reward, next_state in data:
                    states.add(state) # we use state to query its next round pre-state
                    if state not in self.distance or self.distance[state] > self.distance[next_state] + 1:
                        self.distance[state] = self.distance[next_state] + 1
                        print("updating state:" + str(state))
                        print("updated distance: " + str(self.distance[state]))
                        self.best_action[state] = action
