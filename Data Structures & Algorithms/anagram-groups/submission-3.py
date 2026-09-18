class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        
        for s in strs:
            res[self.makeCount(s)].append(s)

        return list(res.values())

        
    def makeCount(self, s):
        count = [0]*26
        for c in s:
            count[ord(c) - ord('a')] += 1
        return tuple(count)
        