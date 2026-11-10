class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = 0
        ans = ''
        
        # if len(s) == 1: return s

        for i in range(len(s)):
            # odd length case
            l, r = i, i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if best < r-l+1:
                    best = r-l+1
                    ans = s[l:r+1]
                l, r = l-1, r+1
                    
            # even length case
            l, r = i, i+1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if best < r-l+1:
                    best = r-l+1
                    ans = s[l:r+1]
                l, r = l-1, r+1
        
        return ans