class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for ch in s:
            d[ch] = d.get(ch,0) + 1
        for ch in t:
            if ch not in d:
                return False
            d[ch] -= 1
        for val in d.values():
            if val != 0:
                return False
        return True