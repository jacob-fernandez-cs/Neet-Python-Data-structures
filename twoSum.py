class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {} #value : index

        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[n] = i
        return

Solution = Solution()

nums = [2,7,11,15]
target = 9

print(Solution.twoSum(nums, target))





