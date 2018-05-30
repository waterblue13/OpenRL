
class Memory(object):
    """This class is used to manage the memory of collected data.
       It can be organized in all fancy ways, such as a tree, a priority queue, or simple a stack.
       We can get access to data with Memory.
       The data updaing order is what we concerned in Memory.
       As a result, this is where topological structure of states, and sequential nature of states play their role.
    """
  
    def get_data(self, size):
        raise NotImplementedError
