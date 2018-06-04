import gym


class Env(object):

    def __init__(self, env_name):
        self.env = gym.make(env_name)
        self.observation_space = self.env.observation_space
        self.action_space = self.env.action_space

    def seed(self, seed):
        self.env.seed(seed)

    def reset(self):
        state = self.env.reset()
        state = tuple(list(state))
        return state

    def step(self, action):
        next_state, reward, done, _ = self.env.step(action)
        next_state = tuple(list(next_state))
        return next_state, reward, done, _
