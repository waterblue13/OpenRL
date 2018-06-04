from . import memory

class GraphMemory(memory.Memory):
    """GraphMemory to store the relation(connected action) between states"""

    def __init__(self):
        
        self.predecessor = {} # key: next_state, value:[state, action, reward]


    def add(self, state, action, reward, next_state):
        #print("add data:" + str(state) + " " + str(action) + " " + str(reward) + " " + str(next_state))
        if next_state in self.predecessor:
            self.predecessor[next_state].add((state, action, reward))
        else:
            self.predecessor[next_state] = set([(state, action, reward)])
        #print("after adding:" + str(self.predecessor))

    def get(self, next_states): #next_states, a set of next_state
        result = set([])
        for next_state in next_states:
            if next_state in self.predecessor:
           #     print("state" + str(next_state))
           #     print("not in memory" + str(self.predecessor))
                for state, action, reward in self.predecessor[next_state]:
                    result.add((state, action, reward, next_state))
        return result

#graph_memory = GraphMemory()
#graph_memory.add(1, 1, -1, 2)
#graph_memory.add(3, 2, -1, 2)
#print(graph_memory.get([2]))
