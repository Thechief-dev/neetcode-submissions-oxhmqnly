class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1 , -1, -1):
            if nums[i -1 ] == val:
                print(nums[i-1])
                nums.remove(val)
                
        
        return len(nums)
        