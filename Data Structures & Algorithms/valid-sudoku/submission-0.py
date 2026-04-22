class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        boxes = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                row = (r,val)
                col = (c , val)
                box = (r//3 , c//3 , val)
                if (row in rows or col in cols or box in boxes): return False
                rows.add(row)
                cols.add(col)
                boxes.add(box)

        return True