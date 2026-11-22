class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for i in range(len(strs[0])):
            for ch in strs:
                if i == len(ch) or ch[i] != strs[0][i]:
                    return ch[:i]

        return strs[0]