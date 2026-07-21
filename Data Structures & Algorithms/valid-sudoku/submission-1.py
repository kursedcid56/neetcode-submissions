class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = set()
        for i in range(len(board)):
            for j in range(len(board)):
                value = board[i][j]
                if value == ".":
                    continue
                row_label = f"hang{i} gia tri {value}"
                column_label = f"cot{j} gia tri{value}"
                box_label = f"Ô {i//3}-{j//3} gia tri{value}"

                if (row_label in check)or(column_label in check)or(box_label in check):
                    return False
                check.add(row_label)    
                check.add(column_label)    
                check.add(box_label)    

        return True            