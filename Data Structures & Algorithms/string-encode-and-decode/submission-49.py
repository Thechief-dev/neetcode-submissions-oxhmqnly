class Solution:

    def encode(self, strs: List[str]) -> str:
        words = ""

        for s in strs:
            words += str(len(s)) + "." + s
        return words
    def decode(self, s: str) -> List[str]:
        
        words = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != ".":
                j += 1
            
            size = int(s[i:j])

            i = j + 1
            j = i + size
            words.append(s[i:j])
            i = j
        return words