class Solution:
    def canJump(self, nums: List[int]) -> bool:
        destination = len(nums) - 1

        for i in range(destination - 1, -1, -1):
            if nums[i] + i >= destination:
                destination = i
        
        if destination == 0:
            return True
        else:
            return False