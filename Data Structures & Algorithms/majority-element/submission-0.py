class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dictTo = defaultdict(int)
        majority_rule = len(nums) // 2
        for i, num in enumerate(nums):
            dictTo[num] += 1
        
        
        for key, value in dictTo.items():
            if value > majority_rule:
                return key
        
