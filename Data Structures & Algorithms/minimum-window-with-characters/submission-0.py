from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic1 = Counter(t)
        left = 0
        have = 0
        curr = {}
        min_len = float('inf')
        min_start = 0
        for right in range(len(s)):
            ch = s[right]
            curr[ch] = curr.get(ch,0)+1
            if ch in dic1 and dic1[ch] == curr[ch]:
                have+=1
            while have == len(dic1):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                left_ch = s[left]
                curr[left_ch] -= 1
                if left_ch in dic1 and curr[left_ch] < dic1[left_ch]:
                    have -= 1
                left += 1
        if min_len == float('inf'):
            return ""
        return s[min_start:min_start+min_len]