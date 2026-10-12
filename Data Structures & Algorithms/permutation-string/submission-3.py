class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1): return False

        count_s1 = [0]*26
        for c in s1:
            count_s1[ord(c) - ord('a')] += 1

        count_s2 = [0]*26
        for i in range(len(s1)):
            count_s2[ord(s2[i]) - ord('a')] += 1

        l = 0; r = len(s1)-1

        while r < len(s2):
            if count_s1 == count_s2:
                return True
           
            count_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1

            r += 1

            if r < len(s2):
                count_s2[ord(s2[r]) - ord('a')] += 1

        return False        