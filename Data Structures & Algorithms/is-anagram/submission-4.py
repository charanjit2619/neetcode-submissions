class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if sorted(s) != sorted(t):
            return False
        else:
            return True

# The dictionary counting has a time complexity of O(n), while this has a time complexity of O(nlogn) due to sorting. So this would be a bit slower. 
# Space complexity of this solution: O(n) since sorting creates a new list in the memory. (dictionary solution: O(n))
