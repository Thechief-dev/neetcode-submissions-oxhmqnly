class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastIndex = {}

        for i, ch in enumerate(s):
            lastIndex[ch] = i 

        size = 0
        end = 0

        for i, ch in enumerate(s):
            size += 1
            end = max(end, lastIndex[ch])

            if i == end:
                res.append(size)
                size = 0

        return res

