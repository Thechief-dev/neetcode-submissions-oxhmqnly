class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        mid = n // 2

        sortLeft = self.sortArray(nums[:mid])
        sortRight = self.sortArray(nums[mid:])


        return self.merge(sortLeft, sortRight)
    
    def merge(self, left, right):
        res = [] # merge in list
        i = j = 0 # pointers for left and right

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