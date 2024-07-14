from collections import Counter
from random import randrange


class NQueens:
    def __init__(self, N):
        self.N = N

    def initial(self):
        ''' Returns a random initial state '''
        return tuple(randrange(self.N) for i in range(self.N))

    def goal_test(self, state):
        ''' Returns True if the given state is a goal state '''
        shu, pie, na = (set() for i in range(3))
        for row, col in enumerate(state):
            if col in shu or row - col in pie or row + col in na:
                return False
            shu.add(col)
            pie.add(row - col)
            na.add(row + col)
        return True

    def value(self, state):
        ''' Returns the value of a state. The higher the value, the closest to a goal state '''
        shu, pie, na = [Counter() for i in range(3)]
        for row, col in enumerate(state):
            shu[col] += 1
            pie[row - col] += 1
            na[row + col] += 1
        clashes = 0
        for cnt in [shu, pie, na]:
            for key in cnt:
                clashes += cnt[key] * (cnt[key] - 1) // 2
        return -clashes

    def neighbors(self, state):
        ''' Returns all possible neighbors (next states) of a state '''
        neighbors = []
        for row in range(self.N):
            for col in range(self.N):
                if col != state[row]:
                    neighbor = list(state)
                    neighbor[row] = col
                    neighbors.append(tuple(neighbor))
        return neighbors
