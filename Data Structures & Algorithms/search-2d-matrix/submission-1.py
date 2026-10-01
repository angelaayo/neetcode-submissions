class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[len(row) -1] < target:
                continue # skip over to the next if the row has a lst number smaller than the goal
            if row[0] > target:
                return False
            j = 0
            while j < len(row):
                if row[j] == target:
                    return True
                j+=1
            return False
        return False