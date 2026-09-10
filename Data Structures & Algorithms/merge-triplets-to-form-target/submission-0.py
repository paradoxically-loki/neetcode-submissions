class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        max_a, max_b, max_c = float('-inf'), float('-inf'), float('-inf')

        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue

            max_a = max(max_a, a)
            max_b = max(max_b, b)
            max_c = max(max_c, c)

        if (max_a, max_b, max_c) == (target[0], target[1], target[2]):
            return True
        
        return False
            