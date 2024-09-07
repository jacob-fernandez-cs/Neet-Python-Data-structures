class Solution:
    def maxArea(self, height: list[int]) -> int:
        #brute force solution
        result = 0
        for leftpointer in range(len(height)):
            for rightpointer in range(leftpointer + 1, len(height)):
                area = (rightpointer - 1) * min(height[leftpointer], height[rightpointer])
                result = max(result, area)
        return result
    
    def linearTime(self, height: list[int]) -> int:
        result = 0
        leftpointer = 0
        rightpointer = len(height) - 1

        while leftpointer < rightpointer:
            area = (rightpointer - 1) * min(height[leftpointer], height[rightpointer])
            result = max(result, area)

            if height[leftpointer] < height[rightpointer]:
                l += 1
            else:
                r -= 1
        return result


Solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
Solution.linearTime(height)