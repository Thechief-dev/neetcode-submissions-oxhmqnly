class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [] * (len(nums) * 2)

        for num in nums:
            res.append(num)

        for num in nums:
            res.append(num)

        return res