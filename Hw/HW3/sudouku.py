#Question1 :
    # source : https://www.geeksforgeeks.org/sudoku-backtracking-7/
    # source : youtube

#Question2 :
    #https://levelup.gitconnected.com/csp-algorithm-vs-backtracking-sudoku-304a242f96d0


class FirstProblem:

    def __init__(self,dim,board) -> None:
        self.expandedNodes = 0
        self.dim = dim
        self.board = board

    def solveSimpleBackTracking(self): # in this function we need to implement two other functions : isSafe and getNextLocation according to question
        location = self.getNextLocation()
        if location[0] == -1:
            return True
        else:
            self.expandedNodes += 1
            for choice in range(1, self.dim+1):
                if self.isSafe(self.board,location[0], location[1], str(choice)):
                    self.board[location[0]][location[1]] = str(choice)
                    if self.solveSimpleBackTracking():
                        return True
                    self.board[location[0]][location[1]] = '0'
        return False
                    
    def getNextLocation(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '0':
                    return [i,j]
        return [-1,-1]

    def isSafe(self,board, row, col, num): # source : gfg
        for x in range(9):
            if board[row][x] == num:
                return False
            
        for x in range(9):
            if board[x][col] == num:
                return False
            
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + startRow][j + startCol] == num:
                    return False
        return True

board = [
        ['0', '1', '6', '3', '0', '8', '4', '2', '0'],
        ['8', '4', '0', '0', '0', '7', '3', '0', '0'],
        ['3', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '6', '0', '9', '4', '0', '8', '0', '2'],
        ['0', '8', '1', '0', '3', '0', '7', '9', '0'],
        ['9', '0', '3', '0', '7', '6', '0', '4', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '3'],
        ['0', '0', '5', '7', '0', '0', '0', '6', '8'],
        ['0', '7', '8', '1', '0', '3', '2', '5' , '0']
    ]

sudoku = FirstProblem(9,board)
sudoku.solveSimpleBackTracking()
print("#### SudokuSolverSimpleBackTracking ####")
print("board : ")
for row in sudoku.board:
    print(row)

print('-----------------------------------------')


class SecondProblem:
    def __init__(self,dim,fileDir):
        self.dim = dim
        self.expandedNodes = 0
        with open(fileDir) as f:
            content = f.readlines()
            self.board = [list(x.strip()) for x in content]
        self.rv = self.getRemainingValues()
    def getDomain(self,row,col):
        RVCell = [str(i) for i in range(1 ,self.dim + 1)]
        for i in range(self.dim):
            if self.board[row][i] != '0':
                if self.board[row][i] in RVCell:
                    RVCell.remove(self.board[row][i])
        for i in range(self.dim):
            if self.board[i][col] != '0':
                if self.board[i][col] in RVCell:
                    RVCell.remove(self.board[i][col])
        boxRow = row - row%3
        boxCol = col - col%3
        for i in range(3):
            for j in range(3):
                if self.board[boxRow+i][boxCol+j]!=0:
                    if self.board[boxRow+i][boxCol+j] in RVCell:
                        RVCell.remove(self.board[boxRow+i][boxCol+j])
        return RVCell
    def getRemainingValues(self):
        RV=[]
        for row in range(self.dim):
            for col in range(self.dim):
                if self.board[row][col] != '0':
                    RV.append(['x'])
                else:
                    RV.append(self.getDomain(row,col))
        return RV
    
    def getDomainLength(self,lst):
        if 'x' in lst or lst == []:
            return 10
        else:
            return len(lst)

    def getNextMRVRowCol(self):
        rvMap = list(map(self.getDomainLength,self.rv))
        minimum = min(rvMap)
        if minimum == 10:
            return (-1,-1)
        index = rvMap.index(minimum)
        return(index // 9, index % 9)
    
    def isEmptyDomainProduced(self,row,col,choice):
        element = self.rv.pop(row*9 + col)
        if [] in self.rv:
            self.rv.insert(row*9+col,element)
            return True
        else:
            self.rv.insert(row*9+col,element)
            return False
            
    def solveCSPFH(self):
        location = self.getNextMRVRowCol()
        if location[0] == -1:
            return True
        else:
            self.expandedNodes+=1

            row = location[0]
            col = location[1]
            for choice in self.rv[row*9+col]:
                choice_str = str(choice)
                self.board[row][col] = choice_str
                cpy = copy.deepcopy(self.rv) 
                self.rv = self.getRemainingValues()
    
                if not self.isEmptyDomainProduced(row,col,choice_str):
                    if self.solveCSPFH():
                        return True
                self.board[row][col] = '0'
                self.rv = cpy
        return False

board = [
        ['0', '1', '6', '3', '0', '8', '4', '2', '0'],
        ['8', '4', '0', '0', '0', '7', '3', '0', '0'],
        ['3', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '6', '0', '9', '4', '0', '8', '0', '2'],
        ['0', '8', '1', '0', '3', '0', '7', '9', '0'],
        ['9', '0', '3', '0', '7', '6', '0', '4', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '3'],
        ['0', '0', '5', '7', '0', '0', '0', '6', '8'],
        ['0', '7', '8', '1', '0', '3', '2', '5' , '0']
    ]

sudoku = FirstProblem(9,board)
sudoku.solveSimpleBackTracking()
print("#### SudokuSolverSimpleBackTracking ####")
print("board : ")
for row in sudoku.board:
    print(row)