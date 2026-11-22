class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupWord = defaultdict(list)

        for word in strs:
            flagMapping = [0] * 26

            for ch in word:
                flagMapping[ord(ch) - ord('a')] += 1
            
            groupWord[tuple(flagMapping)].append(word)
        
        return list(groupWord.values())