class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # convert to the most frequent character?
        # num of replacements = lengths of the current window - freq of the most frequent

        l = 0
        maxFreq = 0
        maxLen = 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1
            maxFreq = max(maxFreq, count[s[r]])

            if r-l+1 - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r-l+1)

        return maxLen

        


