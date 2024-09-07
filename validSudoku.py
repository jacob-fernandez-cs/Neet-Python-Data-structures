class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
    #determine if a sudoku board is valid
    #Each row must contain the digits 1-9 without repetition.
    #Each column must contain the digits 1-9 without repetition.
    #Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    #create a hashset for columns and rows to make sure there is no repetition
    #create a hashset for each 3x3 grid
        import collections
        cols = collections.defaultdict(set) #this is a hashmap, where the key is the column number and the value is the set of all values in the respective column
        rows = collections.defaultdict(set) #this is a hashmap, where the key is the row number and the value is the set of all values in the respective row
        squares = collections.defaultdict(set) #this is a hashmap, where the key is (row/3, column/3)

        #the grid is 9x9 thus we need to iterate through the entire grid
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": #checking if the space is empty, represented by dot if it is empty move on to the next loop iteration
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r //3, c // 3)]): #we need to check if a duplicate has been found, you must check if the value exists in the current row, if the value exists in the current column, and if the value exists in the current 3x3 grid
                    return False
                #if it is not a duplicate we must update all 3 hashmaps
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c])
        return True #no duplicates have been found, thus return true
    

Solution = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution.isValidSudoku(board))
