from . import rl_algorithm
import math
import numpy as np
import gym
import random
from collections import deque
from numpy import pi

class HeuristicDiscreteExploration(rl_algorithm.Algorithm):
    """Exploration algorithm for RL env with continous state and discrete action.
       This algorithm encourages actions that may lead to novel state.
       1. State novelty is calculated by a Gaussian Distribution of visited states in an exponential moving way.
       2. Action is selected by a bandit, assuming that each step will not change the states too much, and the bandit on those states are nearly the same.
       3. At the end of each episode, the gaussian distribution will be re-initialized, to summary the average statistic of last episode.
    """
    def __init__(self, state_dim, action_dim):
        self.ob_dim = state_dim
        self.ac_dim = action_dim
    
        self.state_mean = [0 for i in range(self.ob_dim)]
        self.state_variance = [0 for i in range(self.ob_dim)] # mean and variance to balance between each dimension
        self.state_meanx2 = [0 for i in range(self.ob_dim)]
        
        self.reward_mean = {}
        for i in range(self.ac_dim):
            self.reward_mean[i] = 0
        self.exploration = {}
        for i in range(self.ac_dim):
            self.exploration[i] = 100
    
        self.state = []
        self.state_mean_iter = []
        self.state_meanx2_iter = []

    def __reward_reset__(self):
        for i in range(self.ac_dim):
            self.reward_mean[i] = 0
        for i in range(self.ac_dim):
            self.exploration[i] = 100

    def __add_reward__(self, action, reward):
        """if we use >= 20 here, the algorithm will reach the goal much later. ==20 is much better. we donnot know why"""
        if self.exploration[action] == 20:
            self.reward_mean[action] = reward
        else:
            self.reward_mean[action] = self.reward_mean[action] * 0.8 + reward * 0.2
        for i in range(self.ac_dim): self.exploration[i] = self.exploration[i] + 1  # If you haven't take an action for a long time, we will increase its probability
        self.exploration[action] = 1
  
    def __difference_reward__(self, new_state):
        """ 
           How novel is new state?
           (s-mean)/cov, we want the state to be different, according to current distribution.
        """

        state = self.__norm__(new_state)
        return sum([abs(state[i]) for i in range(len(state))])

    def __norm__(self, state):
        if self.state_mean == [0 for i in range(self.ob_dim)] or self.state_variance == [0.0001 for i in range(self.ob_dim)]: return state
        return [(state[i] - self.state_mean[i])/self.state_variance[i] for i in range(len(state))]

    def __statistic_exp__(self, x):
        self.state_mean = [0.99 * self.state_mean[i] + 0.01 * x[i] for i in range(len(x))]
        self.state_meanx2 = [0.99 * self.state_meanx2[i] + 0.01 * x[i] * x[i] for i in range(len(x))]
        self.state_variance = [0.0001 + math.sqrt(self.state_meanx2[i] - self.state_mean[i] * self.state_mean[i]) for i in range(len(x))]
        self.state.append(x)

    def __statistic_iter__(self):
        mean = [0 for i in range(self.ob_dim)]
        meanx2 = [0 for i in range(self.ob_dim)]
        n = len(self.state)
        for state in self.state:
            mean = [mean[i] + state[i]/n for i in range(self.ob_dim)]
            meanx2 = [meanx2[i] + state[i]*state[i]/n for i in range(self.ob_dim)]
        self.state_mean_iter.append(mean)
        self.state_meanx2_iter.append(meanx2)
        self.state = []

        m = [0 for i in range(self.ob_dim)]
        mx2 = [0 for i in range(self.ob_dim)]
        n = len(self.state_mean_iter)
        for mean in self.state_mean_iter:
            m = [m[i] + mean[i]/n for i in range(self.ob_dim)]
        for meanx2 in self.state_meanx2_iter:
            mx2 = [mx2[i] + meanx2[i]/n for i in range(self.ob_dim)]
        self.state_mean = m
        self.state_meanx2 = mx2
        #print("Episode Begin with mean state:"+str(self.state_mean))
  
    def take_action(self, state):
        """
           Take action with a bandit based on pseudo reward.
           Todo: change it to an policy based on exponential record
        """
        Qs = [self.reward_mean[i] if self.exploration[i] < 20 else math.inf for i in range(self.ac_dim)]
        #print(Qs)
        Q = max(Qs)
        answer = [i for i, j in enumerate(Qs) if j == Q]
        return answer[0]
  
    def update(self, state, action, reward, next_state, done):
        self.__statistic_exp__(next_state)
        pseudo_reward = self.__difference_reward__(next_state)
        self.__add_reward__(action, pseudo_reward)
        if done:
            self.__reward_reset__()
            self.__statistic_iter__()
