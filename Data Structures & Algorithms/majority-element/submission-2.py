class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = 0
        res = 0

        for i in range(len(nums)):
            if k == 0:
                res = nums[i]
            
            if nums[i] == res:
                k += 1
            else:
                k -= 1
        return res