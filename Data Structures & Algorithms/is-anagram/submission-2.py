class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 or len(t) == 0:
            return False

        seen = {}
        for letter in s:
            if letter in seen:
                seen[letter] += 1
            else: 
                seen[letter] = 1
        
        for letter in t:
            if letter in seen:
                seen[letter] -= 1
            else:
                return False

        for key, value in seen.items():
            if value != 0:
                return False
        
        return True