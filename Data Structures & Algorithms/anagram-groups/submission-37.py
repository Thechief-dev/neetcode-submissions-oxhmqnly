class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 52
            for ch in word:
                if 'a' <= ch <= 'z':
                    count[ord(ch) - ord('a')] += 1
                elif 'A' <= ch <= 'Z':
                    count[ord(ch) - ord('A') + 26] += 1
            
            res[tuple(count)].append(word)
        return list(res.values())