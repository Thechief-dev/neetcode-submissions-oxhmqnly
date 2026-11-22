class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num

            if num in diffMap:
                return [diffMap[num], i]
            else:
                diffMap[diff] = i
        return [0, 0]