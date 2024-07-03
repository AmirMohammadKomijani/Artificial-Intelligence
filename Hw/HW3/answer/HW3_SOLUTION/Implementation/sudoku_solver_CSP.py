from array import array
import time
import copy
# import sys
# sys.setrecursionlimit(200000)

class SudokuSolverCSP:
    def __init__(self, dim, board):
        self.board = board
        self.dim = dim
        self.expandedNodes = 0
        self.rv = self.getRemainingValues() # RV = Remaining Values

    # def __init__(self, dim, fileDir):
    #     self.dim = dim
    #     self.expandedNodes = 0
    #     with open(fileDir) as f:
    #         content = f.readlines()
    #         self.board = [list(x.strip()) for x in content] # split
    #     self.rv = self.getRemainingValues() # RV = Remaining Values

    def getDomain(self, row, col):
        RVCell = [str(i) for i in range(1, self.dim+1)] # RVCell = Remaining Values Cell = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(self.dim):
            if self.board[row][i] != '0': # check row if there is any value (not empty)
                if self.board[row][i] in RVCell: # if the value is in the domain
                    RVCell.remove(self.board[row][i]) # remove it from the domain
        for i in range(self.dim):
            if self.board[i][col] != '0':
                if self.board[i][col] in RVCell:
                    RVCell.remove(self.board[i][col])
        boxRow = row - (row % 3) # get the top left corner of the box
        boxCol = col - (col % 3) 
        for i in range(boxRow, boxRow+3):
            for j in range(boxCol, boxCol+3):
                if self.board[i][j] != '0':
                    if self.board[i][j] in RVCell:
                        RVCell.remove(self.board[i][j])
        return RVCell

    def getRemainingValues(self):
        RV = []
        for row in range(self.dim):
            for col in range(self.dim):
                if self.board[row][col] != '0':
                    RV.append(['x']) # x means the cell is already filled
                else:
                    RV.append(self.getDomain(row, col))
        return RV

    def ReduceRemainingValues(self, row, col, choice):
        for i in range(self.dim):
            if choice in self.rv[row*self.dim + i]:
                self.rv[row*self.dim + i].remove(choice)
            if choice in self.rv[i*self.dim + col]:
                self.rv[i*self.dim + col].remove(choice)
        boxRow = row - (row % 3) # get the top left corner of the box
        boxCol = col - (col % 3)
        for i in range(3):
            for j in range(3):
                if choice in self.rv[(boxRow + i)*self.dim + (boxCol + j)]:
                    self.rv[(boxRow + i)*self.dim + (boxCol + j)].remove(choice)

        for i in range(self.dim):
            if self.board[row][i] == choice or self.board[i][col] == choice:
                return False
        boxRow = row - (row % 3)
        boxCol = col - (col % 3)
        for i in range(3):
            for j in range(3):
                if self.board[boxRow + i][boxCol + j] == choice:
                    return False
        return True

    def getDomainLength(self,lst):
        if 'x' in lst or lst == []:
            return 10 # return 10 as a large number out of the problem space in order to prevent the agent from choosing an empty domain as the minimum remaining value cell.
        else:
            return len(lst)

    # if you choose a value from the small domain set you have a high probability of choosing the right value.
    def getNextMRVRowCol(self): # MRV stands for Minimum Remaining Value
        rvMap = list(map(self.getDomainLength,self.rv)) # {index_of_domain_array --> lenght of array}
        minimum = min(rvMap)
        if minimum == 10: # if there is no remaining valeus for any cell
            return (-1, -1)
        index = rvMap.index(minimum)
        return(index // self.dim, index % self.dim) # (row, col) : Since we stored the domains linearly we have to compute the row and columns with a division and modulo operation on each self.rv index.
    
    # Forward Checking is simply providing a vision for the program to increase the probability of making a profit out of its choice in the higher levels of the tree.
    def isEmptyDomainProduced(self,row,col,choice): # It is possible to implement forward checking for more than one step. However, it may cause a serious time overhead.
        element = self.rv.pop(row*self.dim + col)
        if [] in self.rv:
            self.rv.insert(row*self.dim +col,element)
            return True
        else:
            self.rv.insert(row*self.dim +col,element)
            return False
    
    def getNextLocation(self): # One variable at a time without MRV heuristic
        for row in range(self.dim):
            for col in range(self.dim):
                if self.board[row][col] == '0':
                    return [row, col]
        return [-1, -1]

    def solveCSP(self):
        location = self.getNextMRVRowCol() # get next empty cell location with Minimum Remaining Value [row, col]
        if location[0] == -1:
            return True
        else:
            self.expandedNodes += 1
            for choice in self.rv[location[0]*self.dim + location[1]]:
                self.board[location[0]][location[1]] = choice
                back_up = copy.deepcopy(self.rv)
                self.rv[location[0]*self.dim + location[1]] = ['x']
                # self.rv = self.getRemainingValues() 
                self.ReduceRemainingValues(location[0], location[1], choice) # A better way is to only check the domain of the values in the same row and column of the selected cell, not the whole table!
                if not self.isEmptyDomainProduced(location[0], location[1], str(choice)): # Forward Checking
                    if self.solveCSP():
                        return True
                self.board[location[0]][location[1]] = '0'
                self.rv = back_up
        return False

def main():
    board = [
        ['5', '3', '0', '0', '7', '0', '0', '0', '0'],
        ['6', '0', '0', '1', '9', '5', '0', '0', '0'],
        ['0', '9', '8', '0', '0', '0', '0', '6', '0'],
        ['8', '0', '0', '0', '6', '0', '0', '0', '3'],
        ['4', '0', '0', '8', '0', '3', '0', '0', '1'],
        ['7', '0', '0', '0', '2', '0', '0', '0', '6'],
        ['0', '6', '0', '0', '0', '0', '2', '8', '0'],
        ['0', '0', '0', '4', '1', '9', '0', '0', '5'],
        ['0', '0', '0', '0', '8', '0', '0', '7', '9']
    ]
    dim = 9
    fileDir = 'sudoku.txt'
    start = time.time()
    # sudokuSolver = SudokuSolverCSP(dim, fileDir)
    sudokuSolver = SudokuSolverCSP(dim, board)
    sudokuSolver.solveCSP()
    end = time.time()
    print("#### SudokuSolverCSP ####")
    print("board : ")
    for row in sudokuSolver.board:
        print(row)
    print("expandedNodes: ") 
    print(sudokuSolver.expandedNodes) # analysis
    print("elapsed time: ")
    print(end - start) # analysis
    print("########################################")