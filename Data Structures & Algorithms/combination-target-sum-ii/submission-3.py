class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = set()
        candidates.sort()

        def dfs(i, curr, currSum):
            if currSum == target:
                res.add(tuple(curr))
                return

            if i >= len(candidates) or currSum > target:
                return

            curr.append(candidates[i])
            dfs(i+1, curr, currSum + candidates[i])
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curr, currSum)

        dfs(0, [], 0)

        return [list(item) for item in res]