class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1="adc"
        # s2="dcda"
        if len(s1) > len(s2):
            return False

        sorted_s1 = "".join(sorted(s1))
        k = len(s1)

        for i in range(len(s2) - k + 1):
            sub_str = s2[i: i+k]
            sub_str = "".join(sorted(sub_str))
            print(sub_str)
            if sub_str == sorted_s1:
                return True
        
        return False