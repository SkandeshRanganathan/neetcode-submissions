class Solution:
    def validPalindrome(self, s: str) -> bool:
        def fn(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l = 0
        n = len(s)
        r = n-1
        while l < r:
            if s[l] != s[r]:
                return fn(l+1,r) or fn(l,r-1)
            l += 1
            r -= 1
        return True