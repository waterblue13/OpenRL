import gym
from algorithms.heuristic_discrete_exploration import HeuristicDiscreteExploration

def main():
    # initialization
    env_name = "MountainCar-v0"
    random_seed = 1234
    env = gym.make(env_name)
    env.seed(random_seed)
    num_episodes = 100
    exploration_policy = HeuristicDiscreteExploration(state_dim = env.observation_space.shape[0], action_dim = env.action_space.n)
  #  learning_policy = GraphSearch(state_dim = env.observation_space.shape[0], action_dim = env.action_space.n)
    
    # training
    for episode in range(num_episodes):
        state = env.reset()
        for step in range(200):
            action = exploration_policy.take_action(state)
            next_state, reward, done, _ = env.step(action)
            exploration_policy.update(state, action, reward, next_state, done)
  #          learning_policy.update(state, action, reward, next_state, done)
            next_state = state
            if done: 
                if step < 199: 
                    print("reach goal in "+ str(step)+" steps!")
                break
        
    # testing
  #  accumulated_reward = 0
  #  state = env.reset()
  #  while true:
  #    action = learning_policy.take_action(state)
  #    next_state, reward, done, _ = self.env.step(action)
  #    accumulated_reward += reward
  #    next_state = state

if __name__ == "__main__":
    main()
