class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for x in nums:
            dic[x] = dic.get(x,0) + 1
        l = sorted(dic, key = dic.get)
        return l[-k:]