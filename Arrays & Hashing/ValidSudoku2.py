
class Solution:
    def isValidSudoku(self, board : list[list[str]]) -> bool:
        isValid = True

        squareHash = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
            ]

        for row in range(9):
            numCount = [0,0,0,0,0,0,0,0,0,0]
            numCount2 = [0,0,0,0,0,0,0,0,0,0]
            for column in range(9):
                number = board[row][column]
                number2 = board[column][row]
                square = (int(row/3) * 3 + int(column/3))
                print(square)

                if number.isdigit():
                    squareHash[square][int(number)] += 1
                    if squareHash[square][int(number)] > 1:
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
