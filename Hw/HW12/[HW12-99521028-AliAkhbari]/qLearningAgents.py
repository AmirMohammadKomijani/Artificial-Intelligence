from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import gridworld

import random,util,math
import copy

class QLearningAgent(ReinforcementAgent):
    
    def __init__(self, **args):

        ReinforcementAgent.__init__(self, **args)
        self.qvalues = util.Counter()

    def getQValue(self, state, action):
        
        return self.qvalues[(state,action)]

    def computeValueFromQValues(self, state):
        
        actions = self.getLegalActions(state)
        if len(actions) == 0:
          return 0
        else:
          return max([self.getQValue(state,action) for action in actions])
        
    def computeActionFromQValues(self, state):
       
        actions = self.getLegalActions(state)
        stateMaxQValue = self.computeValueFromQValues(state)
        maxAction = []
        if len(actions) == 0:
          return None
        maxAction = [action for action in actions if self.getQValue(state, action) == stateMaxQValue]
        return random.choice(maxAction)

    def getAction(self, state):
    
        legalActions = self.getLegalActions(state)
        action = None
        if util.flipCoin(self.epsilon) == True:
          action = random.choice(legalActions)
        else:
          action = self.computeActionFromQValues(state)
        return action

    def update(self, state, action, nextState, reward):

        qValueState = self.getQValue(state,action)
        qValueNextState = self.computeValueFromQValues(nextState)
        self.qvalues[(state,action)] = (1 - self.alpha) * qValueState + self.alpha * (reward + self.discount*(qValueNextState)- qValueState)
        
    def getPolicy(self, state):

        return self.computeActionFromQValues(state)

    def getValue(self, state):
        
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1
        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action

class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent
       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def update(self, state, action, nextState, reward: float):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def final(self, state):
        """Called at the end of each game."""
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass
