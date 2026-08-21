class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

        # if len(nums) == 0:
        #     return 0

        # max_length = 1

        # for num in nums:
        #     if num - 1 in nums:
        #         continue
        #     else:
        #         seq_start = num
        #         length = 1
        #         while (seq_start + length) in nums:
        #             length += 1
                
        #         max_length = max(max_length, length)
        # return max_length
                
