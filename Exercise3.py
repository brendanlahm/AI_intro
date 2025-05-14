# Markov Deterministic Probability

class MDP(object):
    def __init__(self):
        pass
    states = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    actions = {
    1: ('r', 'd'),
    2: ('r', 'd', 'l'),
    3: ('l', 'd'),
    4: ('u', 'r', 'd'),
    5: ('u', 'r', 'd', 'l'),
    6: ('u', 'd', 'l'),
    7: ('u', 'r'),
    8: ('u', 'r', 'l'),
    9: ('u', 'l')
}
    def getSuccessorProbReward(self, state, action):
        spr = {
            1: {'r': [(2, 1.0, -1)], 'd': [(4, 1.0, -1)]}
        }
        pass
    def getActions(self):
        return(self.actions)






mdp = MDP()




