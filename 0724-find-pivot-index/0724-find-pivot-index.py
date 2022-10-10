class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = [0]
        for num in nums[:-1]:
            leftSum.append(num + leftSum[-1])
        rightSum = [0]
        for num in reversed(nums[1:]):
            rightSum.insert(0, num + rightSum[0])
        for i in range(len(nums)): 
            if leftSum[i] == rightSum[i]: 
                return i
        return -1
        