class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0: return 0

        l = 0

        currSet = set()
        currSet.add(s[0])

        maxLen = 1

        for r in range(1, len(s)):
            while s[r] in currSet:
                currSet.remove(s[l])
                l += 1
            
            currSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)

        return maxLen


        