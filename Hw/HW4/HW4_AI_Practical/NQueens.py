import random
from random import randrange
from collections import Counter


# source : https://github.com/vitorverasm/ai-nqueens/blob/master/NQueens.py

class NQueens:
    def __init__(self, N):
        self.N = N

    def initial(self):
        ''' Returns a random initial state '''
        return tuple(randrange(self.N) for i in range(self.N))

    def goal_test(self, state):
        ''' Returns True if the given state is a goal state '''
        st1, st2, st3 = (set() for i in range(3))
        for row, col in enumerate(state):
            if col in st1 or row - col in st2 or row + col in st3:
                return False
            st1.add(col)
            st2.add(row - col)
            st3.add(row + col)
        return True

    def value(self, state):
        ''' Returns the value of a state. The higher the value, the closest to a goal state '''

        st1, st2, st3 = [Counter() for i in range(3)]

        for row, col in enumerate(state):
            st1[col] += 1
            st2[row - col] += 1
            st3[row + col] += 1
        val = 0

        for count in [st1, st2, st3]:
            for key in count:
                val += count[key] * (count[key] - 1) / 2
        return -val
    

    def neighbors(self, state):
        ''' Returns all possible neighbors (next states) of a state '''
        resList = []
        for row in range(self.N):
            for col in range(self.N):
                if col != state[row]:
                    aux = list(state)
                    aux[row] = col 
                    resList.append(list(aux)) 
        return resList