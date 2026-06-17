class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # check rows
        checklist = [0] * 10
        for mlist in board:
            for _, numstr in enumerate(mlist):
                if numstr == ".":
                    continue
                num = int(numstr)
                if checklist[num] == 1:
                    return False
                checklist[num] = 1
            checklist = [0] * 10

        # check columns
        # check rows
        for num in range(0, 9):
            checklist = [0] * 10
            colist = [i[num] for i in board]
            for _, numstr in enumerate(colist):
                if numstr == ".":
                    continue
                num = int(numstr)
                if checklist[num] == 1:
                    return False
                checklist[num] = 1
            checklist = [0] * 10

        # check small boxes
        for nx in range(0, 9, 3):
            checklist = [0] * 10
            for idx in range(0, 9, 3):
                colist = []
                colist.extend(board[nx][idx : idx + 3])
                colist.extend(board[nx + 1][idx : idx + 3])
                colist.extend(board[nx + 2][idx : idx + 3])
                for _, numstr in enumerate(colist):
                    if numstr == ".":
                        continue
                    num = int(numstr)
                    if checklist[num] == 1:
                        return False
                    checklist[num] = 1
                checklist = [0] * 10
        return True