class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        count = 0
        n = len(s)
        for count in range(n//2):
            if s[count].lower() != s[n-1-count]:
                return False
        return True