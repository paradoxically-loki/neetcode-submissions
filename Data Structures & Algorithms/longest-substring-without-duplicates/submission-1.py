class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0: return 0

        l, r = 0, 1
        ans = 0

        seen = set(s[l])
        ans += 1
        curr = 1

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                curr += 1
                ans = max(ans, curr)
            else:
                seen.remove(s[l])
                l += 1
                curr -= 1

        return ans







        