class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = [0]*26
        t_freq = [0]*26

        for alphabet in s:
            s_freq[ord(alphabet) - 97] += 1

        for alphabet in t:
            t_freq[ord(alphabet) - 97] += 1
    
        return s_freq == t_freq


        