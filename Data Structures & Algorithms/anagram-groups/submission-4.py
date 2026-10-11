class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for s in strs:
            groups[tuple(self.count_freq(s))].append(s)

        res = []
        for val in groups.values():
            res.append(val)

        return res


    def count_freq(self, s):

        count = [0]*26

        for c in s:
            count[ord(c) - ord('a')] += 1

        return count

