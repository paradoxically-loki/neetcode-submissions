from functools import lru_cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(maxsize = None)
        def dfs(l,r):
            if l > r:
                return 0

            even = (r-l)%2 == 0 #alice's turn 
            left = piles[l] if even else 0
            right = piles[r] if even else 0
            return max(dfs(l+1,r) + left, dfs(l,r-1) + right)

        total = sum(piles)
        alice_score = dfs(0,len(piles)-1)
        return alice_score > total - alice_score
        