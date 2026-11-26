class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
   
        for num, cnt in count.items():
            buckets[cnt].append(num)

        
        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for bucket in buckets[i]:
                res.append(bucket)
                if len(res) == k:
                    return res