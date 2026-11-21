class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictTo = defaultdict(int)

        for i, num in enumerate(nums):
            looking_diff = target - num

            if num in dictTo:
                return [dictTo[num] , i]
            else:
                dictTo[looking_diff] = i
        
        return [0, 0]