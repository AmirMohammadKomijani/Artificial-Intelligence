from abc import ABC, abstractmethod
from Constants import NO_OF_CELLS, BANNER_HEIGHT
from Utility import Node
import math


class Algorithm(ABC):

    def __init__(self, grid):
        self.grid = grid
        self.frontier = []
        self.explored_set = []
        self.path = []

    def get_initstate_and_goalstate(self, snake):
        return Node(snake.get_x(), snake.get_y()), Node(snake.get_fruit().x, snake.get_fruit().y)

    def manhattan_distance(self, nodeA, nodeB):
        distance_1 = abs(nodeA.x - nodeB.x)
        distance_2 = abs(nodeA.y - nodeB.y)
        return distance_1 + distance_2

    def euclidean_distance(self, nodeA, nodeB):
        distance_1 = nodeA.x - nodeB.x
        distance_2 = nodeA.y - nodeB.y
        return math.sqrt(distance_1**2 + distance_2**2)

    @abstractmethod
    def run_algorithm(self, snake):
        pass

    def get_path(self, node):
        if node.parent == None:
            return node

        while node.parent.parent != None:
            self.path.append(node)
            node = node.parent
        return node

    def inside_body(self, snake, node):
        for body in snake.body:
            if body.x == node.x and body.y == node.y:
                return True
        return False

    def outside_boundary(self, node):
        if not 0 <= node.x < NO_OF_CELLS:
            return True
        elif not BANNER_HEIGHT <= node.y < NO_OF_CELLS:
            return True
        return False

    def get_neighbors(self, node):
        i = int(node.x)
        j = int(node.y)

        neighbors = []
        # left [i-1, j]
        if i > 0:
            neighbors.append(self.grid[i-1][j])
        # right [i+1, j]
        if i < NO_OF_CELLS - 1:
            neighbors.append(self.grid[i+1][j])
        # top [i, j-1]
        if j > 0:
            neighbors.append(self.grid[i][j-1])

        # bottom [i, j+1]
        if j < NO_OF_CELLS - 1:
            neighbors.append(self.grid[i][j+1])

        return neighbors
    

    def CheckInsideOutside(self,snake,neighbor):
        if self.inside_body(snake, neighbor) or self.outside_boundary(neighbor):
            self.explored_set.append(neighbor)
    
    def DFS_Check(self,neighbor,neighbors,snake,presentLocation,FinalLocation):
        if not self.inside_body(snake, neighbor) and not self.outside_boundary(neighbor) and neighbor not in self.explored_set:
            neighbor.parent = presentLocation 
            path = self.returnToFirstDepth(
                snake, FinalLocation, neighbor) 
            if path != None:
                return path 

    def Best_F_Astar(self):
        price = 0
        for bestF in range(len(self.frontier)):
            if self.frontier[bestF].f < self.frontier[0].f:
                price = bestF
        return price
    

    def BestPathCheck(self,bestPath,neighbor,FinalLocation,leastCostNode,furtherCost):
            if neighbor not in self.frontier: 
                neighbor.h = self.manhattan_distance(FinalLocation, neighbor)
                self.frontier.append(neighbor)
                bestPath = True
            elif leastCostNode.g < neighbor.g: 
                bestPath = True  

            if bestPath:
                neighbor.parent = leastCostNode
                neighbor.g = furtherCost
                neighbor.f = neighbor.g + neighbor.h        
    
