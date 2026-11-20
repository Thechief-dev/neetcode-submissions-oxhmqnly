class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        u = set()

        for num in nums:
            if num not in u:
                u.add(num)
        
        return len(nums) != len(u)