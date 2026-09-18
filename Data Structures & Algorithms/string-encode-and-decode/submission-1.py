class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            _len = len(s)
            res += str(_len)+'#'
            res += s
 
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            num = ''
            j = i
            while s[j] != '#':
                num += s[j]
                j += 1

            num = int(num)  
            res.append(s[j+1:j+1+num])
            i = j + 1 + num
    
        return res

