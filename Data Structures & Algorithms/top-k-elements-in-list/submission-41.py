class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1

        sorted_freq = sorted(freq.items(), key= lambda item: item[1], reverse=True)
        res = []
        for key, value in sorted_freq:
            res.append(key)
            if len(res) == k :            
                return res