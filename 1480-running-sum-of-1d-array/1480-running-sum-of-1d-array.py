class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        if not nums: 
            return res
        res.append(nums[0]);
        for num in nums[1:]: 
            res.append(num + res[-1])
        return res
            
        