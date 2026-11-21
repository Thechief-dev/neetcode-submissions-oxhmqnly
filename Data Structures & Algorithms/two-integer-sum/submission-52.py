class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_idx = defaultdict(int)

        for i, num in enumerate(nums):
            diff=  target - num

            if num in diff_idx:
                return [diff_idx[num], i]
            
            else:
                diff_idx[diff] = i
        
        