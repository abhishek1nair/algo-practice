# LeetCode url: https://leetcode.com/problems/valid-sudoku/

class Solution:
    def __get_num_dict(self):
        return {
            "1": False,
            "2": False,
            "3": False,
            "4": False,
            "5": False,
            "6": False,
            "7": False,
            "8": False,
            "9": False
        }

    def __verify_rows(self, board):
        for row in board:
            check_list = self.__get_num_dict()
            for item in row:
                if item == '.':
                    continue
                if check_list[item]:
                    return False
                else:
                    check_list[item] = True
        return True

    def __verify_cols(self, board):
        for r in range(9):
            check_list = self.__get_num_dict()
            for c in range(9):
                item = board[c][r]
                if item == '.':
                    continue
                if check_list[item]:
                    return False
                else:
                    check_list[item] = True
        return True

    def __verify_block(self, board):
        # block start and end points need to setup for rows and cols
        r_offset = 0
        c_offset = 0
        for r_offset in range(0, 9, 3):
            for c_offset in range(0, 9, 3):
                check_list = self.__get_num_dict()
                for i in range(3):
                    for j in range(3):
                        item = board[c_offset + i][r_offset + j]
                        if item == '.':
                            continue
                        if check_list[item]:
                            return False
                        else:
                            check_list[item] = True
        return True

    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hasValidRows = self.__verify_rows(board)
        hasValidCols = self.__verify_cols(board)
        hasValidBlocks = self.__verify_block(board)

        # print(hasValidRows, hasValidCols, hasValidBlocks)
        isValid = hasValidRows and hasValidCols and hasValidBlocks
        return isValid

# Learnings from this solution and why it is bad?
# 1. Try to solve the whole problem in one loop
# 2. Try to encode the data to make in simpler so that comparisons become simple
# 3. Try to reduce space complexity,
#    here the __get_num_dict creates too many local variables, try to optimise
#    that.
