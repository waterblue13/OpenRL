
class ValueNetwork(object):
  """ ValueNetwork is used to keep record of the estimated value of each state, action pair under certain policy"""

  def get_value(self, state, action):
    raise NotImplementedError
  
  def get_value(self, state):
    raise NotImplementedError
    
  def update(self, state, action, reward, next_state):
    raise NotImplementedError
    
  def batch_update(self, batch_data):
    raise NotImplementedError
