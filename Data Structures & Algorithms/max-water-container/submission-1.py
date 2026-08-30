class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxW = (r-l) * min(heights[l], heights[r])

        while(l < r):
            if heights[l] < heights[r]:
                l += 1
                maxW = max(maxW, (r-l) * min(heights[l], heights[r]))

            elif heights[l] > heights[r]:
                r -= 1
                maxW = max(maxW, (r-l) * min(heights[l], heights[r]))
            
            else:
                l += 1
                maxW = max(maxW, (r-l) * min(heights[l], heights[r]))
        return maxW