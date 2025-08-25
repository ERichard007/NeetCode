#trash solution

class Solution:
    def isValidSudoku(self, board : list[list[str]]) -> bool:
        isValid = True

        cellCount = [
                [0,0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0,0]
                ]
        cell = 0
        rowct = -1
        colct = -1

        for i in range(9):
            numCount = [0,0,0,0,0,0,0,0,0,0]
            numCount2 = [0,0,0,0,0,0,0,0,0,0]
            for j in range(9):
                number = board[i][j]
                number2 = board[j][i]

                rowct+=1

                if ((rowct%3==0 and rowct!=0) and colct==3):
                    print("increment1")
                    rowct = 0
                    colct = 0
                    cell = 0
                    cellCount = [
                    [0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0]
                    ]
                elif (rowct==9):
                    print("increment2")
                    cell = 0
                    colct += 1
                    rowct = 0
                elif (rowct%3==0 and rowct!=0):
                    print("increment3")
                    cell += 1

                if number.isdigit():
                    if cellCount[cell][int(number)] < 1:
                        cellCount[cell][int(number)]+=1
                        print(f"{cellCount}\n***")
                    else:
                        cellCount[cell][int(number)]+=1
                        print(f"INVALID:\n{cellCount}\n***")
                        return False
                    


                    if numCount[int(number)] == 0:
                        numCount[int(number)]+=1
                    else:
                        return False
                    
                if number2.isdigit():
                    if numCount2[int(number2)] == 0:
                        numCount2[int(number2)]+=1
                    else:
                        return False
                
        return isValid

board = [
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".","3",".","."],
    [".",".",".","1","8",".",".",".","."],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".",".","1",".","9","7","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".","3","6",".","1",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","2","."]
    ]
mySolution = Solution()
isValid = mySolution.isValidSudoku(board)
print(f" The board is valid") if isValid else print(f" The board is not valid")
