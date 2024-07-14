import random


def hill_climbing(problem):
    ''' Returns a state as the solution of the problem '''
    current = problem.initial()
    while True:
        neighbours = problem.neighbors(current)
        if not neighbours:
            break
        neighbour = max(neighbours,
                key=lambda state: (problem.value(state), random.random()))
        if problem.value(neighbour) <= problem.value(current):
            break
        current = neighbour
    return current

def hill_climbing_random_restart(problem, limit = 10):
    state = problem.initial()
    cnt = 0
    while problem.goal_test(state) == False and cnt < limit:
        state = hill_climbing(problem)
        cnt += 1
    return state
