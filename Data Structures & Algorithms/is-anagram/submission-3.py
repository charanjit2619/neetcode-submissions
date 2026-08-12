class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_seen = {}
        for letter in s:
            if letter in s_seen:
                s_seen[letter] += 1
            else:
                s_seen[letter] = 1

        t_seen = {}
        for letter in t:
            if letter in t_seen:
                t_seen[letter] += 1
            else:
                t_seen[letter] = 1

        for key, value in t_seen.items():
            if key in s_seen:
                if value == s_seen[key]:
                    continue
                else:
                    return False
            else:
                return False
        return True
        
