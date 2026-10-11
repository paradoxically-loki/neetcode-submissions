class Solution:

    def encode(self, strs: List[str]) -> str:

        # number of chars + hash
        res = []

        for s in strs:
            len_ = len(s)

            res.append(str(len_))
            res.append('#')
            res.append(s)

        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        
        res = []
        
        l = 0
        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1
            _len = int(s[l:r])

            res.append(s[r + 1: r + 1 + _len])

            l = r + 1 + _len

        return res

