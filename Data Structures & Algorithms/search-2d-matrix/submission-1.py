class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        l_row, r_row = 0, n-1

        while l_row <= r_row:
            mid_r = (r_row - l_row)//2 + l_row

            if matrix[mid_r][0] <= target <= matrix[mid_r][m-1]:

                l = 0; r = m-1
                while l <= r:
                    mid = (r-l)//2 + l
                    if matrix[mid_r][mid] == target:
                        return True
                    elif matrix[mid_r][mid] < target:
                        l = mid+1
                    else:
                        r = mid-1
                return False

            elif matrix[mid_r][0] > target:
                r_row = mid_r - 1

            else:
                l_row = mid_r + 1
        
        return False