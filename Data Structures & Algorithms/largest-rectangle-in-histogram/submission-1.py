class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        l = [-1]*n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                l[i] = stack[-1]
            stack.append(i)

        stack = []
        r = [n]*n 
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                r[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(n):
            l[i] += 1
            r[i] -= 1
            maxArea = max(maxArea, heights[i]*(r[i]-l[i]+1))

        return maxArea       