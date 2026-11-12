class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix)*len(matrix[0]))-1
        mid = (left+right)//2

        while left <= right:
            mid = (left+right)//2
            if target == matrix[(mid//len(matrix[0]))][mid%len(matrix[0])]:
                return True
            elif target > matrix[(mid//len(matrix[0]))][mid%len(matrix[0])]:
                left = mid+1
            else:
                right = mid-1
        
        return False