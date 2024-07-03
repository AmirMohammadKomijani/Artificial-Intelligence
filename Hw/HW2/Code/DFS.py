from Utility import Node
from Algorithm import Algorithm


class DFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def returnToFirstDepth(self, snake, FinalLocation, presentLocation):

        if presentLocation.equal(FinalLocation):
            return self.get_path(presentLocation)

        if presentLocation in self.explored_set:
            return None

        self.explored_set.append(presentLocation) 
        neighbors = self.get_neighbors(presentLocation) 


        for neighbor in neighbors:
            self.DFS_Check(neighbor,neighbors,snake,presentLocation,FinalLocation)

        return None

    def run_algorithm(self, snake):

        if len(self.path) != 0:

            path = self.path.pop()

            if self.inside_body(snake, path):
                self.path = [] 
            else:
                return path

        self.frontier = []
        self.explored_set = []

        initialstate, FinalLocation = self.get_initstate_and_goalstate(snake)
        self.frontier.append(initialstate)
        return self.returnToFirstDepth(snake, FinalLocation, initialstate)