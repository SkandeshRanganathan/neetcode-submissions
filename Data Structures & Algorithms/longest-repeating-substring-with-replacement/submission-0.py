class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = [0]*26
        mf = 0
        ans = 0
        r = 0
        for right in range(len(s)):
            i = ord(s[right]) - ord('A')
            freq[i] += 1
            mf = max(mf,freq[i])
            r = (right-left+1) - mf
            if r > k:
                freq[(ord(s[left])) - ord('A')] -= 1
                left += 1
            ans = max(ans,right - left + 1)
        return ans