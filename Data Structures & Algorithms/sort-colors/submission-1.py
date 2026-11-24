class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = defaultdict(int)
        nums.sort(reverse=False)
        for i in range(len(nums)):
            freq[nums[i]] += 1
        
        print(freq)