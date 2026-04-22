class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        l = 0
        r = 0
        for i in range (max(len(word1),len(word2))):
            if l < len(word1):
                ans = ans + word1[l]
                l += 1
            if r < len(word2)!= "":
                ans = ans + word2[r]
                r += 1
        return ans