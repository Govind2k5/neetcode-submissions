class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = len(matrix),len(matrix[0])

        top,bot=0,row-1
        while top<=bot:
            midrow = (top+bot)//2
            if target < matrix[midrow][0]:
                bot = midrow -1
            elif target > matrix[midrow][-1]:
                top = midrow +1
            else:
                break
        if not top<=bot:
            return False
        row = (top +bot)//2
        l = 0
        r = col -1
        while l<=r:
            mid = (l+r)//2
            if target < matrix[row][mid]:
                r = mid -1
            elif target > matrix[row][mid]:
                l = mid +1
            else:
                return True
        return False