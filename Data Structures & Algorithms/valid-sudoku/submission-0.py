class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        column = defaultdict(list)
        sub_boxes = defaultdict(list)

        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element == ".":
                    continue
                if element in row[i]:
                    return False
                else:
                    row[i].append(element)
                if element in column[j]:
                    return False
                else:
                    column[j].append(element)
                if element in sub_boxes[i//3, j//3]:
                    return False   
                else:       
                    sub_boxes[i//3, j//3].append(element)
        return True
        
        
