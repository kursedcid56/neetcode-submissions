class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = set()
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                row_label = f"hang{i} co so {value}"
                column_label = f"cot{j} co so {value}"
                box_label = f"o{i//3}-{j//3}co so {value} "

                if (row_label in check) or (column_label in check) or (box_label in check):
                    return False
                check.add(row_label)           
                check.add(column_label)
                check.add(box_label)

        return True        
