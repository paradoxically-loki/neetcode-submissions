class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for num in nums:
            new_subsets = []
            for subset in results:
                new_subset = subset + [num]
                new_subsets.append(new_subset)
            results.extend(new_subsets)
        return results
        