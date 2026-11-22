class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidates = 0
        count = 0

        for num in nums:
            if count == 0:
                candidates = num
            
            if candidates == num:
                count += 1
            else:
                count -= 1
        return candidates
        
