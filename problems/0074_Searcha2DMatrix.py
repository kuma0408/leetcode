class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        w = len(matrix[0])
        h = len(matrix)
        l = 0
        r = w * h - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // w
            col = mid % w

            if matrix[row][col] > target:
                r = mid - 1
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                return True
            
        return False