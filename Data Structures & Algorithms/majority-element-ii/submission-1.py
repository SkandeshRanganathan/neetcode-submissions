class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = []
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for key,value in dic.items():
            if value > n//3:
                l.append(key)
        return l