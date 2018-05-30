
class PolicyNetwork(obj):
  """PolicyNetwork maps state to action, and can be trained by (state, action, reward/value) tuples or by gradient in a DDPG way.
     PolicyNetwork can be called in the following ways:
     1. generate_action
         a. with randomness in parameter or action
         b. stochastic policy, return a distribution on actions
         c. deterministic policy, return an action
     2. update
         a. by (state, action, reward/value) data tuples
         b. by gradient from ValueNetwork, such as in DDPG.
   """
   
   def generate_action(self, state):
     raise NotImplementedError

   
   def update(self, state, action, weight):
     raise NotImplementedError
