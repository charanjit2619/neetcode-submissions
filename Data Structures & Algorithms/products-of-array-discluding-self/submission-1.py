class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        res = []

        array_product = 1
        for num in nums:
            if num == 0:
                zero_count += 1
                continue
            array_product = array_product*num
        
        if zero_count > 1:
            res =  [0] * len(nums)
        elif zero_count == 1:
            res = [0] * len(nums)
            res[nums.index(0)] = array_product
        else:
            for num in nums:
                res.append(int(array_product/num))
        return res