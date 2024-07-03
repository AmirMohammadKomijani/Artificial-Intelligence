from Algorithm import Algorithm


class A_STAR(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):

        self.frontier = []
        self.explored_set = []

        FirstLocation, FinalLocation = self.get_initstate_and_goalstate(snake)

        # open list
        self.frontier.append(FirstLocation)

        # while we have states in open list
        while len(self.frontier) > 0:

            price = self.Best_F_Astar()

            leastCostNode = self.frontier.pop(price)

            # check if its goal state
            if leastCostNode.equal(FinalLocation):
                return self.get_path(leastCostNode)

            self.explored_set.append(leastCostNode)
            neighbors = self.get_neighbors(leastCostNode)


            for neighbor in neighbors:
                
                if self.inside_body(snake, neighbor) or self.outside_boundary(neighbor) or neighbor in self.explored_set:
                    continue 

                furtherCost = leastCostNode.g + 1
                bestPath = False 

                self.BestPathCheck(bestPath,neighbor,FinalLocation,leastCostNode,furtherCost)
                
        return None