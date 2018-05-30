import gym
from algorithms import HeuristicDiscreteExploration, GraphSearch

def main():
  # initialization
  env_name = "MountainCar-v0"
  random_seed = 1234
  num_episodes = 100
  exploration_policy = HeuristicDiscreteExploration(state_dim = env.observation_space.shape[0], ac_dim = env.action_space.n)
  learning_policy = GraphSearch(state_dim = env.observation_space.shape[0], ac_dim = env.action_space.n)
  
  # training
  env = gym.make(env_name)
  env.seed(random_seed)
  for episode in range(num_episodes):
    state = env.reset()
    while true:
      action = exploration_policy.take_action(state)
      next_state, reward, done, _ = self.env.step(action)
      exploration_policy.update(state, action, reward, next_state, done)
      learning_policy.update(state, action, reward, next_state, done)
      next_state = state
      if done: break
      
  # testing
  accumulated_reward = 0
  state = env.reset()
  while true:
    action = learning_policy.take_action(state)
    next_state, reward, done, _ = self.env.step(action)
    accumulated_reward += reward
    next_state = state

if __name__ == "__main__":
  main()
