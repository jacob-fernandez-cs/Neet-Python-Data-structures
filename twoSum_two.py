class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lP = 0
        rP = len(numbers) - 1

        while lP < rP:
            currentSum = numbers[lP] + numbers[rP]

            if currentSum > target:
                rP -= 1
            elif currentSum < target:
                lP += 1
            else:
                return [lP + 1, rP + 1] #adding one since the indices for this problem want to start at 1 not 0

Solution = Solution()

sortedList = [1,3,4,5,7,11]

print(Solution.twoSum(sortedList, 9))