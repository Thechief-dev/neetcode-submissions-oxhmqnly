class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [] * (len(nums) * 2)

        for i in range(2):
            for num in nums:
                res.append(num)

        return res