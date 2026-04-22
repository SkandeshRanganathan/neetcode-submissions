class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ana = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in ana:
                ana[key].append(i)
            else:
                ana[key] = [i]
        return list(ana.values())