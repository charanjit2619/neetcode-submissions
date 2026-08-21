class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        if len(nums) == 0:
            return 0

        max_length = 1

        for num in numset:
            if num - 1 in numset:
                continue
            else:
                seq_start = num
                length = 1
                while (seq_start + length) in numset:
                    length += 1
                
                max_length = max(max_length, length)
        return max_length
                
