class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        check_set = set()
        for r in range(9):
            for c in range(9):
                item = board[r][c]
                if item == '.':
                    continue
                # you might think you can encode cols as (c, item) - but don't forget (r, item) with
                # values might have same values, more so in case of densely filled state.
                # therefore, we're using encoding col data as (item, c)
                if (r, item) in check_set or (item, c) in check_set or (r/3, c/3, item) in check_set:
                    return False
                check_set.add((r, item))
                check_set.add((item, c))
                check_set.add((r/3, c/3, item))
        return True

