class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        dictTo = defaultdict(int)
        res = ""

        for ch in strs:
            prefix = ""

            for i in range(len(ch)):
                prefix += ch[i]
                dictTo[prefix] += 1
                if dictTo[prefix] == len(strs):
                    res = prefix
        return res
