# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random
import util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """

        legalMoves = gameState.getLegalActions()


        scores = [self.evaluationFunction(
            gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(
            len(scores)) if scores[index] == bestScore]

        chosenIndex = random.choice(bestIndices)

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):

        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [
            ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        pacLastFood = currentGameState.getFood()
        PresentPosition = list(successorGameState.getPacmanPosition())
        maxDistance = -10000000

        dis = 0
        lsFoods = pacLastFood.asList()

        if action == 'Stop':
            return maxDistance
        
        for state in newGhostStates:
            if state.getPosition() == tuple(PresentPosition) and (state.scaredTimer == 0):
                return maxDistance 
        
        for food in lsFoods:
            dis = -1 *(manhattanDistance(food, PresentPosition))

            if (dis > maxDistance):
                maxDistance = dis

        return maxDistance



def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)
        self.nodesCount = 0


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        
        with open('MinimaxAgent.txt', 'a') as f:
            f.write(f"\n {self.nodesCount}")
            
        "*** YOUR CODE HERE ***"
        def minMaxHelper(gameState, depth, agent):
            if agent >= gameState.getNumAgents():
                agent = 0
                depth += 1
            if gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            if depth==self.depth:
                return self.evaluationFunction(gameState)
            elif (agent == 0):
                return maxFinder(gameState, depth, agent)
            else:
                return minFinder(gameState, depth, agent)
        

        def maxFinder(gameState, depth, agent):
            result = ["meow", -float("inf")]
            pacMovesList = gameState.getLegalActions(agent)
            
            if not pacMovesList:
                return self.evaluationFunction(gameState)
                
            for move in pacMovesList:
                presentState = gameState.generateSuccessor(agent, move)
                presentPoint = minMaxHelper(presentState, depth, agent+1)
                if type(presentPoint) is list:
                    temp = presentPoint[1]
                else:
                    temp = presentPoint
                if temp > result[1]:
                    result = [move, temp]                    
            return result
            
        def minFinder(gameState, depth, agent):
            result = ["meow", float("inf")]
            ghostActions = gameState.getLegalActions(agent)
            
            if not ghostActions:
                return self.evaluationFunction(gameState)
                
            for move in ghostActions:
                presentState = gameState.generateSuccessor(agent, move)
                presentPoint = minMaxHelper(presentState, depth, agent+1)
                if type(presentPoint) is list:
                    temp = presentPoint[1]
                else:
                    temp = presentPoint
                if temp < result[1]:
                    result = [move, temp]
            return result

        resList = minMaxHelper(gameState, 0, 0)
        return resList[0]    



class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        with open('AlphaBetaAgent.txt', 'a') as f:
            f.write(f"\n {self.nodesCount}")
        "*** YOUR CODE HERE ***"

        def minMaxHelper(gameState, depth, agent, alpha, beta):
            if agent >= gameState.getNumAgents():
                agent = 0
                depth += 1
            if (depth==self.depth or gameState.isWin() or gameState.isLose()):
                return self.evaluationFunction(gameState)
            elif (agent == 0):
                return maxFinder(gameState, depth, agent, alpha, beta)
            else:
                return minFinder(gameState, depth, agent, alpha, beta)
        
        def maxFinder(gameState, depth, agent, alpha, beta):
            result = ["meow", -float("inf")]
            agentMovesList = gameState.getLegalActions(agent)
            
            if not agentMovesList:
                return self.evaluationFunction(gameState)
                
            for move in agentMovesList:
                presentLocation = gameState.generateSuccessor(agent, move)
                presentPoint = minMaxHelper(presentLocation, depth, agent+1, alpha, beta)
                
                if type(presentPoint) is list:
                    temp = presentPoint[1]
                else:
                    temp = presentPoint
                    
                #real logic
                if temp > result[1]:
                    result = [move, temp]
                if temp > beta:
                    return [move, temp]
                alpha = max(alpha, temp)
            return result
            
        def minFinder(gameState, depth, agent, alpha, beta):
            result = ["meow", float("inf")]
            ghostActions = gameState.getLegalActions(agent)
           
            if not ghostActions:
                return self.evaluationFunction(gameState)
                
            for action in ghostActions:
                presentLocation = gameState.generateSuccessor(agent, action)
                presentPoint = minMaxHelper(presentLocation, depth, agent+1, alpha, beta)
                
                if type(presentPoint) is list:
                    temp = presentPoint[1]
                else:
                    temp = presentPoint
                    
                    
                if temp < result[1]:
                    result = [action, temp]
                if temp < alpha:
                    return [action, temp]
                beta = min(beta, temp)
            return result
             
        resultList = minMaxHelper(gameState, 0, 0, -float("inf"), float("inf"))
        return resultList[0]

 


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        def expHelper(gameState, depth, agent):
            if agent >= gameState.getNumAgents():
                agent = 0
                depth += 1
            if (depth==self.depth or gameState.isWin() or gameState.isLose()):
                return self.evaluationFunction(gameState)
            elif (agent == 0):
                return maxFinder(gameState, depth, agent)
            else:
                return expFinder(gameState, depth, agent)
        
        def maxFinder(gameState, depth, agent):
            reslut = ["meow", -float("inf")]
            agentMovesList = gameState.getLegalActions(agent)
            
            if not agentMovesList:
                return self.evaluationFunction(gameState)
                
            for move in agentMovesList:
                presentLocation = gameState.generateSuccessor(agent, move)
                presentPoint = expHelper(presentLocation, depth, agent+1)
                if type(presentPoint) is list:
                    temp = presentPoint[1]
                else:
                    temp = presentPoint
                if temp > reslut[1]:
                    reslut = [move, temp]                    
            return reslut
            
        def expFinder(gameState, depth, agent):
            reslut = ["meow", 0]
            ghostMoves = gameState.getLegalActions(agent)
            
            if not ghostMoves:
                return self.evaluationFunction(gameState)
                
            prob = 1.0/len(ghostMoves)    
                
            for move in ghostMoves:
                presentLocation = gameState.generateSuccessor(agent, move)
                presentPoint = expHelper(presentLocation, depth, agent+1)
                if type(presentPoint) is list:
                    val = presentPoint[1]
                else:
                    val = presentPoint
                reslut[0] = move
                reslut[1] += val * prob
            return reslut
             
        reslutList = expHelper(gameState, 0, 0)
        return reslutList[0]  


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    FoodLocation = currentGameState.getFood().asList() 
    DistaceFromFood = [] 
    ghostStates = currentGameState.getGhostStates() 
    capPos = currentGameState.getCapsules()  
    PresentLocation = list(currentGameState.getPacmanPosition()) 
 
    for food in FoodLocation:
        foodDistanceagent = manhattanDistance(food, PresentLocation)
        DistaceFromFood.append(-1*foodDistanceagent)
        
    if not DistaceFromFood:
        DistaceFromFood.append(0)

    return max(DistaceFromFood) + currentGameState.getScore() 


# Abbreviation
better = betterEvaluationFunction
