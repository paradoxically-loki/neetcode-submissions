class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l1, l2 = len(s1), len(s2)

        if l1 > l2: 
            return False

        need, window = [0]*26, [0]*26

        for c in s1:
            need[ord(c) - ord('a')] += 1

        for r in range(l2):
            window[ord(s2[r]) - ord('a')] += 1

            if r >= l1:
                window[ord(s2[r - l1]) - ord('a')] -= 1

            if need == window:
                return True

        return False
        