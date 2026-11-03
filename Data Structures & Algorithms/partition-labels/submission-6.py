class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        endOfSubString = {}
        size = 0
        end = 0
        res = []

        for i, ch in enumerate(s):
            endOfSubString[ch] = i
        
        for i, ch in enumerate(s):
            size += 1
            end = max(end, endOfSubString[ch])

            if i == end:
                res.append(size)
                size = 0
        return res