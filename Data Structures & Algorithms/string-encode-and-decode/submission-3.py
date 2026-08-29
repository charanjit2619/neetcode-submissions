class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word)) + '#'
            encoded_str += word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        i = 0

        while i < (len(s)):
            if s[i] == '#':
                count = int(s[start:i])
                res.append(s[i+1: i + count + 1])
                start = i + count + 1
                i += count + 1
            i += 1
        return res
