class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupList = defaultdict(list)

        for word in strs:
            letterLog = [0] * 26

            for ch in word:
                letterLog[ord(ch) - ord('a')] += 1
            groupList[tuple(letterLog)].append(word)

        return list(groupList.values())