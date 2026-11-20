class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)

        return len(nums) != len(unique)