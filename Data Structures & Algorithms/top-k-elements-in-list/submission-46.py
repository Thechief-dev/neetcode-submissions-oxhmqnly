class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        shelf = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1
        
        for file, cnt in count.items():
            shelf[cnt].append(file)

        
        handOfFile = []

        for idx in range(len(shelf) - 1, 0, -1):
            for file in shelf[idx]:
                handOfFile.append(file)
                if len(handOfFile) == k:
                    return handOfFile