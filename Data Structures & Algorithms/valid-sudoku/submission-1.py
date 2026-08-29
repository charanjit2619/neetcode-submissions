class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(int)
        col = defaultdict(int)
        sub_board = defaultdict(int)

        for i in range(9):
            for j in range(9):
                # print(i//3, j//3)
                element = board[i][j]
                if element == ".":
                    continue
                else:
                    element = int(element)

                if row[i] & 1 << element:
                    return False
                row[i] = row[i] | 1 << element
                if col[j] & 1 << element:
                    return False
                col[j] = col[j] | 1 << element
                if sub_board[f"{i//3}_{j//3}"] & 1 << element:
                    return False
                sub_board[f"{i//3}_{j//3}"] = sub_board[f"{i//3}_{j//3}"] | 1 << element
        return True