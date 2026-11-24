class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        n = len(nums)

        mid = n // 2

        leftSort = self.sortArray(nums[:mid])
        rightSort = self.sortArray(nums[mid:])

        return self.merge(leftSort, rightSort)
    
    def merge(self, left, right):
        res = []

        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])

        return res