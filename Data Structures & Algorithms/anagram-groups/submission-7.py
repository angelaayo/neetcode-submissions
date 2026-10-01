class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
           sortedKey = tuple(sorted(s)) 
           # sorted returns a list hence we make it a tuple(not mutable)
           res[sortedKey].append(s)
        return list(res.values())
        