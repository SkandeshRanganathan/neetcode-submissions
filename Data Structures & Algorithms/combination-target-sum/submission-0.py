class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def back(start,target,path):
            if target == 0:
                result.append(path[:])
                return
            if target < 0:
                return 
            for i in range(start,len(nums)):
                num = nums[i]
                path.append(num)
                back(i,target-num,path)
                path.pop()
        back(0,target,[])
        return result