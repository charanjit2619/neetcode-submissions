class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNum = sorted(nums)
        res = set()

        for i in range(len(sortedNum) - 2):
            target = -sortedNum[i]

            sliced_sortedNum = sortedNum[i + 1:]

            p1 = 0
            p2 = len(sliced_sortedNum) - 1

            while(p1 < p2):
                if sliced_sortedNum[p1] + sliced_sortedNum[p2] > target : 
                    p2 -= 1
                elif sliced_sortedNum[p1] + sliced_sortedNum[p2] < target : 
                    p1 += 1
                else:
                    res.add((sortedNum[i], sliced_sortedNum[p1], sliced_sortedNum[p2]))
                    p1 += 1
        return [list(s) for s in res]