class Solution:
    def trap(self, height: List[int]) -> int:

        # water at i = min(heights[l], heights[r]) - heights[i]
        # heights[l] and heights[r] are the max heights at both sides of i

        prefix = [height[0]]*len(height)
        suffix = [height[-1]]*len(height)

        for i in range(1, len(height)):
            prefix[i] = max(prefix[i-1], height[i])

        for i in range(len(height)-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])

        water = [0]*len(height)

        for i in range(len(height)):
            water[i] = min(prefix[i], suffix[i]) - height[i]

        return sum(water)  