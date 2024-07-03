import time
# import sys
# sys.setrecursionlimit(200000)

class SudokuSolverSimpleBackTracking:
    def __init__(self, dim, board):
        self.board = board
        self.dim = dim
        self.expandedNodes = 0

    # def __init__(self, dim, fileDir):
    #     self.dim = dim
    #     self.expandedNodes = 0
    #     with open(fileDir) as f:
    #         content = f.readlines()
    #         self.board = [list(x.strip()) for x in content] # split?
    
    def sloveSimpleBackTracking(self): # DFS with 2 ideas : 1.One variable at a time 2.Check constraints as you go
        location = self.getNextLocation() # get next empty cell location [row, col]
        if location[0] == -1:
            return True
        else:
            self.expandedNodes += 1
            for choice in range(1, self.dim+1): # choices from  1 to 9
                if self.isSafe(location[0], location[1], str(choice)):
                    self.board[location[0]][location[1]] = str(choice)
                    if self.sloveSimpleBackTracking():
                        return True
                    self.board[location[0]][location[1]] = '0'
        return False

    def getNextLocation(self): # One variable at a time
        for row in range(self.dim):
            for col in range(self.dim):
                if self.board[row][col] == '0':
                    return [row, col]
        return [-1, -1]
    
    def isSafe(self, row, col, choice): # Check constraints as you go
        for i in range(self.dim):
            if self.board[row][i] == choice or self.board[i][col] == choice:
                return False
        boxRow = row - (row % 3)
        boxCol = col - (col % 3)
        for i in range(3):
            for j in range(3):
                if self.board[boxRow + i][boxCol + j] == choice:
                    return False
        # for i in range(boxRow, boxRow+3):
        #     for j in range(boxCol, boxCol+3):
        #         if self.board[i][j] == choice:
        #             return False
        return True
    
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
    # sudokuSolver = SudokuSolverSimpleBackTracking(dim, fileDir)
    sudokuSolver = SudokuSolverSimpleBackTracking(dim, board)
    sudokuSolver.sloveSimpleBackTracking()
    end = time.time()
    print("#### SudokuSolverSimpleBackTracking ####")
    print("board : ")
    for row in sudokuSolver.board:
        print(row)
    print("expandedNodes: ") 
    print(sudokuSolver.expandedNodes) # analysis
    print("elapsed time: ")
    print(end - start) # analysis
    print("########################################")